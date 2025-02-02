from typing import Dict, List

from singer.logger import get_logger
from tap_moeda.endpoints.last import Last
from tap_moeda.endpoints.daily import Daily
from tap_moeda.endpoints.endpoint import Endpoint


class Currency(Endpoint):
    # Construtor da classe
    def __init__(self, config: Dict) -> None:
        self.config = config

    # É quem vai fazer a conexão checando o catalog.
    def sync(self, stream: str) -> List:
        if stream == "last":
            data = Last(self.config).sync(stream)
        elif stream == "daily":
            data = Daily(self.config).sync(stream)
        else:
            raise ValueError(f"Unrecognized stream: {stream}")

        return data