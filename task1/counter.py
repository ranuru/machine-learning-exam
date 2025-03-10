import nbformat
import re

# Load the notebook
notebook_path = "task1/notebook.ipynb"  # Change this to your notebook file
with open(notebook_path, "r", encoding="utf-8") as f:
    notebook = nbformat.read(f, as_version=4)

# Extract Markdown cells
markdown_cells = [
    cell["source"] for cell in notebook.cells if cell.cell_type == "markdown"
]

# Count words
word_count = sum(len(re.findall(r"\b\w+\b", cell)) for cell in markdown_cells)

print(f"Total word count in Markdown cells: {word_count}")
