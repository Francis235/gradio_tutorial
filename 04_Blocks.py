import gradio as gr

with gr.Blocks() as demo:
    with gr.Tab(label="txt2img"):
        with gr.Row():
            with gr.Column(scale=15):
                txt1 = gr.Textbox(lines=2, label="")
                txt2 = gr.Textbox(lines=2, label="")
            with gr.Column(scale=1, min_width=1):
                button1 = gr.Button(value="1")
                button2 = gr.Button(value="2")
                button3 = gr.Button(value="3")
                button4 = gr.Button(value="4")
            with gr.Column(scale=6):
                generate_button = gr.Button("Generate", variant="primary", scale=1)
                with gr.Row():
                    drop_down1 = gr.Dropdown(["Option 1", "Option 2", "Option 3"], label="Style1")
                    drop_down2 = gr.Dropdown(["Option 1", "Option 2", "Option 3"], label="Style2")
        with gr.Row():
            with gr.Column():
                with gr.Row():
                    drop_down3 = gr.Dropdown(["Option 1", "Option 2", "Option 3"], label="Sampling method")
                    slider1 = gr.Slider(minimum=0, maximum=100, step=10, label="Sample steps")
                checkboxgroup = gr.CheckboxGroup(["Restore face", "Tiling", "Hires.fix"])
                with gr.Row():
                    slider2 = gr.Slider(minimum=0, maximum=100, step=10, label="Width")
                    slider3 = gr.Slider(minimum=0, maximum=100, step=10, label="Batch count")
                with gr.Row():
                    slider4 = gr.Slider(minimum=0, maximum=100, step=10, label="Height")
                    slider5 = gr.Slider(minimum=0, maximum=100, step=10, label="Batch size")
                slider6 = gr.Slider(minimum=0, maximum=100, step=10, label="CFG scale")
                with gr.Row():
                    number1 = gr.Number(label="Seed", scale=3  )
                    button5 = gr.Button(value="Randomize", min_width=1)
                    button6 = gr.Button(value="Reset", min_width=1)
                    checkbox1 = gr.Checkbox(label="Extra", min_width=10)
                drop_down4 = gr.Dropdown(["1", "2", "3"], label="Script")
            with gr.Column():
                gallery = gr.Gallery(
                    [
                        "http://www.marketingtool.online/en/face-generator/img/faces/avatar-1151ce9f4b2043de0d2e3b7826127998.jpg",
                        "http://www.marketingtool.online/en/face-generator/img/faces/avatar-116b5e92936b766b7fdfc242649337f7.jpg",
                        "http://www.marketingtool.online/en/face-generator/img/faces/avatar-1163530ca19b5cebe1b002b8ec67b6fc.jpg",
                        "http://www.marketingtool.online/en/face-generator/img/faces/avatar-1116395d6e6a6581eef8b8038f4c8e55.jpg",
                        "http://www.marketingtool.online/en/face-generator/img/faces/avatar-11319be65db395d0e8e6855d18ddcef0.jpg",
                    ], columns=3
                )
                with gr.Row():
                    button7 = gr.Button(value="📁", min_width=1)
                    button8 = gr.Button(value="Save", min_width=1)
                    button9 = gr.Button(value="Zip", min_width=1)
                    button10 = gr.Button(value="Send to img2img", min_width=1)
                    button11 = gr.Button(value="Send to inpaint", min_width=1)
                    button12 = gr.Button(value="Send to extras", min_width=1)
                text3 = gr.Textbox(lines=4, label="")
    with gr.Tab(label="img2img"):
        pass

demo.launch()