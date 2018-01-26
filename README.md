# flask-socket-comm-test

Small example of a Flask web server communicating with a backend service using SocketIO.

`server.py` contains the Flask web server.
The served index page opens a SocketIO connection back to the server.

`client.py` contains a backend service using [SocketIO-Client](https://pypi.python.org/pypi/socketIO-client).
It opens a SocketIO connection to the server, which then broadcasts a message to the browser.
