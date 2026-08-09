from pathlib import Path
from docling.document_converter import DocumentConverter

def doc_converter(input_path: Path, file_name: str) -> None:
    output_dir = Path("./data/processed")
    output_file = output_dir / file_name

    converter = DocumentConverter()
    result = converter.convert(str(input_path))
    document = result.document
    markdown_output = document.export_to_markdown()

    output_dir.mkdir(parents=True, exist_ok=True)

    output_file.write_text(markdown_output, encoding="utf-8")