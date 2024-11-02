# PDF to Markdown Converter

A simple Python utility that converts PDF documents to markdown text using Docling.

## Features

- Convert PDF files to markdown text
- Support for both local PDF files and URLs
- Simple, reusable Python class
- Error handling included

## Installation

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

## Usage

```python
from pdf_to_markdown import PdfToMarkdown

# Initialize converter
converter = PdfToMarkdown()

# Convert from local file
markdown = converter.convert("path/to/your/document.pdf")
if markdown:
    print(markdown)

# Convert from URL
markdown = converter.convert("https://example.com/document.pdf")
if markdown:
    print(markdown)
```

## Error Handling

The `convert()` method returns `None` if the conversion fails, and prints an error message. Always check the return value before using the result.

## Example

```python
converter = PdfToMarkdown()

# Example with a local file
result = converter.convert("sample.pdf")
if result:
    with open("output.md", "w", encoding="utf-8") as f:
        f.write(result)

# Example with a URL
result = converter.convert("https://arxiv.org/pdf/2408.09869")
if result:
    print(result)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
