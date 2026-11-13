
from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    'app_requests_total',
    'Total number of application requests',
    ['method', 'endpoint', 'status']
)

@app.before_request
def before_request():
    pass

@app.after_request
def after_request(response):
    if hasattr(request_context := __import__('flask').request, 'endpoint'):
        if request_context.endpoint != 'metrics':
            REQUEST_COUNT.labels(
                request_context.method,
                request_context.endpoint or 'unknown',
                str(response.status_code)
            ).inc()
    return response

@app.route('/')
def home():
    return "Self Healing DevOps Application Running!"

@app.route('/health')
def health():
    return jsonify(status="healthy")

@app.route('/info')
def info():
    return jsonify(application="DevOps Monitoring App")

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
