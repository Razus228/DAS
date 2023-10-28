from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

chat_messages = []

@app.route('/')
def chat():
    return render_template('chat.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    chat_messages.append(message)
    return jsonify({"status": "Message sent"})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify(chat_messages)

if __name__ == '__main__':
    app.run(debug=True)
