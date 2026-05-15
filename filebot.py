from google import genai
import os


client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
uploaded_file = None

# Check if the user has uploaded a file
if uploaded_file is None:
    path = input("Upload a document to get started. \nEnter the filepath: ")
    uploaded_file = client.files.upload(file=path)

# Loop for the chatbot
while True:
    prompt = input("Ask about the document, or type 'quit' ")
    if prompt.lower() == "quit":
        break
        
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[prompt, uploaded_file],
    )
    print(f"Filebot: \n {response}")
