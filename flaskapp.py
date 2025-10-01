from flask import Flask, request, jsonify, render_template, redirect, url_for
from Producer import say_hello

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()            #get the data from front end
    key = data.get('key')

    if not key:
        return jsonify({'error': 'Key is required'}), 400

    try:
        message = say_hello(key)
        return jsonify({'message': message, 'status': 'sent'}), 200, redirect(url_for('welcome', ket=key))                      #send the data to frontend
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/welcome/<ket>')
def welcome(ket):
    return f"Welcome {ket}"


if __name__ == '__main__':
    app.run(debug=True)

