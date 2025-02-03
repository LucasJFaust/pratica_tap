from typing import List

import requests
from requests.adapters import HTTPAdapter
from datetime import datetime
from abc import ABC


#Classe com o construtor. O ABC é uma classe básica que a classe esta herdando para facilitar.
class Endpoint(ABC):

    def __init__(self, config) -> None:
        self.base_url = "https://economia.awesomeapi.com.br/json"
        self.config = config
        self.header = {}

    # Esse método básicamente vai inicialisar uma sessão para nós, chamar o
    # método que faz a request e vai inserir para cada record (linha da tabela ou API) no for o dado extract_at
    def get_data(self, params) -> List:
        session = requests.Session()

        response = self.do_request(endpoint_url=params, session=session)

        if type(response) is list:
            for record in response:
                # Com essa lógica, para cada linha extraida vamos adicionar o datetime
                record['extracted_at'] = str(datetime.now())

        return response

    # Método para fazero request. É ele que vai receber a sessão
    def do_request(
        self,
        endpoint_url,
        session: requests.Session
    ) -> requests.Response:

        response = self.mount_retry_session(session=session).get(
            endpoint_url,
            header=self.header,
            auth=None,
            params=None
        )

        return response

    def mount_session(
        self,
        session=None
    ):
        session = session or requests.Session()
        # Através dessa adapter é que vamos montar a sessão
        adapter = HTTPAdapter()
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session
