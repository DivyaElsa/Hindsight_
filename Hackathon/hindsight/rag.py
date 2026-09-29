import os
from groq import Groq
from hindsight.memory import retrieve_context
from dotenv import load_dotenv

load_dotenv()

# Ensure GROQ_API_KEY is set in the environment
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def ask_hindsight(query: str) -> str:
    """
    Uses the RAG loop to generate an answer based on past memory and the current query.
    """
    # 1. Retrieve relevant past context
    context = retrieve_context(query)
    
    # 2. Construct the system prompt with injected memory
    system_prompt = (
        "You are 'Hindsight', an advanced coding assistant with long-term memory. "
        "Use the provided past interactions and user preferences to inform your answers. "
        "If the past context is relevant, apply those preferences or lessons learned to the current task. "
        "Keep your answers concise, accurate, and focused on code.\n\n"
    )
    
    if context:
        system_prompt += f"### Past Context & Memory ###\n{context}\n#############################\n"
        
    # 3. Call the LLM
    try:
        response = client.chat.completions.create(
            model="qwen/qwen3.8-27b", # Extracted from the API's available models list
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error connecting to LLM: {str(e)}\n\nMake sure your GROQ_API_KEY is set in the .env file."
