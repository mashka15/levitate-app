from waitress import serve
from wsgi import app
import logging

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    logging.info("Starting the server on http://0.0.0.0:5000")
    serve(app, host='0.0.0.0', port=5000)
