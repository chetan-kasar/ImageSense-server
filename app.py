import base64

from flask import Flask, render_template, request
import PIL.Image
from io import BytesIO
import google.generativeai as genai
genai.configure(api_key='AIzaSyAMjsZilyZXxmG3mVDmqb6Y4D30ZX-GwNs')

app = Flask(__name__)

@app.route("/generateText", methods = ["POST"])
def generateText():
    file = request.files["fileImage"]
    img = PIL.Image.open(BytesIO(file.read()))
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(img)

    file_content = file.read()
    file_content_base64 = base64.b64encode(file_content).decode('utf-8')

    return render_template("index.html", output=response.text, file_content_base64=file_content_base64)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

# model = genai.GenerativeModel('gemini-pro')
# response = model.generate_content("What is the meaning of life?")

#print(response.text)

# img = PIL.Image.open("H:/Gemini/building.webp")
# model = genai.GenerativeModel('gemini-pro-vision')
# response = model.generate_content(img)

