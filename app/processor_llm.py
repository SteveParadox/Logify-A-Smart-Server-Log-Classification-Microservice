from dotenv import load_dotenv
from groq import Groq

# Load environment variables (e.g., API key)
load_dotenv()

# Initialize the Groq client
groq = Groq()

def classify_with_llm(log_msg):
    """
    Classifies a log message using a Groq-hosted LLaMA 3.3 70B model.

    Parameters:
        log_msg (str): The log message to classify.

    Returns:
        str: Category name or 'Unclassified'
    """
    prompt = f"""
    Classify the log message into one of these categories:
    (1) Workflow Error, (2) Depreciation Warning.
    If you can't figure out a category, return 'Unclassified'.
    Only return the category name. No preamble.

    Log message: {log_msg}
    """

    chat_completion = groq.chat.completions.create(
        model="llama3-70b-8192",  # Correct model slug for Groq
        messages=[
            {
                "role": "user",
                "content": prompt.strip(),
            }
        ]
    )

    return chat_completion.choices[0].message.content.strip()
