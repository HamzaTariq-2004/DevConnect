from flask import jsonify

def register_routes(app):
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"message": "Welcome to DevConnect!"}), 200

    @app.route("/ping", methods=["GET"])
    def ping():
        return jsonify({"message": "pong"}), 200
    @app.route("/contact", methods=["GET"])
    def contact():
    	return jsonify({"email": "support@devconnect.com"}), 200
    @app.route("/about", methods=["GET"])
    def about():
    	return jsonify({"app": "DevConnect", "purpose": "CI/CD Practice"}), 200
    @app.route("/version", methods=["GET"])
    def version():
    	return jsonify({"version": "1.0.0"}), 200
