from typing import Tuple, Union, List, Dict


class GraphQuerier:

    def cancel(self):
        pass

    def _commit_all(self):
        pass

    def query(self, query:str) -> Tuple[bool, Union[List[Dict[str, str]], None]]:
        return False, None