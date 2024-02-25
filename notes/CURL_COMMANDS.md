# Curl Commands

```
curl -i "http://10.0.1.104:1996/api/v1/magic/packet" \
-H "Content-Type: application/json"

# wake up the Roku here
curl -i -X POST "http://10.0.1.104:1996/api/v1/magic/packet" \
    -H "Content-Type: application/json" \
    -d '{"ip_address":"10.0.1.102","mac_address":"f0:a3:b2:79:0b:fe"}'
```
