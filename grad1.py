import gradio as gr

def greeting(name, intensity):
    return "Hello, " + name + " welcome to Gradio!" * int(intensity)



demo = gr.Interface(
    fn= greeting,
    inputs=["text", "slider"],
    outputs=["text"]
)

demo.launch()