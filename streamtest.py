from flask import stream_with_context, request, Flask
from markupsafe import escape
import time

app = Flask(__name__)

@app.route("/")
def streamed_response():
    def generate():
        time.sleep(0.5)
        yield '<p>Hello '
        yield "sir"
        yield '!</p>'
        time.sleep(1)
        yield '<p>howareyou'
        yield '!</p>'
    return stream_with_context(generate())

app.run(debug=True)