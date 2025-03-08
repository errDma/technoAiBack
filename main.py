from flask import Flask, request
from get_films import get_films
import json
from flask import jsonify, request

# Создаем экземпляр Flask
app = Flask(__name__)

@app.route("/film/", methods=["GET"])
def read_film():
    description = request.args.get("description")
    if description is None:
        return jsonify({"error": "Missing 'description' parameter"}), 400
    
    try:
        result = get_films(description)
        print(result)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)