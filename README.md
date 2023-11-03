
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




## License

[MIT](https://choosealicense.com/licenses/mit/)


Copyright (c) [2023] [Shwetha K S]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Screenshots

![chatWithAI](https://www.dropbox.com/scl/fi/qg1zhkb7m8bk5uchtr2fd/chatWithAI.jpeg?rlkey=to77bae42l42m35dplcieg0z9&dl=0)

## Usage/Examples
- Run the following command in your python shell or command prompt and then you are good to go!

```
python chat.py
```

Cool right?




