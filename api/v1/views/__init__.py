from flask import Blueprint

# Create the app_views Blueprint instance with URL prefix '/api/v1'
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Perform wildcard import from api.v1.views.index
from api.v1.views.index import *
