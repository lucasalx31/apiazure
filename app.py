import os
from flask import Flask, request, jsonify
from collections import defaultdict
from dotenv import load_dotenv
from promptflow.core import Prompty, AzureOpenAIModelConfiguration
from copilot import get_chat_response  # Ajuste conforme o nome do seu arquivo

load_dotenv()

app = Flask(__name__)

# Dicionário para armazenar o histórico de cada usuário
user_history = defaultdict(list)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('input')
    user_id = data.get('user_id', 'default_user')  # Use um ID de usuário padrão se não estiver fornecido

    if not user_input:
        return jsonify({'error': 'Input não pode ser vazio.'}), 400

    # Recupera o histórico do usuário
    history = user_history[user_id]

    # Chama a função get_chat_response
    response = get_chat_response(chat_input=user_input, chat_history=history)

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
