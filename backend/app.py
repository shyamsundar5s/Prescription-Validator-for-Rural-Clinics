from flask import Flask, request, jsonify
from ocr.ocr_processor import process_prescription_image
from models.prescription_validation import validate_prescription

app = Flask(__name__)

@app.route('/validate', methods=['POST'])
def validate():
    data = request.json
    prescription_text = data.get("prescription_text", "")
    symptoms = data.get("symptoms", [])
    validation_result = validate_prescription(prescription_text, symptoms)
    return jsonify(validation_result)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    prescription_text = process_prescription_image(file)
    return jsonify({"text": prescription_text})

if __name__ == '__main__':
    app.run(debug=True)
