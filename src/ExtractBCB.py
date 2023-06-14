from typing import Any
import bcb
import pandas as pd

class BCBExtractor:

    def __init__(self) -> None:
        self.expectativas = bcb.Expectativas()
        self.sgs = bcb.sgs.SGS()


    def get(self, endpoint: str) -> Any:
        return self._bcb.get_endpoint(endpoint)

