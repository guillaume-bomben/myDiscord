from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg['data'])
    emit('message', {'username': msg['username'], 'message': msg['data']}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
