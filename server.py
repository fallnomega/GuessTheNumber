import random

from flask import Flask

app = Flask(__name__)
SYSTEM_NUMBER = random.randint(0, 9)


@app.route('/')
def greet():
    return f"<h1>Guess a number between 0 and 9</h1>" \
           f"<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'><br><br>" \
           f"<a href=\"/0\">0</a><br>" \
           f"<a href=\"/1\">1</a><br>" \
           f"<a href=\"/2\">2</a><br>" \
           f"<a href=\"/3\">3</a><br>" \
           f"<a href=\"/4\">4</a><br>" \
           f"<a href=\"/5\">5</a><br>" \
           f"<a href=\"/6\">6</a><br>" \
           f"<a href=\"/7\">7</a><br>" \
           f"<a href=\"/8\">8</a><br>" \
           f"<a href=\"/9\">9</a><br>"


def get_numbers(function):
    def generate_guess(number):
        if SYSTEM_NUMBER < int(number):
            return '<h1 style="color:red;">Too high, guess again</h1><br>' \
                   '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
        elif SYSTEM_NUMBER > int(number):
            return '<h1 style="color:blue;">Too low, guess again</h1><br>' \
                   '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
        else:
            return '<h1 style="color:green;">You guessed correct</h1><br>' \
                   '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

    return generate_guess


@app.route('/<int:number>')
@get_numbers
def show_results(number):
    return f'<h1>{number}</h1>'


if __name__ == "__main__":
    app.run(debug=True, port=5000)
