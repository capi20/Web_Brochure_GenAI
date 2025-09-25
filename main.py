import gradio as gr
from brochure_generator import stream_gpt

def stream_brochure(company_name, url):
    yield from stream_gpt(company_name, url)

# Gradio interface
view = gr.Interface(
    fn=stream_brochure,
    inputs=[
        gr.Textbox(label="Company name:"),
        gr.Textbox(label="Landing page URL including http:// or https://")
    ],
    outputs=[gr.Markdown(label="Brochure:")],
    flagging_mode="never"
)

if __name__ == "__main__":
    view.launch()
