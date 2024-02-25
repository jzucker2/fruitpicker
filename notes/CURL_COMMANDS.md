# Curl Commands

```
curl -i "http://localhost:1996/api/v1/check-under-voltage" \
-H "Content-Type: application/json"

# wake up the Roku here
curl -i "http://10.0.1.8:1996/api/v1/check-under-voltage" \
    -H "Content-Type: application/json"
```
