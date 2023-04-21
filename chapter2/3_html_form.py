from flask import *

# おまじない
app = Flask(__name__)

# トップページ（"/"）にGETリクエストが来たら実行される
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    prompt = request.form["prompt_text"]
    print(prompt)
    return "dummy text"

# Webサーバーを起動するおまじない
if __name__ == "__main__":
    app.run(debug=True)
