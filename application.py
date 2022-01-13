"""
Module Docstring
"""

__author__ = "David Alvarez Calvo david@devidd.com"
__version__ = "0.1.0"
__license__ = "MIT"

import os

import lotoes as application

env = os.getenv('FLASK_CONFIG')
#if env is None or env not in ["test", "prod"]:
env = "dev"

app = application.create_app(env)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6032, debug=True)