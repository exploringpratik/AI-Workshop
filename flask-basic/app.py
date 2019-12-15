from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def Index():
    data = {'A': 'A for Apple', 'B': 'B for Ball', 'C': 'C for Cat'}
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)

