from openai import AzureOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Variables
product_name = "Smart Fitness Watch"
target_audience = "Young professionals"

# Base directory (project root)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Function to load prompt templates
def load_prompt(file_name):
    prompt_path = os.path.join(BASE_DIR, "prompts", file_name)
    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()

# Prompt templates
prompts = {
    "professional": load_prompt("professional_prompt.txt"),
    "friendly": load_prompt("friendly_prompt.txt"),
    "bold": load_prompt("bold_prompt.txt")
}

# User selects tone
print("Available tones:", ", ".join(prompts.keys()))
tone = input("Select tone: ").lower()

if tone not in prompts:
    print("❌ Invalid tone selected")
    exit()

# Inject variables into prompt
prompt = prompts[tone].format(
    product_name=product_name,
    target_audience=target_audience
)

# Azure OpenAI API call
response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    messages=[
        {"role": "system", "content": "You are a marketing assistant."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7
)

# Output
print("\nTone Selected:", tone.capitalize())
print("Generated Slogan:")
print(response.choices[0].message.content)

