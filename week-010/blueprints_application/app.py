from flask import Flask, render_template
from admin.admin import admin_app

app = Flask(__name__)
app.register_blueprint(admin_app)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, port=5050)