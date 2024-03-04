from flask import current_app as app
from ..utils import global_get_now
from .rpi_bad_power import RPiBadPower


log = app.logger


class ExporterException(Exception):
    pass


class Exporter(object):
    DEFAULT_SYSTEM_HEALTH_VALUE = 'missing'

    @classmethod
    def get_client(cls, rpi_power_client=None):
        if not rpi_power_client:
            rpi_power_client = RPiBadPower.get_client()
        return cls(rpi_power_client)

    def __init__(self, rpi_power_client):
        super().__init__()
        self.rpi_power_client = rpi_power_client
        self._last_power_value = None

    @classmethod
    def get_now(cls):
        return global_get_now()

    def __repr__(self):
        return f'Exporter => blah: {self._last_power_value}'
