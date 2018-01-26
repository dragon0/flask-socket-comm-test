from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    app.logger.info('lol')
    return render_template('index.html')

@socketio.on('connect', namespace='/browser')
def browser_connect():
    app.logger.info('browser connected ')

@socketio.on('disconnect', namespace='/browser')
def browser_connect():
    app.logger.info('browser disconnected ')

@socketio.on('value changed', namespace='/browser')
def browser_value_changed(message):
    app.logger.info('received message: ' + str(message))

@socketio.on('connect', namespace='/client')
def client_connect():
    session['client'] = 'something??'
    app.logger.info('client connected ' + session['client'])
    emit('client connected', {'msg': session['client']}, namespace='/browser')
    emit('aaa', {'msg': session['client']}, namespace='/client')

@socketio.on('disconnect', namespace='/client')
def client_connect():
    app.logger.info('client disconnected ')

if __name__ == '__main__':
    socketio.run(app, debug=True)

