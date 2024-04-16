from flask import Flask
# Create a Flask app instance
app = Flask (__name__)
# Define a route
@app.route("/")
def hello ():
        return "<p style="text-align:center"> Hello, Welcome to flask web app! <p>"
# Run the app if executed directly
if __name__ == '__main__':
        app.run (host = '0.0.0.0')
