from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows React to talk to Flask

# Sample medicine interaction rules
interactions = {
    "Ibuprofen+Warfarin": "Risk of bleeding",
    "Paracetamol+Aspirin": "Generally safe"
}

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    meds = [m.strip() for m in data['meds'].split(',')]
    sugar = int(data['sugar'])
    cholesterol = int(data['cholesterol'])

    # Check medicine interaction
    med_key = '+'.join(sorted(meds))
    med_result = interactions.get(med_key, "No known interaction")

    # Check lab values
    sugar_result = "High" if sugar > 140 else "Normal"
    chol_result = "High" if cholesterol > 200 else "Normal"

    # Combine result
    message = f"Medicine: {med_result}, Sugar: {sugar_result}, Cholesterol: {chol_result}"
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)