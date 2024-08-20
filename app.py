from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/home')
def home():

    content = 'hello world '
    return render_template(
        'index.html',
        content = content
        )

if __name__ == '__main__':
    app.run(debug=True)