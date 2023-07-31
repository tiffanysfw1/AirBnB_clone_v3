from flask import jsonify
from api.v1.views import app_views

# Define the /status route on the app_views Blueprint
@app_views.route('/status', methods=['GET'])
def status():
    # Return a JSON response with "status": "OK"
    return jsonify({"status": "OK"})
""

