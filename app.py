from flask import Flask, render_template
app = Flask(__name__)
TvShow = ["avengers", "forest-gum", "lion-king", "spide-man", "titanic"]
@app.route('/')
def index():
    return render_template("index.html", len=len(TvShow), TvShow=TvShow)
if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)