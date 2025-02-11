from flask import Flask

app = Flask("littleflaskapp")

@app.route("/")
def Index():
	return "<h1>My Little Flask App</h1>"

app.run('0.0.0.0', 5000, debug=True) 
