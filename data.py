import requests

parameters = {
    "amount": 10,
    "category": 18, # 18 for Computer Science category
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
questions = response.json()
question_data = questions["results"]
