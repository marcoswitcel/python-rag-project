from pathlib import Path
from docling.document_converter import DocumentConverter

def extract_doc():
    input_file = Path("./data/raw/dom-casmurro/pg55752-images.html")
    output_dir = Path("./data/processed")
    output_file = output_dir / "dom-casmurro.md"

    converter = DocumentConverter()
    result = converter.convert(str(input_file))
    document = result.document
    markdown_output = document.export_to_markdown()

    output_dir.mkdir(parents=True, exist_ok=True)

    output_file.write_text(markdown_output, encoding="utf-8")
