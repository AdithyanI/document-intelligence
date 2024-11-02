import argparse
from pdf_to_markdown import PdfToMarkdown

def main():
    parser = argparse.ArgumentParser(description='Convert PDF to Markdown')
    parser.add_argument('input', help='Input PDF file path or URL')
    parser.add_argument('-o', '--output', help='Output markdown file (optional, prints to console if not specified)')
    
    args = parser.parse_args()
    
    converter = PdfToMarkdown()
    result = converter.convert(args.input)
    
    if result:
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"Successfully converted to {args.output}")
        else:
            print(result)

if __name__ == '__main__':
    main() 