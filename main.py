from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": "*"}})

data_store = []

@app.route('/users', methods=['POST'])
def cadastro():
    dados = request.get_json()

    required_fields = ['nome', 'sobrenome', 'email', 'telefone']
    for field in required_fields:
        if field not in dados:
            return jsonify({"error": f"Campo '{field}' é obrigatório."}), 400

    data_store.append(dados)

    return jsonify({"message": "Cadastro realizado com sucesso!", "data": dados}), 201

@app.route('/users', methods=['GET'])
def listagem():
    return jsonify(data_store), 200

if __name__ == '__main__':
    app.run(debug=True)
