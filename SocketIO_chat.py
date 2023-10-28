from flask import Flask, render_template, request
from flask_socketio import SocketIO
from flask_migrate import Migrate
app = Flask(__name__)
socketio = SocketIO(app)

# A dictionary to store connected clients
connected_clients = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    client_id = request.sid
    connected_clients[client_id] = None
    print(f"Client {client_id} connected")

@socketio.on('disconnect')
def handle_disconnect():
    client_id = request.sid
    connected_clients.pop(client_id, None)
    print(f"Client {client_id} disconnected")

@socketio.on('message')
def handle_message(data):
    client_id = request.sid
    message = data['message']
    # Broadcast the message to all connected clients
    socketio.emit('message', {'message': message, 'sender': client_id})

if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
