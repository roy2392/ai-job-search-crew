from flask import Flask, request, jsonify
from flask_cors import CORS
from agents import JobApplicationSystem

app = Flask(__name__)
CORS(app)

system = JobApplicationSystem("John Doe", "john@example.com")

@app.route('/search_jobs', methods=['POST'])
def search_jobs():
    criteria = request.json.get('criteria')
    result = system.search_jobs(criteria)
    return jsonify(result)

@app.route('/apply_to_job', methods=['POST'])
def apply_to_job():
    data = request.json
    result = system.apply_to_job(data['company'], data['position'])
    return jsonify({"message": result})

@app.route('/update_application_status', methods=['POST'])
def update_application_status():
    result = system.update_application_status()
    return jsonify({"message": result})

@app.route('/analyze_performance', methods=['POST'])
def analyze_performance():
    data = request.json
    result = system.analyze_performance(data['company'], data['feedback'])
    return jsonify({"message": result})

@app.route('/generate_report', methods=['GET'])
def generate_report():
    result = system.generate_report()
    return jsonify({"report": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)