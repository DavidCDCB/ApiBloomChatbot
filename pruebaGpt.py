import requests

url = "https://you-chat-gpt.p.rapidapi.com/"

headers = {
	"X-RapidAPI-Key": "8d2f313a48msh601880f56aefda7p1386eejsn9e539a3674a0",
	"X-RapidAPI-Host": "you-chat-gpt.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
