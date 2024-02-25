from enum import Enum
from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics
from prometheus_flask_exporter import Counter, Summary


class Labels(Enum):
    DEVICE = 'device'

    @classmethod
    def labels(cls):
        return list([
            cls.DEVICE.value,
        ])


class Metrics(object):
    UNDER_VOLTAGE_CHECK_TIME = Summary(
        'fruitpicker_under_voltage_check_time',
        'Time spent to check if pi is under voltage')

    UNDER_VOLTAGE_CHECK_EXCEPTIONS = Counter(
        'fruitpicker_under_voltage_check_exceptions',
        'Exceptions while attempting to check if pi is under voltage')


# https://github.com/rycus86/prometheus_flask_exporter#app-factory-pattern
# https://github.com/rycus86/prometheus_flask_exporter/blob/master/examples/gunicorn-app-factory/app_setup.py
def get_metrics_app_factory():
    return GunicornPrometheusMetrics.for_app_factory()


metrics = get_metrics_app_factory()
