from typing import Dict, List, Union
from breath_api_interface.proxy import ServiceProxy
from breath_api_interface.queue import Queue
from breath_api_interface.service_interface import Service
from breath_api_interface.request import Request, Response

from breath_data.bd_acess_point.relational_querier import RelationalQuerier

class BDAcessPoint(Service):
    '''BReATH service for provide BD acess

        :ivar relational_querier: Handles relational (SQL) queries
        :type relational_querier: breath_data.bd_acess_point.relational_querier.RelationalQuerier

        :ivar graph_querier: Handles graph (Neo4j) queries
        :type graph_querier: breath_data.bd_acess_point.graph_querier.GraphQuerier
    '''

    def __init__(self, proxy:ServiceProxy, request_queue:Queue):
        '''BDAcessPoint constructor.

            Initializes the service with the BDs.
        '''
        super().__init__(proxy=proxy, request_queue=request_queue)

        self.relational_querier = RelationalQuerier()
        self.graph_querier = GraphQuerier()
        

    def run(self) -> None:
        '''Run the service, handling BD requests.
        '''
        request = self._get_request()

        if request is None:
            return

        response : Response = Response(sucess=False, response_data={"message": "Operation not available"})

        if request.operation_name == "register_symptom":
            response = self._register_symptom(request)

        request.send_response(response)

        
    def _cancel_all(self):
        self.relational_querier.cancel()
        self.graph_querier.cancel()

    def _commit_all(self):
        self.relational_querier.commit()
        self.graph_querier.commit()

    def _register_symptom(self, request: Request) -> Response:
        
        user_id = request.request_info["user_id"]
        symptom_name = request.request_info["symptom_name"]
        
        year = request.request_info["year"]
        month = request.request_info["month"]
        day = request.request_info["day"]

        symptoms_types = self._search_symptom_type(symptom_name)

        if symptoms_types is None:
            self._cancel_all()
            return Response(sucess=False, response_data={"message": "Symptom type not found"})

        symptom_type_id = symptoms_types[0]["id"]

        users = self._search_user(user_id)

        if users is None:
            self._cancel_all()
            return Response(sucess=False, response_data={"message": "User not found"})

        patient_id = users[0]["Paciente"]
        city_id = users[0]["Cidade"]

        sql_query = "INSERT INTO Sintoma(Tipo, Ano, Mês, Dia, Cidade)"
        sql_query += " VALUES('{0}', '{1}', '{2}', '{3}', {4})".format(symptom_type_id, year, month, day, city_id)

        sucess, symptom = self.relational_query.query(sql_query)

        if not sucess:
            self._cancel_all()
            return Response(sucess=False, response_data={"message":"Error while registering symptom"})

        symptom_id = symptom[0]["id"]

        sql_query3 = "INSERT_INTO PacienteSintoma(Paciente, Sintoma) VALUES('{0}', '{1}')".format(patient_id, symptom_id)
        sucess, _ = self.relational_querier.query(sql_query3)

        if not sucess:
            self._cancel_all()
            return Response(sucess=False, response_data={"message":"Cannot register patient symptom relation"})

        self._commit_all()

        return Response(sucess=True)

    def _search_symptom_type(self, symptom_name:str) -> Union[List[Dict[str, str]], None]:
        neo_query = "MATCH (t:Tipo_Sintoma {{nome: {0}}}) RETURN t".format(symptom_name)        
        sucess, symptoms_types = self.graph_querier.query(neo_query)

        if not sucess:
            return None

        return symptoms_types

    def _search_user(self, user_id:int) -> Union[List[Dict[str, str]], None]:
        sql_query = "SELECT * FROM Usuarios WHERE Usuarios.id = {0}".format(user_id)
        sucess, users = self.relational_querier.query(sql_query)

        if not sucess:
            return None
        
        return users
