# Curl Commands

```
curl -i "http://localhost:5566/api/v1/check-under-voltage" \
-H "Content-Type: application/json"

# check on a device
curl -i "http://10.0.1.8:5566/api/v1/check-under-voltage" \
    -H "Content-Type: application/json"
```

## Dev

```
curl -i "http://10.0.1.8:5566/api/v1/rpi-power/debug" \
-H "Content-Type: application/json"

curl -i "http://10.0.1.8:5566/api/v1/rpi-power/collector/simple" \
-H "Content-Type: application/json"

curl -i "http://10.0.1.8:5566/api/v1/rpi-power/collector/metrics/update" \
-H "Content-Type: application/json"
```
