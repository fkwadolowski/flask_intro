from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center"> World!</h1><p> This is ' 
            'paragraph.</p><img '
            'src="https://media.giphy.com/media/v1'
            '.Y2lkPTc5MGI3NjExb2dteWZocGhjanIwYWpwcWM2bHliaWNhamZodGtzOGNmMGh2Z3FlNyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3oEdvaAhIxot8KIKiI/giphy.gif" width=200>')


# aby zadziałało set FLASK_APP=hello.py
# flask --app hello.py run

# if __name__=="__main__":
#     app.run()
@app.route("/bye")  # Diffrent routes
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")  # Variables and path converting
def greet(name, number):
    return f"Hello {name},do you like number:{number}?"


if __name__ == "__main__":
    app.run(debug=True)
