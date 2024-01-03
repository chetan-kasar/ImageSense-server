from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import PIL.Image
from io import BytesIO
import google.generativeai as genai
genai.configure(api_key='AIzaSyAMjsZilyZXxmG3mVDmqb6Y4D30ZX-GwNs')

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ["POST"])
def home():
    if 'image' in request.files:
        image = request.files['image']
        img = PIL.Image.open(BytesIO(image.read()))
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content(img)
        data = {'message':response.text}
        return jsonify(data)

    else:
        return 'No image found in request!'

if __name__ == "__main__":
    app.run(debug=True)

# model = genai.GenerativeModel('gemini-pro')
# response = model.generate_content("What is the meaning of life?")

#print(response.text)

# img = PIL.Image.open("H:/Gemini/building.webp")
# model = genai.GenerativeModel('gemini-pro-vision')
# response = model.generate_content(img)

