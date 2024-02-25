from flask import current_app as app
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
    def check_under_voltage(cls):
        under_voltage = new_under_voltage()
        if under_voltage is None:
            log.info("System not supported.")
        elif under_voltage.get():
            log.info("Under voltage detected.")
        else:
            log.info("Voltage is normal.")
