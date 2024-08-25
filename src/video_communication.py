from src import socketio

@socketio.on('incoming_call')
def incoming_call(message):
    socketio.emit('call_received', message)

@socketio.on('handshake')
def call_accepted(message):
    socketio.emit('pair', message)