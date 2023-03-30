from flask import Flask, render_template, request
import fitz

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['fileInput']
        if file:
            # read the PDF file
            pdf = fitz.open(stream=file.read(), filetype="pdf")
            text = ""
            for page in pdf:
                text += page.get_text()

            # extract name, skills and experience
            # here you can write your code to extract name, skills and experience from the text
            # and store it in variables `name`, `skills` and `experience`
            # for demonstration purposes, I'm just returning the entire text as the name
            name = text.strip()
            skills = "Python, Flask, HTML, CSS"
            experience = "2 years of experience in web development"

            return render_template('index.html', name=name, skills=skills, experience=experience)

if __name__ == '__main__':
    app.run(debug=True)
