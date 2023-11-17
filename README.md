# capella
Take home for capella space devops engineer.

## Goal
Encoding a URL such as http://anywebsite.com/app/docs and returns an encoded URL such as http://someapp/GeAi9K.

## API Usage
#### POST /encode
This endpoint takes an input URL and returns a shortened version of it.
`{"url": "http://www.example.com/thisisalongexample"}`

#### GET /decode/<short-url>
This endpoint takes the shortened URL and returns the full URL.

## How to run
Assumes working dir is root of project and python is in path, may need to run python3 cmd instead.
```
pip install -r requirements.txt
python main.py
```

## How to call API
Once the service is running you can call the endpoints, examples shown in curl.
```
curl -X POST -H "Content-Type: application/json" -d '{"url": "http://www.example.com/thisisalongexample"}' http://127.0.0.1:5000/encode

curl http://127.0.0.1:5000/decode/cb21edc2
```
Where "cb21edc2" is what was returned from the POST.

## Testing
With the service running you can test with
```
python test_url.py
```
There will be a SSL warning during testing - not production grade code so ignore it.
