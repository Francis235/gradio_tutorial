import gradio as gr

input_list = [
    gr.Audio(sources=["microphone", "upload"], type="numpy", label="Audio File"),
    gr.Checkbox(label="Checkbox"),
    gr.ColorPicker(label="Color Picker"),
    gr.Dataframe(headers=["Header 1", "Header 2"], label="Dataframe"),
    gr.Dropdown(choices=["Choice 1", "Choice 2", "Choice 3"], label="Dropdown"),
    gr.File(label="File", type="filepath"),
    gr.Image(sources=["webcam", "upload"], label="Image"),
    gr.Number(label="Number"),
    gr.Radio(choices=["Choice 1", "Choice 2", "Choice 3"], label="Radio"),
    gr.Slider(minimum=0, maximum=10, label="Slider", step=1),
    gr.Textbox(lines=3, max_lines=7, placeholder="Text here...", label="Textbox"),
    gr.TextArea(lines=3, max_lines=7, placeholder="Text here...", label="Textarea"),
    gr.Video(sources=["webcam", "upload"], label="Video"),
    # gr.CheckboxGroup(choices=["Choice 1", "Choice 2", "Choice 3"], label="Checkbox Group"),
]

output_list = [
    gr.Textbox(label="Audio outputs", lines=7),
    gr.Textbox(label="Checkbox outputs"),
    gr.Textbox(label="Color Picker outputs"),
    gr.Textbox(label="Dataframe outputs"),
    gr.Textbox(label="Dropdown outputs"),
    gr.Textbox(label="File outputs"),
    gr.Textbox(label="Image outputs"),
    gr.Textbox(label="Number outputs"),
    gr.Textbox(label="Radio outputs"),
    gr.Textbox(label="Slider outputs"),
    gr.Textbox(label="Textbox outputs"),
    gr.Textbox(label="TextArea outputs"),
    gr.Textbox(label="Video outputs"),
    # gr.Textbox(label="Checkbox Group outputs"),
]

def input_and_output(*input_data):
    return input_data

iface = gr.Interface(
    fn=input_and_output,
    inputs=input_list,
    outputs=output_list,
    title = "Input and Output Components",
    description="This is a demo of input and output components.", 
    live=True,
)

iface.launch()