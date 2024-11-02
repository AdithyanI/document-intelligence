from docling.document_converter import DocumentConverter
from pathlib import Path
from typing import Union, Optional

class PdfToMarkdown:
    """A simple class to convert PDF documents to markdown text using Docling."""
    
    def __init__(self):
        """Initialize the PDF to Markdown converter."""
        self.converter = DocumentConverter()

    def convert(self, source: Union[str, Path]) -> Optional[str]:
        """
        Convert a PDF document to markdown text.
        
        Args:
            source: Path to PDF file or URL to PDF document
            
        Returns:
            str: Markdown text of the converted document
            None: If conversion fails
            
        Example:
            converter = PdfToMarkdown()
            markdown_text = converter.convert("path/to/document.pdf")
            # or
            markdown_text = converter.convert("https://arxiv.org/pdf/2408.09869")
        """
        try:
            # Convert the document
            result = self.converter.convert(source)
            
            # Export to markdown text
            markdown_text = result.document.export_to_markdown()
            
            return markdown_text
            
        except Exception as e:
            print(f"Error converting PDF: {str(e)}")
            return None 