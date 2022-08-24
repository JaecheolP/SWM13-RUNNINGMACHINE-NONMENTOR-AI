from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('main.html')

@app.route("/submit", methods=['POST'])
def submit():
	if (request.method == 'POST'):
		value = request.form.get('essayContent')
		totalScore = 5
		dockhaeScore = 3
		nonliScore = 2
		pyohyunScore = 2
		scores = {
			"message": "Success",
			"response": {
				"totalScore": totalScore,
				"logicScore": nonliScore,
				"expressionScore": pyohyunScore,
				"vocabularyScore": dockhaeScore,
			}
		}
		print(type(scores))
		print(json.dumps(scores))
		print(type(json.dumps(scores)))
		return render_template("gradeSheet.html", scores=json.dumps(scores), value=value)
if __name__ == '__main__':
	app.run()