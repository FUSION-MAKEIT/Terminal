# app.py

import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute():
    try:
        command = request.json.get('command')
        result = subprocess.check_output(command, shell=True, text=True)
        return jsonify({'output': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
