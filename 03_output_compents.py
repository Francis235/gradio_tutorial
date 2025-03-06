import gradio as gr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
# Audio/音频组件
# def audio_fn(audio):
#     hz = audio[0]
#     data = audio[1]
#     return hz, data
# demo = gr.Interface(fn=audio_fn, inputs=gr.Audio(type="numpy"), outputs="audio")

# "filepath"
# def audio_fn(audio):
#     return audio
# demo = gr.Interface(fn=audio_fn, inputs=gr.Audio(type="filepath"), outputs="audio")

# # Bar/柱状图组件
# simple = pd.DataFrame({
#     "a": [1, 2, 3],
#     "b": [4, 5, 6]    
# })
# demo = gr.Interface(fn=None, inputs=None, outputs=gr.BarPlot(simple, x="a", y="b"))

# # Gallery/画廊组件
# def process():
#     image_list = [
#         "http://www.marketingtool.online/en/face-generator/img/faces/avatar-1151ce9f4b2043de0d2e3b7826127998.jpg",
#         "http://www.marketingtool.online/en/face-generator/img/faces/avatar-116b5e92936b766b7fdfc242649337f7.jpg",
#         "http://www.marketingtool.online/en/face-generator/img/faces/avatar-1163530ca19b5cebe1b002b8ec67b6fc.jpg",
#         "http://www.marketingtool.online/en/face-generator/img/faces/avatar-1116395d6e6a6581eef8b8038f4c8e55.jpg",
#         "http://www.marketingtool.online/en/face-generator/img/faces/avatar-11319be65db395d0e8e6855d18ddcef0.jpg",
#     ]
#     image_list = [(image, f"Image {i+1}") for i, image in enumerate(image_list)]
#     return image_list
# demo = gr.Interface(fn=process, inputs=None, outputs=gr.Gallery(columns=5))

# # Plot组件
# def fig_output():
#     Fs = 8000
#     f = 5
#     sample = 10
#     x = np.arange(sample) 
#     y = np.sin(2 * np.pi * f * x / Fs)
#     # plt.plot(x, y)
#     plt.bar(x, y)
#     return plt
# demo = gr.Interface(fn=fig_output, inputs=None, outputs=gr.Plot())
     
# #  Textbox组件
# def textbox_output():
#     return "Hello, Gradio!"
# demo = gr.Interface(fn=textbox_output, inputs=None, outputs=gr.Textbox())
 
# # Json组件
# json_sample = {
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York"
# }
# demo = gr.Interface(fn=None, inputs=None, outputs=gr.Json(json_sample))

# Html组件
demo = gr.Interface(fn=None, inputs=None, outputs=gr.HTML("""
<h1>Hello, Gradio!</h1>
<p>This is an HTML component.</p>
"""))
 
demo.launch()