# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Hello, world!"


# if __name__ == "__main__":
#     app.run()

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

def main():
    return "Hello, Python!"  # Return something that matches the test assertion

if __name__ == "__main__":
    app.run()
