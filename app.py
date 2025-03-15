from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Google Translate API Key (Replace with your actual key)
API_KEY = "YOUR_GOOGLE_API_KEY"
TRANSLATE_URL = "https://translation.googleapis.com/language/translate/v2"

def translate_text(text, target_lang):
    """Function to translate text using Google Translate API"""
    params = {
        "q": text,
        "target": target_lang,
        "format": "text",
        "key": API_KEY
    }
    response = requests.post(TRANSLATE_URL, data=params)
    result = response.json()
    return result["data"]["translations"][0]["translatedText"]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]
        target_lang = request.form["language"]
        translated_text = translate_text(text, target_lang)
        return jsonify({"translated_text": translated_text})
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
