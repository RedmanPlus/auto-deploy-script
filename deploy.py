from flask import Flask, request, json
from git_docker import *

app = Flask(__name__)

@app.route('/')
def index():
	return 'hi mom'

@app.route('/githubIssue',methods=['POST'])
def githubIssue():
	data = request.json
	print(data['ref'])
	if data['ref'] == 'refs/heads/main':
		update()
	return data

if __name__ == '__main__':
	app.run(debug=True)