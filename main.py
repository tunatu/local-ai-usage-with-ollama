from flask import Flask, render_template, request, stream_with_context, Response
import requests
import json

app = Flask(__name__)

MODEL = "yourmodelhere"

SABLON = {
    "model": MODEL,
    "stream": True
}
def handle_prompt(inpp):
    sablon_local = SABLON.copy()
    sablon_local["messages"] = [
        {"role": "user", "content": inpp}
    ]

    try:
        with requests.post(
            "http://127.0.0.1:11434/api/chat",
            json=sablon_local,
            stream=True
        ) as r:
            for line in r.iter_lines():
                if not line:
                    continue
                try:
                    d = json.loads(line.decode("utf-8"))
                    if "message" in d and "content" in d["message"]:
                        yield d["message"]["content"]
                    elif d.get("done"):
                        break
                except Exception as e:
                    yield f"\n[Error parsing stream: {e}]\n"
    except Exception as e:
        yield f"\n[Request error: {e}]\n"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")

    if request.method == "POST":
        inpp = request.form.get("texin")
        if not inpp:
            return render_template("home.html", response="If you can see this it means no data was entered.")
        return Response(
            stream_with_context(handle_prompt(inpp)),
            content_type="text/plain"
        )

if __name__ == "__main__":
    app.run(debug=True)
