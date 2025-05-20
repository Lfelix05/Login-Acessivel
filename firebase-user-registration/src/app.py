from flask import Flask, request, jsonify
from firebase_service import register_user

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')
    
    if password != confirm_password:
        return jsonify({'error': 'As senhas não coincidem.'}), 400
    
    try:
        user_id = register_user(email, password)
        return jsonify({'message': 'Usuário registrado com sucesso!', 'user_id': user_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)