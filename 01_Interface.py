import gradio as gr

def greet(name):
    return "Hello " + name + "!"

def turn_grey(image):
    import cv2
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return image

def  file_path(input, name):
    return input

# iface = gr.Interface(fn=greet, inputs="text", outputs="text")
# iface = gr.Interface(
#     fn=greet,
#     inputs=gr.Textbox(lines=5, placeholder="Name Here...", label="Name"),
#     outputs=gr.Textbox(lines=2, placeholder="Output Here...", label="Output"),
# )

# iface = gr.Interface(fn=turn_grey, inputs="image", outputs="image")
# iface = gr.Interface(
#     fn=turn_grey,
#     inputs=gr.Image(label="Input"),
#     outputs=gr.Image(label="Output"),
# )

iface = gr.Interface(fn=file_path, inputs=[gr.Audio(sources=["microphone"], type="filepath"), gr.Radio(choices=["A", "B"])], outputs="text")

iface.launch()