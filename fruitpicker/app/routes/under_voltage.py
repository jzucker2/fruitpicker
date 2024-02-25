from flask import current_app as app
from ..routers.under_voltage_router import UnderVoltageRouter


log = app.logger


@app.route('/api/v1/check-under-voltage')
async def check_under_voltage():
    router = UnderVoltageRouter()
    return await router.check_under_voltage_response()
