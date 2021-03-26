from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "The server number 2 is on."


@app.route("/info", methods=["GET"])
def information():
    output = "This server will allow the user to request blood analyseas."
    return output


@app.route("/HDL", methods=["POST"])
def HDL_request():
    """
        input info: {"HDL": 60}
    """
    in_data = request.get_json()
    print(in_data)
    HDL = in_data["HDL"]
    result = analyse_HDL(HDL)
    answer = {"HDL": HDL, "Analysis": result}
    if answer != "Normal":
        return "Bad HDL", 400
#    return "The result for a blood level of {} is {}".format(HDL,result)
    return jsonify(answer)

@app.route("/say_hello/<person>")
@app.route("/say_hello/<person>/<age>", methods=["GET"])
def say_hello_function(person):
    next_year = int(age) + 1
    output = "Hello there, {}! You will be {} old next year".format(person, next_year)
    return output


if __name__ == "__main__":
    app.run()
