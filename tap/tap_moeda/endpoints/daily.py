from datetime import datetime
import requests
from singer import get_logger

from tap_moeda.endpoints.endpoint import Endpoint

LOGGER = get_logger()

class Daily(Endpoint):
    def __init__(self, config) -> None:
        super().__init__(config)

    def sync(self, stream) -> list:
        session= requests.Session()
        params = self.config
        endpoint = f'/{stream}/{params["currency"]}/?start_date= {params["start_date"]}&end_date={params["end_date"]}'
        endpoint_url = self.base_url + endpoint
        LOGGER.info("URL = " + endpoint_url)
        response = self.get_data(params=endpoint_url)

        return response.json