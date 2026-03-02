import sys
import os

# Add the flask directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'flask'))

from app import app

# Vercel expects the Flask app to be named 'app'
# This file serves as the entrypoint for Vercel
