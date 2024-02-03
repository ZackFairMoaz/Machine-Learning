import gradio as gr
import numpy as np
import pandas as pd
import pickle
import model

def run_inference(age, sex, cpt, rbp, chol, fbs, rer, mhra, eia, oldpeak, slope_ST, nmv, thal):
    df = pd.read_csv('heart.csv')
    X = df.drop('target', axis=1)
    scaler = pickle.load(open('scaler.pkl', 'rb'))  # Assuming you saved the scaler during training
    input_data = scaler.transform([[age, sex, cpt, rbp, chol, fbs, rer, mhra, eia, oldpeak, slope_ST, nmv, thal]])
    loaded_model = pickle.load(open('Regression_Model.sav', 'rb'))
    prediction = loaded_model.predict(input_data)
    return prediction[0]

demo = gr.Interface(
     fn = run_inference,
     inputs = [
        gr.Slider(label = "Age", value=0, minimum=0, maximum=100, step=1),
        gr.Slider(label = "Sex", info="0: Female, 1: Male", value=0, minimum=0, maximum=1, step=1),
        gr.Slider(label = "cpt", info="Chest Pain Type", value=0, minimum=0, maximum=3, step=1),
        gr.Slider(label = "rbp", info="Resting Blood Pressure", value=0, minimum=80, maximum=200, step=1),
        gr.Slider(label = "chol", info="Cholesterol mg/dl", value=0, minimum=100, maximum=600, step=1),
        gr.Slider(label = "fbs", info="Fasting Blood Sugar", value=0, minimum=0, maximum=1, step=1),
        gr.Slider(label = "rer", info="Resting Electrocardiographic Results", value=0, minimum=0, maximum=2, step=1),
        gr.Slider(label = "mhra", info="Maximum Heart Rate Achieved", value=0, minimum=70, maximum=220, step=1),
        gr.Slider(label = "eia", info="Exercise Induced Angina (0-1)", value=0, minimum=0, maximum=1, step=1),
        gr.Slider(label = "oldpeak", info="ST depression induced by exercise relative to rest", value=0.0, minimum=1.6, maximum=6.2, step=0.1),
        gr.Slider(label = "slope_ST", info="The slope of the peak exercise ST segment", value=0, minimum=0, maximum=2, step=1),
        gr.Slider(label = "nmv", info="Number of major vessels colored by flourosopy", value=0, minimum=0, maximum=3, step=1),
        gr.Slider(label = "thal", info="thal: (0 = normal; 1 = fixed defect; 2 = reversable defect)", value=0, minimum=0, maximum=2, step=1),
    ],
    outputs=[gr.Textbox(label="Prediction", lines=1, scale=3)],
)

if __name__ == "__main__":
    model.train()
    demo.launch(share=True, server_name='0.0.0.0')