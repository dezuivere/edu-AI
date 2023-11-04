import google.generativeai as palm
import re
import gradio as gr
from gtts import gTTS
from dotenv import load_dotenv
import os

load_dotenv() # to load the env variable from .env file

apiKey = os.getenv("API_KEY")

palm.configure(api_key=apiKey)

models = [m for m in palm.list_models(
) if 'generateText' in m.supported_generation_methods]
model = models[0].name   # It will select one of the model 


def genResp(text):
    completion = palm.generate_text(
        model=model,
        prompt=text,
        temperature=0,
        max_output_tokens=400  # The maximum length of the response
    )
    # Ensure the result is a string
    if isinstance(completion.result, str):
        return completion.result
    else:
        return str(completion.result)


infoQuestions = [
    "About {}: ",
    "PreRequisites of {}: ",
    "Requirements of {}: ",
    "Installations of {} programming language?",
    "Advantages of {}: ",
    "Applications of {}: ",
    "Concepts to learn {}: ",
    "Resources to learn {}: ",
    "no questions",
]


def chatWithAI(language, question):
    known_programming_languages = [
        "python", "java", "c++", "javascript", "ruby", "c",
        "c#", "php", "swift", "go", "rust",
        "typescript", "perl", "dart", "kotlin", "lua",
        "scala", "fortran", "cobol", "bash", "r",
        "matlab", "vba", "groovy", "haskell", "groovy",
        "elixir", "clojure", "objective-c", "pl/sql", "ada",
        "sql", "assembly", "lisp", "prolog", "pascal",
        "scheme", "tcl", "smalltalk", "forth", "vhdl",
        "verilog", "ada", "racket", "fortran", "erlang",
        "f#", "powershell", "cobol", "d", "rpg",
        "julia", "dart", "labview", "apex", "r"
        # additional languages can be added
    ]
    

    if language:
        language = language.lower()

        # Check if the input is in the list of known programming languages
        if language in known_programming_languages:
            # Generate response based on selected question
            res = re.sub(r"\n", "<br>", genResp(question.format(language)))
            response = f'<h2>{question.format(language)}</h2><p>{res}</p>'
            return response
        else:
            rs = re.sub(r"\n", "<br>", genResp(f"What is {language}?"))
            response = f'The provided input is not a known programming language.<br><h2>{language}</h2><p>{rs}</p>'
            return response
    else:
        return "Please enter the name of a programming language."



# this function will convert our text response into speech
def text_to_speech(text):
    newText = text
    stars = ['**', '*']
    for star in stars:
        newText = newText.replace(star, '')

    # Remove HTML tags from the text
    icons = ['<br>', '<h2>', '<p>', '</br>', '</h2>', '</p>', '**', '*']
    for icon in icons:
        text = text.replace(icon, '')

    # Convert text to speech
    tts = gTTS(text=text, lang='en', slow=False)

    # Save the speech audio into a file
    filename = "speech.mp3"
    # every time when user inputs the input the audio file is overwrittem
    tts.save(filename)

    return filename, newText


inputs = [gr.Textbox(lines=1, label="ProgrammerPal"), gr.Radio(
    infoQuestions, label="What Do You Want to Know?")]
outputs = [gr.Audio(
    type='filepath', label="speech"), gr.HTML(label="reply")]

# Create a Gradio interface
chatInterface = gr.Interface(
    fn=lambda x, y: text_to_speech(chatWithAI(x, y)),
    inputs=inputs,
    outputs=outputs,
    title="Chatbot for ",
    description="Enter the name of a programming language.",
    theme=gr.themes.Base(),
)

chatInterface.launch(share=True)
