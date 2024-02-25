#!/usr/bin/env python3
from app import create_app


if __name__ == "__main__":
    app = create_app()
    host = app.config.get('FRUITPICKER_HOST')
    port = app.config.get('FRUITPICKER_PORT')
    app.run(host=host, port=port, debug=True)
