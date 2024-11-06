import requests

# URL da sua API
url = "http://127.0.0.1:5000/chat"

# Função para testar a API
def test_api():
    user_input = input("Faça sua pergunta: ")
    
    # Cria o corpo da requisição
    payload = {
        "input": user_input,
        "user_id": "usuario_exemplo"  # Você pode usar um ID de usuário fixo ou gerar um
    }
    
    # Faz a requisição POST
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        response_data = response.json()
        print("Resposta do bot:", response_data['reply'])
    else:
        print("Erro ao chamar a API:", response.status_code, response.text)

if __name__ == "__main__":
    test_api()
