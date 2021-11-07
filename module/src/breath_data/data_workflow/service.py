from breath_api_interface.proxy import ServiceProxy
from breath_api_interface.queue import Queue
from breath_api_interface.service_interface import Service
from breath_api_interface.request import Request, Response

class DataWorflow(Service):
    def __init__(self, proxy:ServiceProxy, request_queue:Queue):
        '''DataWorflow constructor.
        '''
        super().__init__(proxy=proxy, request_queue=request_queue)

    def run(self) -> None:
        '''Run the service, handling requests.
        '''

        request = self._get_request()

        if request is None:
            return

        response : Response = Response(sucess=False, response_data={"message": "Operation not available"})


        if request.operation_name == "load_open_sus_data":
            response = self._load_open_sus_data(request)

        request.send_response(response)

    def _load_open_sus_data(self, request:Request) -> Response:
        ...