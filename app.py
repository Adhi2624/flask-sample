from flask import Flask

app = Flask(__name__)

# Sample route for the homepage
@app.route('/')
def home():
    return "Welcome to the Flask API!"

if __name__ == '__main__':
    app.run(debug=True)
