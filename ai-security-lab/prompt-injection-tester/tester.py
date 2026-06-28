import os 
from google import genai
from config import API_KEY, MODEL_NAME
from datetime import datetime

def create_client():

    return genai.Client(api_key=API_KEY)

def send_prompt(client, prompt):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    try:
        return response.text
    except Exception as e:
        return f"ERROR OCCURED: {e}"

def load_prompts(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    prompts = []

    for line in lines:
        line = line.strip()

        if line:
            prompts.append(line)

    return prompts

def save_log(category, prompt, response):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    filename = f"logs/{category}.txt"

    with open(filename, "w") as file:
        file.write("=" * 60 + "\n")
        file.write(f"Timestamp: {timestamp}\n")
        file.write(f"Category: {category}\n")
        file.write(f"Prompt: {prompt}\n\n")
        file.write(f"Response:\n{response}\n")
        file.write("=" * 60 + "\n\n")

def run_category(client, category, filename):
    prompts = load_prompts(filename)

    for prompt in prompts:
        print(f"Testing: {prompt}")

        response = send_prompt(client, prompt)

        print(f"Response: {response}\n")

        save_log(category, prompt, response)


def main():
    client = create_client()
    
    categories = [
        ("instruction_override", "attacks/instruction_override.txt"),
        ("role_manipulation", "attacks/role_manipulation.txt"),
        ("context_manipulation", "attacks/context_manipulation.txt"),
        ("delimiter_attacks", "attacks/delimiter_attacks.txt") 
    ]
    
    for category, filename in categories:
        run_category(client, category, filename)

if __name__ == "__main__":
    main()

