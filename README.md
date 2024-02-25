# fruitpicker

## Prometheus

To add to `prometheus`, use something like this in `prometheus.yml` file:

```
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
