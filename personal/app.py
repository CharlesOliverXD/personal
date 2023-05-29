from flask import Flask , render_template , url_for

app = Flask(__name__)


@app.route('/')
def home_():

    return render_template("contents/index.html")


if __name__ =="__main__":
    app.run()