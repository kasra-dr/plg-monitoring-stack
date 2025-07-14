from flask import Flask, request, make_response
from prometheus_flask_exporter import PrometheusMetrics
import time
import random

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Static information as metric
metrics.info('app_info', 'A simple Flask application for monitoring demo')

@app.route('/')
def main():
    return "Welcome to the Monitoring Demo App!"

@app.route('/slow'):
    def slow_response():
        delay = random.uniform(0.5, 1.5)
        time.sleep(delay)
        return f"This was a slow response, took {delay:.2f} seconds."

@app.route('/error')
def error_route():
    return "This is an error.", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

