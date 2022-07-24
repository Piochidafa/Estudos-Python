from flask import Flask, jsonify

app = Flask(__name__)


a = {'p1': {
    "firstName": "Adriel",
    "lastName": "sapeca",
    "gender": "Mulher",
    "age": 28
},

   'p2': {
      "firstName": "Junin",
      "lastName": "Caço",
      "gender": "Homem",
      "age": 55
   }
}


@app.route('/')
def ap():
    return jsonify(a)

app.run()

