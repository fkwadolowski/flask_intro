from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World"


# aby zadziałało set FLASK_APP=hello.py
# flask --app hello.py run

# if __name__=="__main__":
#     app.run()
@app.route("/bye")  # Diffrent routes
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")  # Variables and path converting
def greet(name,number):
    return f"Hello {name},do you like number:{number}?"


if __name__ == "__main__":
    app.run(debug=True)
