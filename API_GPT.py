import json
import openai
from flask import Flask, request, jsonify

# Carrega os dados do arquivo JSON
with open('eventos_teste.json', 'r') as file:
    eventos_data = json.load(file)

# Configuração da API da OpenAI
openai.api_key = "SUA CHAVE"

# Inicialização do servidor Flask
app = Flask(__name__)

# Rota para lidar com as perguntas sobre eventos
@app.route('/pergunta-evento', methods=['POST'])
def pergunta_evento():
    # Obtém a pergunta do usuário da requisição POST
    pergunta = request.json['pergunta']

    # Realiza a chamada à API do ChatGPT
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você está buscando informações sobre eventos."},
            {"role": "system", "content": json.dumps(eventos_data)},
            {"role": "user", "content": pergunta}
        ]
    )

    return jsonify({'resposta': resposta.choices[0].message.content})

# Execução do servidor Flask
if __name__ == '__main__':
    app.run()

## para testar no postman
# http://localhost:5000/pergunta-evento
