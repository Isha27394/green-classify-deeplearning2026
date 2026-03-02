import sys
import os

# Add the flask directory to the path
flask_dir = os.path.join(os.path.dirname(__file__), '..', 'flask')
sys.path.insert(0, flask_dir)

# Change working directory to flask folder for relative paths
os.chdir(flask_dir)

# Import the Flask app
from app import app as application

# Export for Vercel
app = application
