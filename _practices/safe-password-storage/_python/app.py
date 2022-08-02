import time
from flask import Flask, request

app = Flask(__name__)

SECRET_TOKEN = 'foobar'


def strcmp(s1, s2):
    if len(s1) != len(s2):
        return False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            return False
        time.sleep(0.01)
    return True


@app.route("/")
def protected():
    if token := request.headers.get('X-TOKEN'):
        return (
            "Hello admin user! Here is your secret content"
            if strcmp(token, SECRET_TOKEN)
            else ("WHO ARE YOU? GET OUT!", 403)
        )

    else:
        return "Missing token", 401


if __name__ == "__main__":
    app.run()
