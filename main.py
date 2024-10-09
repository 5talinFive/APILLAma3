import requests
from fastapi import FastAPI
apiKey = "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";

app = FastAPI()

llama3_api_url = "https://api.groq.com/openai/v1/models"


#define los headers con tu API key
headers = {
    "Authorization": f"Bearer {apiKey}",
    "Content-type": "application/json"
}

#Cuerpo de la solicitud
data = {
    "prompt": "Escribe un poema sobre la tecnología"
}

#petición post a la Api
response = requests.post(llama3_api_url, json=data, headers=headers)

#verificamos la respuesta
if response.status_code == 200:
    result = response.json() #convertimos la respuesta en Json
    print(result)
else:
    print(f"Error {response.status_code}:{response.text}")







