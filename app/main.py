import os

from dotenv import load_dotenv
from web3 import AsyncWeb3, Web3
from web3.types import BlockData


load_dotenv()
PROJECT_ID = os.getenv('ProjectID')


class MainNetConnection:
    _w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.blastapi.io/' + PROJECT_ID))

    def __init__(self) -> None:
        pass

    def is_connected(self):
        return self._w3.is_connected()

    def get_block(self, type: str = 'latest') -> BlockData:
        """
        type: earliest | latest | finalized | pending | safe
        """
        return self._w3.eth.get_block(type)
