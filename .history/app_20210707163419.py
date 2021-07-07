from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def upload():
	if request.method == 'GET':
		return render_template("index.html")
	# else:
    #     return "oops! 404 page not found"


if __name__ == "__main__":
    app.run('0.0.0.0',5000)