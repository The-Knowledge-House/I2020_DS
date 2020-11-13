from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/calculator/')
@app.route('/calculator/<int:value>')
def calculate(value=10):
    return render_template("calculator.html", val=value)

@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == 'POST':
        req = request
        return render_template("form.html", req=req)
    else:
        req = request
        return render_template("form.html", req=req)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", error = e)

if __name__ == '__main__':
    app.run(debug=True)
