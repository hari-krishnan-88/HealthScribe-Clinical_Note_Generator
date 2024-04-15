from flask import Flask, render_template, request

# from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from transformers import pipeline

app = Flask(__name__)

summarizer = pipeline("text2text-generation", model="har1/HealthScribe-Clinical_Note_Generator")
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/clinical-note', methods=["POST"])
def summarize():
    if request.method == "POST":
        inputtext = request.form["inputtext_"]
        clinical_note = summarizer(inputtext, min_length=30, max_length=300)[0]["generated_text"]
        capitalized_lines = []
        for line in clinical_note.split("\r\n"):
            if line:
                capitalized_line = " ".join(word.capitalize() if word != "N/A" else word for word in line.split())
                capitalized_lines.append(capitalized_line)
            else:
                capitalized_lines.append("")
        capitalized_clinical_note = "\r\n".join(capitalized_lines)   
        clinical_note = capitalized_clinical_note
        print(clinical_note)
        clinical_note = clinical_note.replace('\r\n', '<br>')
        return render_template("output.html", data={"clinical_note": clinical_note})

if __name__ == '__main__': # It Allows You to Execute Code When the File Runs as a Script
    app.run()

