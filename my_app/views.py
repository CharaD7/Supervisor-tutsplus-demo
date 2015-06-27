from my_app import app

@app.route('/')
def hello_world():
    return "Hello to the World of Flask!"
