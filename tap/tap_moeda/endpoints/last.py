import requests
from singer import get_logger

from tap_moeda.endpoints.endpoint import Endpoint

LOGGER = get_logger()


class Last(Endpoint):
    def __init__(self,config) -> None:
        super().__init__(config)

    def sync(self,stream) -> list:
        parameter = self.config['currency']
        endpoint = f'/{stream}/{parameter}'
        endpoint_url = self.base_url + endpoint
        LOGGER.info("URL = " + endpoint_url)
        response = self.do_request(endpoint_url=endpoint_url, session=session)

        return response.json
