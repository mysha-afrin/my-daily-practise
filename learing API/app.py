from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "hello world,It's my first API project"
@app.route('/drinks')
def drinks():
    return {"drinks": ["coffee", "tea", "juice"]}
if __name__ == "__main__":
    app.run(debug=True)
