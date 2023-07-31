from flask import Flask

app = Flask(__name__)
from models import storage
from api.v1.views import app_views
app.register_blueprint(app_views)
def teardown_app_context(exception=None):
    """Method to close the database connection at the end of the request."""
    storage.close()
if __name__ == '__main__':
    # Set host and port based on environment variables or default values
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))

    # Run the app with threaded=True
    app.run(host=host, port=port, threaded=True)
