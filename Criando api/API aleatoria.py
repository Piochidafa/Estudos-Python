
from flask import Flask, jsonify

a = {
   "firstName": "Joe",
   "lastName": "Jackson",
   "gender": "male",
   "age": 28
}
app = Flask(__name__)

@app.route('/')
def homepage():
    return jsonify(a)

app.run()