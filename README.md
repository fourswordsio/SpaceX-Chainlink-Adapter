# SpaceX-Chainlink-Adapter

### SpaceX API:
* https://docs.spacexdata.com
* No API Key needed

### Example:
```sh
python3 run.py
curl -X POST -H "Content-Type: application/json" http://localhost:8080 -d '{ "id": 0 }'
```

### Result:
{
  "data": {
    "flight_number": 107, 
    "launch_center": "Kennedy Space Center Historic Launch Complex 39A", 
    "launch_time": "2020-11-16T00:27:00.000Z", 
    "mission_id": "EE86F74", 
    "mission_name": "Crew-1", 
    "rocket_name": "Falcon 9"
  }, 
  "jobRunID": 1, 
  "result": "2020-11-16T00:27:00.000Z", 
  "statusCode": 200
}