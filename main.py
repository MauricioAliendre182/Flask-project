from flask import Flask, request, make_response, redirect

# Create a new instance of Flask
app = Flask(__name__)


# Create the first Route
@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie("user_ip", user_ip)
    return response


@app.route('/hello')
def hello():
    # Ip of the user
    user_ip = request.cookies.get('user_ip')
    return {"Name": "Mauricio Aliendre",
            "Age": 25,
            "IP": user_ip}

if __name__ == "__main__":
    app.run(port=5500, debug=True)