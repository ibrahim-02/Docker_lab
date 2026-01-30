from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__, static_folder='statics')

# Load the trained model from Lab 01
model = joblib.load('breast_cancer_gb_model.pkl')

# Class labels for Breast Cancer dataset
class_labels = ['Malignant', 'Benign']

# Feature names for the 30 features in breast cancer dataset
feature_names = [
    'mean_radius', 'mean_texture', 'mean_perimeter', 'mean_area', 'mean_smoothness',
    'mean_compactness', 'mean_concavity', 'mean_concave_points', 'mean_symmetry', 'mean_fractal_dimension',
    'se_radius', 'se_texture', 'se_perimeter', 'se_area', 'se_smoothness',
    'se_compactness', 'se_concavity', 'se_concave_points', 'se_symmetry', 'se_fractal_dimension',
    'worst_radius', 'worst_texture', 'worst_perimeter', 'worst_area', 'worst_smoothness',
    'worst_compactness', 'worst_concavity', 'worst_concave_points', 'worst_symmetry', 'worst_fractal_dimension'
]

@app.route('/')
def home():
    return "Welcome to the Breast Cancer Classifier API!"

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.form
            
            # Extract all 30 features from form
            features = []
            for feature in feature_names:
                features.append(float(data[feature]))
            
            # Prepare input data
            input_data = np.array([features])
            
            # Perform the prediction
            prediction = model.predict(input_data)
            prediction_proba = model.predict_proba(input_data)
            
            predicted_class = class_labels[prediction[0]]
            confidence = float(np.max(prediction_proba) * 100)
            
            # Return the predicted class in the response
            return jsonify({
                "predicted_class": predicted_class,
                "confidence": round(confidence, 2)
            })
        
        except Exception as e:
            return jsonify({"error": str(e)})
    
    elif request.method == 'GET':
        return render_template('predict.html')
    
    else:
        return "Unsupported HTTP method"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)


