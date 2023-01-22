from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print("Changing the wifi credentials to")
        print("SSID: ", request.form["SSID"])
        print("password: ", request.form["password"])
        return render_template("home.html")

    return render_template("home.html")

if __name__ == "__main__":
   app.run()
