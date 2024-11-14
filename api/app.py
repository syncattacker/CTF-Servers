from flask import Flask, request, jsonify, redirect
from dotenv import load_dotenv
import os
app = Flask(__name__)
load_dotenv()
API_KEY = "b3f9e5d7c8a64ad1a54f7f60d8f0b72d"
@app.route('/')
def root():
    return redirect('/data', code = 302)

@app.route('/data', methods=['GET'])
def getData():
    apiKey = request.headers.get('Authorization')
    if apiKey != f"Beaere {os.getenv('REAL_API_KEY')}":
        return jsonify({
            "error" : "Unauthorized! Missing Authorization Header and API Key.",
            "message" : "Hey Red Team, this will get harder! We're currently investing in our dev team to make things trickier. Search a bit more rigourously, and maybe you will find. Good Luck!",
            "owner" : "BLUE TEAM",
            "notes" : "This Project is deployed on GitHub"
        })
    return jsonify({
        "flag": "BLU3-TE4W{AP1_K3Y_Y0U_R3ALLY_N33D_1T}",
        "message": "Welcome to Protected Area",
        "owner": "BLUE TEAM",
        "success": "Access Granted"
    })

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080, debug = True)