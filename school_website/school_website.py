import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

global counter
counter = 0


def increment():
    global counter
    counter += 1


@app.route('/')
def index():
    print(counter)
    increment()
    return render_template('index.html', title='test', counter=counter)


if __name__ == "__main__":
    app.debug = True
    app.run(app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 5000))))
