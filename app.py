from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 取得使用者輸入的選項
        options = request.form.get("options").splitlines()
        return render_template("index.html", options=options, spin=True)
    return render_template("index.html", options=None, spin=False)

if __name__ == "__main__":
    app.run(debug=True)
