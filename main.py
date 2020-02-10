from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit, send

app = Flask(__name__,
            static_folder="web/static",
            static_url_path="/static",
            template_folder="web/pages")
socketio = SocketIO(app)
ROOMS = {}  # dictionary to store rooms


@app.route("/")
def index():
    """Serve the index HTML"""
    return render_template("index.html")


@socketio.on('room_create')
def on_room_create(data):
    """Creates game lobby
    :param data: Data passed with event"""
    emit("join_room", {"room": "id123"})


if __name__ == "__main__":
    socketio.run(app)
