from dotenv import load_dotenv
import google.generativeai as genai
import random

# Configure the Gemini Pro API
genai.configure(api_key="AIzaSyA823QeHDKUmgKO50_ZDqIBofA8WKHSBO0")

# Initialize the Gemini Pro model
model = genai.GenerativeModel("gemini-2.5-flash")
3
# Define categories
categories = ["Technical Skills", "Soft Skills", "Experience"]


def generate_questions(category, num_questions):
    prompt = f"Generate {num_questions} interview questions for the category '{category}' in a job interview."
    response = model.generate_content(prompt)
    questions = response.text.split("\n")
    return [q.strip() for q in questions if q.strip()]


def display_questions(category, num_questions):
    questions = generate_questions(category, num_questions)
    print(f"\nSelected questions for category '{category}':")
    for i, question in enumerate(questions, 1):
        print(f"{i}. {question}")


# Main interaction loop
while True:
    print("\nJob Description Dashboard")
    print("Categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    category_choice = int(input("Select a category (1-3) or 0 to exit: "))
    if category_choice == 0:
        break
    elif 1 <= category_choice <= len(categories):
        selected_category = categories[category_choice - 1]
        num_questions = int(input("How many questions would you like to display? "))
        display_questions(selected_category, num_questions)
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Job Description Dashboard!")
