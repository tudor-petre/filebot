<h1>FileBot</h1>

FileBot is a simple terminal chatbot that allows users to upload a file and ask questions about it using Google Gemini.

<h2>What FileBot does</h2>

* Asks user for their file's filepath
* Uploads the file to Google Gemini
* Lets you ask questions about the document
* Prints Gemini's response in the terminal

<h2>Requirements</h2>

- Python 3.12+
- A Google Gemini API key
- The `google-genai` package

<h2>Install</h2>

Install the required package:

```bash
pip install google-genai
```

<h2>Set up your API key</h2>

Before running the script, set your API key as an environment variable:

```bash
export GEMINI_API_KEY="your_api_key_here"
```

If you use zsh, you can add that line to your `~/.zshrc` file so it loads automatically

<h2>How to run</h2>

Run `filebot.py` in your terminal

Then:

1. Enter the path to the document you want to upload
2. Ask a question about the document
3. Type `quit` to exit
