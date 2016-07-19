from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path = "static", static_folder = "static")

@app.route('/')
def index():
    user = {'name': 'Arian'}
    return render_template('index.html', title='test', user=user)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
