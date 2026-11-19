import json
from pathlib import Path
from pypdf import PdfReader
from bs4 import BeautifulSoup

PDF_FOLDER = Path("downloads/pdfs")
HTML_FOLDER = Path("downloads/html")

processed_documents = []


def read_pdf(pdf_path):

    text = ""

    try:

        reader = PdfReader(pdf_path)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

    except Exception as e:

        print(f"PDF Error: {pdf_path.name}")
        print(e)

    return text


def read_html(html_path):

    try:

        html_content = html_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        soup = BeautifulSoup(
            html_content,
            "html.parser"
        )

        return soup.get_text(
            separator=" ",
            strip=True
        )

    except Exception as e:

        print(f"HTML Error: {html_path.name}")
        print(e)

        return ""


# -------------------------------
# Process PDFs
# -------------------------------

for pdf_file in PDF_FOLDER.glob("*.pdf"):

    print(
        f"Processing PDF: {pdf_file.name}"
    )

    text = read_pdf(pdf_file)

    processed_documents.append(
        {
            "document_name": pdf_file.name,
            "document_type": "pdf",
            "source_file": str(pdf_file),
            "content": text
        }
    )


# -------------------------------
# Process HTML
# -------------------------------

for html_file in HTML_FOLDER.glob("*.html"):

    print(
        f"Processing HTML: {html_file.name}"
    )

    text = read_html(html_file)

    processed_documents.append(
        {
            "document_name": html_file.name,
            "document_type": "html",
            "source_file": str(html_file),
            "content": text
        }
    )


# -------------------------------
# Save structured output
# -------------------------------

Path(
    "processed"
).mkdir(
    exist_ok=True
)

with open(
    "processed/processed_documents.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        processed_documents,
        file,
        indent=4,
        ensure_ascii=False
    )

print(
    f"\nDocuments Processed: {len(processed_documents)}"
)
