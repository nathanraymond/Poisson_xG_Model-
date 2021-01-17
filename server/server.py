from flask import Flask, jsonify, request, render_template, url_for, send_from_directory, make_response
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)
@app.route('/')
def home():
    return render_template('home.html')

@app.route("/create-entry", methods=["POST"])
def create_entry():

	req = request.get_json()

	res = make_response(jsonify(req), 200)

	return res

    
if __name__ == '__main__':
    app.run(debug=True)
