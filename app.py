from flask import Flask, render_template, Response, request, jsonify, make_response
from rake_nltk import Rake
rake_nltk_var = Rake()

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajax_action',methods=["POST"])
def ajax_action():
	print("djhghj")
	sentenceTxt = request.get_json()
	text = sentenceTxt['name']
	rake_nltk_var.extract_keywords_from_text(text)
	keyword_extracted = rake_nltk_var.get_ranked_phrases()
	return keyword_extracted

@app.route('/success')
def success():
	return render_template('success.html')

if __name__ == "__main__":
	app.run(host="127.0.0.1",debug=True,threaded=True)
