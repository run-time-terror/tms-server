# TMS Server

Backend server for Traffic Monitoring system


## API

```json
POST  http://<server>:8008/process  HTTP/1.1

Content-Type: application/json
```

Body
```json
{
	"time": "Wed Mar 18 2020 23:02:52 GMT+0600",
	"image": "<blob>",
	"speed": 12.41,
	"speed_unit": "km/h"
}
```