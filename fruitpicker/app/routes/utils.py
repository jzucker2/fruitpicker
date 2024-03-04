from flask import current_app as app
from ..utils import get_version


log = app.logger


PRIVACY_POLICY = """
All your base are belong to us! But really, this is only intended for use by a single individual right now. So go away, please.
"""  # noqa: E501


# Keep this simple for debugging
# and to reduce imports here
@app.route('/hey')
@app.route('/api/v1/hey')
@app.route('/utils/hey')
def hey():
    log.debug('hey route')
    return {'message': 'in a bottle'}


@app.route('/health')
@app.route('/api/v1/health')
@app.route('/utils/health')
def health_check():
    log.debug('health route')
    return {
        'status': 'healthy',
        'server': 'fruitpicker',
        'version': get_version(),
    }


@app.route('/utils/version')
def version():
    return {
        # FIXME: replace with a constant
        'server': 'fruitpicker',
        'version': get_version(),
    }


@app.route("/privacy")
def privacy_policy():
    policy_string = PRIVACY_POLICY.strip().strip('\n').replace('\n', '')
    return f"<p>{policy_string}</p>"
