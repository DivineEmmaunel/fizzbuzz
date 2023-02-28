from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
@app.route('/')
def test():
    return redirect(url_for('fizzbuzz'))

@app.route("/fizzbuzz")
def fizzbuzz():
    return render_template("index.html")
    

if __name__ == '__main__':
    app.run()
