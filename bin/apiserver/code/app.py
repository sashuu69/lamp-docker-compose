"""
 * File name : app.py
 * Author : Sashwat K <sashwat0001@gmail.com>
 * Last updated : 11 Jul 2021
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
filesLocation = "/tmp"


# Definition to return json output
def jsonOutputer(code, res):
    return jsonify({"errorCode": code, "result": res})


# Definition to run API
@app.route("/", methods=["GET"])
def apiTesting():
    return jsonOutputer(200, "Hello World")


# Definition to handle 404
@app.errorhandler(404)
def invalid_route(e):
    return jsonOutputer(404, "Page not found")


# Definition Main
def main():
    app.run(host="0.0.0.0")


if __name__ == "__main__":
    main()
