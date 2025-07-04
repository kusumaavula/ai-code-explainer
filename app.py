from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure your Gemini API key
genai.configure(api_key="AIzaSyDll0vUxCaUExE7t3YY7iuhxqPeiIQfbUI")

# Initialize the Gemini Flash model
model = genai.GenerativeModel(model_name='models/gemini-1.5-flash')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/explain', methods=['POST'])
def explain():
    data = request.get_json()
    user_code = data.get('code')

    if not user_code:
        return jsonify({'error': 'No code provided'}), 400

    try:
        response = model.generate_content(f"Explain the following code:\n{user_code}")
        explanation = response.text
        return jsonify({'explanation': explanation})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
