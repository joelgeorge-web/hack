import webbrowser
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/user1')
def user1():
    return render_template('user1.html')

@app.route('/user2')
def user2():
    return render_template('user2.html')

@socketio.on('message')
def handle_message(data):
    message = data['message']
    sender = data['sender']
    # Broadcast the message to all connected users
    emit('new_message', {'message': message, 'sender': sender}, broadcast=True)

# Function to open the browser after the first request
def open_browser():
    webbrowser.open('http://127.0.0.1:5000/user1', new=2)  # Opens user1.html
    webbrowser.open('http://127.0.0.1:5000/user2', new=2)  # Opens user2.html

if __name__ == '__main__':
    # Register the open_browser function to be executed after the first request
    app.before_first_request(open_browser)

    # Start the Flask-SocketIO server
    socketio.run(app, debug=True)
