# PDF to Markdown Converter

A simple utility that converts PDF documents to markdown text using Docling.

## Using the Executable (No Python Required)

1. Download the latest release for your operating system from the [Releases](https://github.com/your-username/pdf-to-markdown-converter/releases) page
2. Open your terminal/command prompt and use the tool:

```bash
# Convert and print to console
pdf2md input.pdf

# Save to file
pdf2md input.pdf -o output.md

# Convert from URL
pdf2md https://example.com/document.pdf -o output.md
```

## For Developers

### Building from Source

1. Clone this repository:

```bash
git clone https://github.com/your-username/pdf-to-markdown-converter.git
cd pdf-to-markdown-converter
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Build the executable:

```bash
python build.py
```

The executable will be created in the `dist` directory.

### Using as a Python Package

```python
from pdf_to_markdown import PdfToMarkdown

converter = PdfToMarkdown()
result = converter.convert("input.pdf")
if result:
    print(result)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
