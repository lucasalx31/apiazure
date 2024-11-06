import os
import requests
from dotenv import load_dotenv
from azure.identity import ClientSecretCredential

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter credenciais do Azure
tenant_id = os.getenv("AZURE_TENANT_ID")
client_id = os.getenv("AZURE_CLIENT_ID")
client_secret = os.getenv("AZURE_CLIENT_SECRET")

# Criar um objeto de credencial
credential = ClientSecretCredential(tenant_id, client_id, client_secret)
print(os.getenv("AZURE_CLIENT_ID"))
# Obter o token de acesso
token = credential.get_token("https://botclamedteste.eastus.inference.ml.azure.com/.default").token

# Definir o endpoint e o cabeçalho
endpoint = "https://botclamedteste.eastus.inference.ml.azure.com/score"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Definir o payload
payload = {"data": "sua_payload"}  # Substitua pelo seu payload real

# Fazer a chamada ao endpoint
response = requests.post(endpoint, headers=headers, json=payload)

# Verificar a resposta
print(response.status_code)
print(response.json())
