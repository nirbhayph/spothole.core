from flask import Flask, request
from json import dumps, loads
from flask_cors import CORS
from spothole_service import pothole_results

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/getResults', methods=['GET'])
def app_get_unit_tests():
    return pothole_results()

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
