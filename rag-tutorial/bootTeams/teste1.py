import requests
import json

# Defina a URL do seu endpoint
#endpoint_url = "https://clamed.openai.azure.com/openai/deployments/text-embedding-3-small/embeddings?api-version=2023-05-15"

# Substitua pela sua chave de API
api_key = "d47b856c6ed44e90ba3a3e4d38385631"  # Certifique-se de que sua chave de API esteja aqui

import requests

# Defina suas credenciais
resource_name = "clamed"  # Nome do seu recurso Azure OpenAI
deployment_name = "text-embedding-3-small"  # Nome do deployment
endpoint = f"https://{resource_name}.openai.azure.com/openai/deployments/{deployment_name}/embeddings?api-version=2023-05-15"
api_key = "d47b856c6ed44e90ba3a3e4d38385631"  # Substitua pelo valor da chave copiada

# Defina os cabeçalhos
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Defina o corpo da solicitação
data = {
    "input": "Seu texto aqui"  # Substitua pelo texto que você deseja enviar
}

# Faça a solicitação
response = requests.post(endpoint, headers=headers, json=data,verify=False)

# Verifique o status e a resposta
if response.status_code == 200:
    print("Resposta:", response.json())
else:
    print("Erro:", response.status_code, response.text)
