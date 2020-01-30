import requests
import json
import string
import hashlib


req = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=9d03d611b6b7b76712792ecaa775a0012cd96825")

json_dict = json.loads(req.content)


# lista das letras do alfabeto
alfabeto = string.ascii_lowercase

print(alfabeto)
print(json_dict)

# armazenamento das informações do JSON localmente
numero_casas = json_dict["numero_casas"]
mensagem_decifrada = ""
mensagem_cifrada = json_dict["cifrado"]

mensagem_cifrada = mensagem_cifrada.lower()

for letra in mensagem_cifrada:
    if letra in alfabeto:
        posicao = alfabeto.find(letra)
        posicao = (posicao - numero_casas) % 26
        mensagem_decifrada = mensagem_decifrada + alfabeto[posicao]
    else:
        mensagem_decifrada = mensagem_decifrada + letra

print(mensagem_decifrada)

json_dict["decifrado"] = mensagem_decifrada

sha1 = hashlib.sha1(mensagem_decifrada.encode())
json_dict["resumo_criptografico"] = sha1.hexdigest()

#req = requests.post("https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=9d03d611b6b7b76712792ecaa775a0012cd96825",data=json_dict)

print(json_dict)

with open("answer.json","w") as f:
    json.dump(json_dict, f, ensure_ascii=False, indent=4)


