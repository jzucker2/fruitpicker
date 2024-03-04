from flask import current_app as app
from ..common.voltage_events import VoltageEvents
from ..metrics import Metrics
from rpi_bad_power import new_under_voltage


log = app.logger


# https://github.com/shenxn/rpi-bad-power?tab=readme-ov-file


class RPiBadPowerException(Exception):
    pass


class RPiBadPower(object):
    @classmethod
    def get_client(cls):
        return cls()

    @classmethod
    def get_event_for_result(cls, under_voltage_result):
        if under_voltage_result is None:
            log.info("System not supported.")
            return VoltageEvents.SYSTEM_NOT_SUPPORTED
        elif under_voltage_result.get():
            log.info("Under voltage detected.")
            return VoltageEvents.UNDER_VOLTAGE_DETECTED
        else:
            log.info("Voltage is normal.")
            return VoltageEvents.NORMAL

    @classmethod
    def _inc_voltage_event(cls, event):
        Metrics.UNDER_VOLTAGE_EVENT_COUNTER.labels(
            event=event.value,
        ).inc()

    @classmethod
    def check_under_voltage(cls):
        under_voltage = new_under_voltage()
        event = cls.get_event_for_result(under_voltage)
        cls._inc_voltage_event(event)
        if event == VoltageEvents.SYSTEM_NOT_SUPPORTED:
            Metrics.SYSTEM_SUPPORTED_VALUE.set(0)
            # TODO: would be cool to do something else here
            return None
        else:
            Metrics.SYSTEM_SUPPORTED_VALUE.set(1)
            final_value = event.under_voltage_value
            Metrics.UNDER_VOLTAGE_VALUE.set(final_value)
            return final_value
