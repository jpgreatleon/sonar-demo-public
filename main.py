from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/sonar')
def hello():
    return "Hello SonarQube!"

if __name__ == '__main__':
    app.run()
