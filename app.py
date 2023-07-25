"""
This script runs the application in http://localhost:80
"""

import bottle
# routes contains the HTTP handlers for our server and must be imported.
import routes

if __name__ == '__main__':

    @bottle.route('/static/<filepath:path>')
    def server_static(filepath):
        """Handler for static files."""
        return bottle.static_file(filepath, root='static')

    # Starts a local test server.
    bottle.run(host='0.0.0.0', port='80', reloader=True)
