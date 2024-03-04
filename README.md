# fruitpicker

This is inspired by [rpi-bad-power](https://pypi.org/project/rpi-bad-power/) 
out of the [Home Assistant Raspberry Pi power supply checker integratio](https://www.home-assistant.io/integrations/rpi_power/) 
that I found really useful and helpful. However, I did not 
want to run `Home Assistant` on every `RPi` in my house. So I came 
up with this little python flask applet.

## Example Deploy

This is an example `docker-compose.yml` for deploying on your home network.

```
version: '3.7'

services:

  fruitpicker:
    container_name: fruitpicker
    image: ghcr.io/jzucker2/fruitpicker:latest
    restart: always
    healthcheck:
      test: [ "CMD-SHELL", "curl -f http://host.docker.internal:5566/api/v1/health || exit 1" ]
      interval: 30s
      timeout: 60s
      retries: 5
      start_period: 80s
    extra_hosts:
      - "host.docker.internal:host-gateway"
    ports:
      - 5566:5566
      - 9266:9266
    volumes:
      # Note: it's important to mount in `/sys` in order to access the host's power status
      - /sys:/sys:ro
    stdin_open: true
```

## Prometheus

Then you want to scrape these stats with your [Prometheus](https://prometheus.io/) scraper. Here's an example to add your `prometheus.yml`

```yaml
  - job_name: 'fruitpicker'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.
    static_configs:
      - targets: [ '10.0.1.131:9266' ]
        labels:
          instance: 'remote_pi'
      - targets: [ 'host.docker.internal:9266' ]
        labels:
          instance: 'local_pi'
```
