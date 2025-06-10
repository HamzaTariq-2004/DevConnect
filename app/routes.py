from flask import jsonify

def register_routes(app):
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"message": "Welcome to DevConnect!"}), 200

    @app.route("/ping", methods=["GET"])
    def ping():
        return jsonify({"message": "pong"}), 200

