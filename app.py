# app.py

import gradio as gr
from weather import get_weather

ui = gr.Interface(
    fn=get_weather,
    inputs=gr.Textbox(label="Enter City Name"),
    outputs=gr.Markdown(label="Weather Info"),  # 🟢 Change this line
    title="🌍 Weather Info App",
    description="Enter the name of a city to get real-time weather information using OpenWeatherMap API.",
    theme="soft"
)

if __name__ == "__main__":
    ui.launch()
