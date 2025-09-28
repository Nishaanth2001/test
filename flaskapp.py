from flask import Flask, request, jsonify
from Producer import say_hello

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    key = data.get('key')

    if not key:
        return jsonify({'error': 'Key is required'}), 400

    try:
        message = say_hello(key)
        return jsonify({'message': message, 'status': 'sent'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':

#     app.run(debug=True)
