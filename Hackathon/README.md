# Hindsight Coding Assistant

A CLI tool for a hackathon that acts as a coding assistant with long-term memory (RAG).
It stores your past prompts, responses, and coding preferences in a local vector database (ChromaDB) to provide personalized, context-aware coding help.

## Setup

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a `.env` file in the root directory and add your OpenAI API Key (or other LLM provider config):
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

## Usage

```bash
# Ask a question
python -m hindsight.cli ask "How do I reverse a string in python?"

# Tell Hindsight a preference
python -m hindsight.cli remember "I prefer using list comprehensions instead of map/filter."

# The next time you ask a related question, Hindsight will recall your preference!
```
