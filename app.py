from flask import Flask

app = flask("littleflaskapp")

@app.route("/")
def Index():
	return "<h1>My Little Flask App</h1>"

 
