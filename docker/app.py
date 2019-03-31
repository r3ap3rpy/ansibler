from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Docker, and Ansible and Python in a single video... isnt it cool?"

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=9999)