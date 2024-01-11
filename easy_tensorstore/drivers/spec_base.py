
from ..constant import TS_DRIVER
from ..json_base import JsonBase


class TsSpecBase(JsonBase):
    def __init__(self, 
                 driver: TS_DRIVER) -> None:
        self.driver = driver.value
