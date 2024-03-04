from enum import Enum
from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics
from prometheus_flask_exporter import Counter, Summary, Gauge


class Labels(Enum):
    DEVICE = 'device'
    EVENT = 'event'

    @classmethod
    def labels(cls):
        return list([
            cls.DEVICE.value,
        ])

    @classmethod
    def voltage_event_labels(cls):
        return list([
            cls.EVENT.value,
        ])


class Metrics(object):
    DEBUG_ROUTE_TIME = Summary(
        'fruitpicker_debug_route_time',
        'Time spent to handle debug route request')

    DEBUG_ROUTE_EXCEPTIONS = Counter(
        'fruitpicker_debug_route_exceptions',
        'Exceptions while attempting to handle debug route request')

    UNDER_VOLTAGE_CHECK_TIME = Summary(
        'fruitpicker_under_voltage_check_time',
        'Time spent to check if pi is under voltage')

    UNDER_VOLTAGE_CHECK_EXCEPTIONS = Counter(
        'fruitpicker_under_voltage_check_exceptions',
        'Exceptions while attempting to check if pi is under voltage')

    SIMPLE_EXPORTER_ROUTE_TIME = Summary(
        'fruitpicker_simple_exporter_route_time',
        'Time spent to handle simple exporter route request')

    SIMPLE_EXPORTER_ROUTE_EXCEPTIONS = Counter(
        'fruitpicker_simple_exporter_route_exceptions',
        'Exceptions while attempting to handle simple exporter route request')

    EXPORTER_METRICS_UPDATE_ROUTE_TIME = Summary(
        'fruitpicker_exporter_metrics_update_route_time',
        'Time spent to handle exporter metrics update route request')

    EXPORTER_METRICS_UPDATE_ROUTE_EXCEPTIONS = Counter(
        'fruitpicker_exporter_metrics_update_route_exceptions',
        'Exceptions while attempting exporter metrics update route request')

    SYSTEM_SUPPORTED_VALUE = Gauge(
        'fruitpicker_system_supported_value',
        'If this sets to 0 than system cannot report other voltage values'
    )

    UNDER_VOLTAGE_VALUE = Gauge(
        'fruitpicker_under_voltage_value',
        'The under voltage value is 1 if detecting bad power'
    )

    UNDER_VOLTAGE_EVENT_COUNTER = Counter(
        'fruitpicker_under_voltage_event_count',
        'The count of voltage related events',
        Labels.voltage_event_labels()
    )


# https://github.com/rycus86/prometheus_flask_exporter#app-factory-pattern
# https://github.com/rycus86/prometheus_flask_exporter/blob/master/examples/gunicorn-app-factory/app_setup.py
def get_metrics_app_factory():
    return GunicornPrometheusMetrics.for_app_factory()


metrics = get_metrics_app_factory()
