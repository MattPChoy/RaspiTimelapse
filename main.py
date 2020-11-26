from flask import Flask as flask
app = flask(__name__)

@app.route("/")
def main():
    return 'Hello World'

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = False)