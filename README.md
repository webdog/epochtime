# Epoch Time

`A simple, flask microservice that returns epoch time to an int-friendly format on an HTTP GET request. Useful for stateless architecture.

## How to run:

`docker build -t epochtime:latest .` 


`docker run -itd -p 8080:8080 epochtime:latest`  

```
import requests
response = requests.get('localhost:8080')
print(response.body)
1532468906.0
``` 
