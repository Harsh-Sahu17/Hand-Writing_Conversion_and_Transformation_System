from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('http://127.0.0.1:5500/index.html/process_data', methods=['POST'])
def process_data():
    data = request.json  # Assuming JSON data is sent from frontend
    # Perform necessary operations with data
    result = {'output': 'Processed data'}  # Placeholder response
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
