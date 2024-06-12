# HealthScribe ( a Clinical Note Generator using Generative AI )

 A web application that allows users to generate clinical notes from transcribed ASR(Automatic Speech Recognition) data of conversations between doctors and patients using fine-tuned BART model [(har1/HealthScribe-Clinical_Note_Generator)](https://huggingface.co/har1/HealthScribe-Clinical_Note_Generator)

## Features

- User-friendly web interface for inputting conversational data obtained through ASR
- Tokenization of input text for processing by the BART model
- Fine-tuned BART model for generating clinical notes from medical conversations
- Presentation of the generated clinical note on the web interface

  
## Project Structure
- `dataset/` : Contains modified MTS-Dialog dataset
- `model notebook/` : Contains 2 .ipynb notebooks (CliNo__version1 : used to fine-tune BART , CliNo__Pipe : Used to test the fine-tuned model metrics in comparision to base BART)
- `venv/` : Virtual Environment
- `test.txt` : Contains test-case conversations
- `templates/` : Contains HTML templates for the web interface.
- `.gitignore` : Specifies files to be ignored by Git.
- `app.py` : Main application file for running the web interface.
- `requirements.txt` : Lists dependencies required for the project.

## Tech Stack

- **Programming Language**: Python
- **Web Framework**: Flask
- **Deep Learning Libraries**: Transformers (HuggingFace)
- **Original Dataset** : [MTS-Dialog](https://github.com/abachaa/MTS-Dialog)
- **Modified Dataset** : [har1/MTS_Dialogue-Clinical_Note](https://huggingface.co/datasets/har1/MTS_Dialogue-Clinical_Note)
- **Base Model**: [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn)
- **Fine-Tuned Model**: [har1/HealthScribe-Clinical_Note_Generator](https://huggingface.co/har1/HealthScribe-Clinical_Note_Generator)
- **Frontend**: HTML, CSS
- **Platform**: Google Colab
- **Version Control**: Git

### Installation

A step by step guide that will tell you how to get the development environment up and running.

First Clone the repo
```
$ git clone https://github.com/hari-krishnan-88/HealthScribe-Clinical_Note_Generator.git
```
Change directory to the repo directory
```
$ cd HealthScribe-Clinical_Note_Generator
```
Activate the Virtual Environment venv
```
$ activate
```
Run the Flask App app.py
```
$ flask --app app --debug run
```
Click on the URL (http://127.0.0.1:5000) to open the web interface on your browser
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 127-629-777
```
## Usage

![1](https://github.com/hari-krishnan-88/HealthScribe-Clinical_Note_Generator/assets/76527692/7ad1546f-f431-4957-af6b-0414d7ba12d5)
-

This is how the initial web-interface looks like. A user can input the doctor-patient conversation in the text box and click on submit.

![2](https://github.com/hari-krishnan-88/HealthScribe-Clinical_Note_Generator/assets/76527692/e34d6eba-6d38-4393-b690-02f7040e7159)
-

After Clicking the submit button the interface tokenizes the data and sends it to the HuggingFace Model and the output is processed.



![3](https://github.com/hari-krishnan-88/HealthScribe-Clinical_Note_Generator/assets/76527692/bb6f289a-749e-4b96-a64b-35c543c3abc3)
-
Final Output is the Clinical note which is derived from the conversation and parameterised on the basis of : 
- Symptoms :
- Diagnosis :
- History of Patient :
- Plan of Action :

## Contributers
- [Aleena Patani](https://github.com/Aleenapatani03)
- [Amigashabnam F](https://github.com/AMI-BYTE6)
- [Harikrishnan KC](https://github.com/hari-krishnan-88)
- [Sujith J](https://github.com/sujithjayaprakash)

