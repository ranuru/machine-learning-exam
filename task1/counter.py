import nbformat
import re

# Load the notebook
notebook_path = "notebook.ipynb"  # Change this to your notebook file
with open(notebook_path, "r", encoding="utf-8") as f:
    notebook = nbformat.read(f, as_version=4)

# Extract Markdown cells
markdown_cells = [
    cell["source"] for cell in notebook.cells if cell.cell_type == "markdown"
]


# Count words in Markdown cells except the first two
def count_words(text):
    # Remove Markdown syntax
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)  # Remove images
    text = re.sub(r"\[.*?\]\(.*?\)", "", text)  # Remove links
    text = re.sub(r"[*_`~]", "", text)  # Remove formatting characters
    words = re.findall(r"\b\w+\b", text)
    return len(words)


word_count = 0
for cell in markdown_cells[2:]:
    word_count += count_words(cell)
# Print the total word count
print(f"Total word count in Markdown cells (excluding the first two): {word_count}")
