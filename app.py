from flask import Flask, render_template, Response, request, jsonify, make_response


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form_action', methods=["POST"])
def form_action():
	print(request.form['username'])
	print(request.form['password'])
	return render_template('success.html')

@app.route('/ajax_action',methods=["POST"])
def ajax_action():
	print("djhghj")
	print(request.get_json())
	return "success"

@app.route('/success')
def success():
	return render_template('success.html')

if __name__ == "__main__":
	app.run(host="0.0.0.0",debug=True,threaded=True)
