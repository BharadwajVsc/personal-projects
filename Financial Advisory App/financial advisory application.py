import warnings

warnings.filterwarnings("ignore")

import gradio as gr
import google.generativeai as genai

# Set the Google API key directly
GOOGLE_API_KEY = "AIzaSyA823QeHDKUmgKO50_ZDqIBofA8WKHSBO0"

if GOOGLE_API_KEY:
    print("Able to connect API Key")
    genai.configure(api_key=GOOGLE_API_KEY)
else:
    print("API Key not found.")

# Set up the Gemini model
generation_config = {
    "temperature": 0.3,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config=generation_config,
    safety_settings=safety_settings,
)


# Function to generate financial advice using Gemini
def generate_financial_advice(
    name,
    age,
    income,
    expenses,
    net_worth,
    goal,
    goal_amount,
    goal_timeline,
    risk_tolerance,
    investment_preferences,
):
    prompt = f"""
    Please provide personalized financial advice to a user with the following information:

    Name: {name}
    Age: {age}
    Income: ${income:.2f}
    Expenses: ${expenses:.2f}
    Net Worth: ${net_worth:.2f}

    Financial Goal: {goal}
    Target Amount: ${goal_amount:.2f}
    Timeline: {goal_timeline} years

    Risk Tolerance: {risk_tolerance}
    Investment Preferences: {investment_preferences}

    Please ensure the advice is actionable and provides clear recommendations.
    """

    response = model.generate_content(prompt)
    return response.text


# Create the Gradio interface
iface = gr.Interface(
    fn=generate_financial_advice,
    inputs=[
        gr.Textbox(label="Name"),
        gr.Number(label="Age"),
        gr.Number(label="Annual Income"),
        gr.Number(label="Monthly Expenses"),
        gr.Number(label="Net Worth"),
        gr.Textbox(label="Financial Goal"),
        gr.Number(label="Target Amount"),
        gr.Number(label="Timeline (Years)"),
        gr.Dropdown(label="Risk Tolerance", choices=["Low", "Medium", "High"]),
        gr.Textbox(label="Investment Preferences (Optional)"),
    ],
    outputs=gr.Textbox(label="Financial Advice"),
    title="Financial Advisory App",
    description="Get personalized financial advice from Gemini.",
)

# Launch the Gradio interface
iface.launch()
