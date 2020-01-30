import requests
import json
import string

req = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=9d03d611b6b7b76712792ecaa775a0012cd96825")

js = json.loads(req)

# lista das letras do alfabeto
beto = list(string.ascii_lowercase)

print(beto)
print(js)

