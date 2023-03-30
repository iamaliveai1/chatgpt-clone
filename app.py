import gradio as gr
import openai

from ailive.engine.chatgpt.chatgpt_api import ask_gpt

# if you have OpenAI API key as an environment variable, enable the below
# openai.api_key = os.getenv("OPENAI_API_KEY")

# if you have OpenAI API key as a string, enable the below
openai.api_key = "xxxxxx"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "



def openai_create(prompt):
    return ask_gpt(prompt, delete_conversation=True)


def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


def main():
    prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "
    block = gr.Blocks()

    with block:
        gr.Markdown("""<h1><center>Build Yo'own ChatGPT with OpenAI API & Gradio</center></h1>
        """)
        chatbot = gr.Chatbot()
        message = gr.Textbox(placeholder=prompt)
        state = gr.State()
        submit = gr.Button("SEND")
        submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

    block.launch(debug=True)


if __name__ == "__main__":
    main()
