#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views

@app.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized_endpoint():
    """Endpoint to raise a 401 error using abort

    This endpoint will raise a 401 error, and the error handler for 401
    in app.py will handle it.

    Returns:
        Response: A JSON response indicating unauthorized access.
    """
    abort(401)


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)
