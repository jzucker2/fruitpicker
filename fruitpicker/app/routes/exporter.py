from flask import current_app as app
from ..routers.exporter_router import ExporterRouter


log = app.logger


@app.route('/api/v1/rpi/exporter/simple')
@app.route('/api/v1/rpi-power/exporter/simple')
def handle_simple_exporter_route():
    router = ExporterRouter()
    return router.handle_simple_exporter_route_response()


@app.route('/api/v1/rpi/exporter/metrics/update')
@app.route('/api/v1/rpi-power/exporter/metrics/update')
def handle_exporter_metrics_update_route():
    router = ExporterRouter()
    return router.handle_exporter_metrics_update_route_response()
