from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/call-api2', methods=['GET'])
def call_api2():
    print("API1: Received request from User")

    try:
        response = requests.get("http://api2:5001/hello")
        print("API1: Got response from API2 →", response.text)
        return jsonify({
            "from": "API1",
            "api2_response": response.json()
        })
    except Exception as e:
        print("API1: Error contacting API2 →", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
