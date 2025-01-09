import argparse
from enum import Enum
from pypdf import PdfReader, PdfWriter, PaperSize

PaperSizeEnum = Enum('PaperSizeEnum', PaperSize.__dict__)

PAGE_SIZES = {i.name: i.value for i in PaperSizeEnum}

def scale_pdf(input_path, output_path, target_size):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        page.scale_to(*target_size)
        writer.add_page(page)

    with open(output_path, "wb") as output_file:
        writer.write(output_file)

def main():
    parser = argparse.ArgumentParser(
        description="Scale a PDF to a specified page size (e.g., A3, A4, A5)."
    )
    parser.add_argument(
        "page_size",
        type=str,
        choices=PAGE_SIZES.keys(),
        help="Target page size",
    )
    parser.add_argument(
        "input_pdf",
        type=str,
        help="Path to the input PDF file.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Path to the output PDF file. Defaults to '<input>_<page_size>.pdf'.",
    )

    args = parser.parse_args()
    page_size_name = args.page_size
    input_pdf = args.input_pdf
    output_pdf = args.output or input_pdf.replace(".pdf", f"_{page_size_name}.pdf")

    target_size = PAGE_SIZES[page_size_name]
    scale_pdf(input_pdf, output_pdf, target_size)

    print(f"Scaled PDF saved to: {output_pdf}")

if __name__ == "__main__":
    main()
