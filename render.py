from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html" , name="Simple web");   

#remove port and debug during production
if __name__ == "__main__":
    app.run() 
