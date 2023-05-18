import os


def serve_dev():
    os.system(
        "FLASK_APP=src.api:app FLASK_DEBUG=1 poetry run flask run --port=8080"
    )