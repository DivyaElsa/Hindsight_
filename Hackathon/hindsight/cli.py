import typer
from rich.console import Console
from rich.markdown import Markdown
from hindsight.rag import ask_hindsight
from hindsight.memory import add_to_memory

app = typer.Typer(help="Hindsight Coding Assistant CLI")
console = Console()

@app.command()
def ask(
    query: str = typer.Argument(..., help="The coding question or task"),
):
    """
    Ask Hindsight a coding question. It will use its long-term memory to provide context-aware answers.
    """
    console.print(f"[bold blue]Thinking about:[/bold blue] {query}")
    
    # Get answer from RAG
    answer = ask_hindsight(query)
    
    console.print("[bold green]Hindsight:[/bold green]")
    console.print(Markdown(answer))
    
    # Save the interaction to memory
    add_to_memory(query, answer)

@app.command()
def remember(
    preference: str = typer.Argument(..., help="A coding preference to remember (e.g., 'I prefer tabs over spaces')")
):
    """
    Tell Hindsight to remember a specific coding preference or fact.
    """
    add_to_memory(f"Preference: {preference}", "User preference recorded.")
    console.print(f"[bold green]Remembered:[/bold green] {preference}")

if __name__ == "__main__":
    app()
