from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#creating database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sohan.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



@app.route("/")
def hello_world():
    return render_template('index.html')
     #return "<p>Hello World!</p>"
@app.route("/products")
def products():
    return "<p>This is products!</p>"
if __name__ == "__main__":
    app.run(debug=True)
