from flask import Flask, request, json
app = Flask(__name__)


@app.route('/')
def index():
    return "Send POST request to: /process"


@app.route('/process', methods=["POST"])
def process():
    try:
        _time = request.json.get("time")
        _image = request.json.get("image")
        _speed = request.json.get("speed")
        _speed_unit = request.json.get("speed_unit")

        data = {
            "time": _time,
            "image": _image,
            "speed": _speed,
            "speed_unit": _speed_unit
        }

    except:
        print("Invalid arguments")
        data = None

    return json.jsonify(data)


if __name__ == "__main__":
    app.run(port=8008, debug=True)
