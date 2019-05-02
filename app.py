import time
from flask import Flask
from flask import send_file
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.get('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

def update_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return "Hit count: {}.\n".format(count)

@app.route('/images/transparent.png')
def image():
    count = update_hit_count()
    print("Hit count: {}.\n".format(count))
    try:
        return send_file('./transparent.png', attachment_filename='transparent.png')
    except Exception as flask_exception:
        print(str(flask_exception))
        return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
