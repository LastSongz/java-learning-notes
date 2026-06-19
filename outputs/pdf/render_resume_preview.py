from pathlib import Path

import pypdfium2 as pdfium


BASE_DIR = Path(__file__).resolve().parent
PDF = BASE_DIR / "6年-Java-本科.pdf"
OUT_DIR = BASE_DIR / "preview"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = pdfium.PdfDocument(PDF)
    print(f"pages {len(doc)}")
    for index, page in enumerate(doc, start=1):
        path = OUT_DIR / f"page_{index}.png"
        page.render(scale=2).to_pil().save(path)
        print(path)


if __name__ == "__main__":
    main()
