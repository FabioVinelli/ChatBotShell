from flask import Flask, request, jsonify
import os
from onboard_agent import OnboardingAgent
from compliance_agent import ComplianceAgent

app = Flask(__name__)

# Initialize agents
onboarding_agent = OnboardingAgent()
compliance_agent = ComplianceAgent()

@app.route('/onboarding', methods=['POST'])
def onboarding():
    data = request.json
    user_input = data['input']
    response = onboarding_agent.process(user_input)
    return jsonify(response)

@app.route('/compliance', methods=['POST'])
def compliance():
    data = request.json
    query = data['query']
    response = compliance_agent.analyze(query)
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
