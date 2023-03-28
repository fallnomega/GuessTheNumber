import random

from flask import Flask

app = Flask(__name__)

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
    def generate_guess(*args):
        return random.randint(0, 9)
    return generate_guess

@app.route('/<int:number>')
@get_numbers
def show_results(number,the_guess):
    return f'<h1>{number} placeholder</h1>'



if __name__ == "__main__":
    app.run(debug=True, port=5000)
# if you get access denied on 127.0.0.1:5000 ; use chrome://net-internals/#sockets in browser.

# 4. Create a route that can detect the number entered by the user e.g "URL/3" or "URL/9" and checks that number
# against the generated random number. If the number is too low, tell the user it's too low, same with too high or if
# they found the correct number. try to make the <h1> text a different colour for each page.  e.g. If the random
# number was 5:
#
# 3 is too low:
#
#
#
# 7 is too high:
#
#
# and 5 is just right:
#
#
# Here are the GIF URLs I used, but it's way more fun finding your own on giphy.com
#
# High: https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif
#
# Low: https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif
#
# Correct: https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif
