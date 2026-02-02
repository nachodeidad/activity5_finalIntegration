from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html')
@app.route("/map")
def map():
    return render_template('interactiveMap.html')

if __name__ == "__main__":
    app.run(debug=True)