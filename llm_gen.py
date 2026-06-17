from langchain_groq import ChatGroq

# Directly provide your Groq API key here
GROQ_API_KEY = "<Paste your own API key>"

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)

def generate_post(prompt):
    response = llm.invoke(prompt)
    return response.content


'''# Example usage
if __name__ == "__main__":
    prompt = "Write a LinkedIn post about completing a Python certification."
    print(generate_post(prompt))'''
