import os
from quart import Quart, request, jsonify
from collections import defaultdict
from dotenv import load_dotenv
from promptflow.core import Prompty, AzureOpenAIModelConfiguration
from copilot import get_chat_response  # Ajuste conforme o nome do seu arquivo
from quart_cors import cors  # Quart compatível com CORS

load_dotenv()

app = Quart(__name__)
app = cors(app)  # Habilitando CORS para todas as rotas

# Dicionário para armazenar o histórico de cada usuário
user_history = defaultdict(list)

@app.route('/chat', methods=['POST'])
async def chat():
    data = await request.get_json()
    user_input = data.get('input')
    user_id = data.get('user_id', 'default_user')  # Use um ID de usuário padrão se não estiver fornecido

    if not user_input:
        return jsonify({'error': 'Input não pode ser vazio.'}), 400

    # Recupera o histórico do usuário
    history = user_history[user_id]

    # Chama a função get_chat_response de forma assíncrona
    response = await get_chat_response(chat_input=user_input, chat_history=history)

    # Atualiza o histórico
    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": response['reply']})
    user_history[user_id] = history

    # Retorna a resposta e o histórico
    return jsonify({
        'reply': response['reply'],
        'context': response['context'],  # Inclui o contexto, se necessário
        'history': history
    })

if __name__ == '__main__':
    app.run(port=5000)
