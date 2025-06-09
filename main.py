import requests
import json

API_KEY = "AIzaSyBPqp1vpv2bouyJf6yGNkUoDMQiNiz17Tw"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [
        {
            "parts": [
                {"text": "39lti 3la smitit li 9ltlk ??"}
            ]
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

# Affichage du résultat
if response.status_code == 200:
    result = response.json()
    print(result["candidates"][0]["content"]["parts"][0]["text"])
else:
    print("Erreur:", response.status_code, response.text)
