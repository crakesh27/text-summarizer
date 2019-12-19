import requests

summary_api_url = 'https://ocsummary.herokuapp.com/summary'
headers = {'Content-type': 'application/json'}
json_data = {
    "Text": "Hi. This is Rakesh. I have query regarding printer. My HP printer 2520 is not working for past 2 days. I tried cleaning and restarting the printer. Please help me in fixing it.",
    "Ratio": 0.7
}

response = requests.get(summary_api_url, json = json_data, headers = headers)

print(response)

response = response.json()

print("Topic: " + response['Topic'])
print("Summary:")
print(response['Summary'])