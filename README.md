
# EduAI

EduAI is a Python chatbot that aids in learning programming languages, providing extensive resources and information. Its unique text-to-speech feature enhances accessibility for all users. Additionally, EduAI has an interactive feature where users can select a question and receive an immediate answer in the form of text as well as speech, making it a comprehensive learning tool. EduAI is not just a chatbot, but a step towards universal accessibility of programming knowledge.




## Features

- Provides information on a wide range of programming languages.
- Offers intelligent, language-specific responses, enabling users to get precise information tailored to their chosen language.
-  Features an easy-to-use input interface and organized HTML responses for a seamless user experience.
- Easily expandable to support additional languages.
- Encourages collaboration and customization for further development.
- Incorporates a text-to-speech feature, enhancing accessibility for visually impaired or differently-abled individuals.
- Includes an interactive feature that allows users to select a question and receive an immediate, accurate answer.


## Installation

- Install Dependencies:

Make sure you have Python installed. This chatbot is written in Python.
Install Gradio if you haven't already. You can use pip for this:

```bash
 pip install gradio

```
Also u need to install the google.generativeai module and gtts(Google-text-to-speech) module :

   ```bash
 pip install google-generativeai


``` 
   ```bash
 pip install gtts


```

Ensure you have the necessary API key or authentication for the Google Generative AI API.

- Set Up API Key:

Replace 'YOUR_API_KEY' in the code with your actual Google Generative AI API key.

Run the Script:

Run the Python script with the chatbot code.

Interact with the Chatbot:

Once the script is running, open a web browser and navigate to the provided local address (e.g., http://127.0.0.1:7860/).

Enter a Programming Language and select a question:

Input the name of a programming language to interact with the chatbot and do select the question.

Explore Responses:

The chatbot will generate and display responses about the specified programming language and also an audio file which can be downloaded.



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY = your api key` 

## Usage/Examples
- Run the following command in your python shell or command prompt and then you are good to go!

```
python chat.py
```

Cool right?




