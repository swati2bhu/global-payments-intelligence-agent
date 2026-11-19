from pypdf import PdfReader
pdf_path = r"D:\paymentsCopilot\docs\1794363534901.pdf"
reader = PdfReader(pdf_path)
print(f"total pages= {len(reader.pages)}")
for page_num,page in enumerate(reader.pages):
	text=page.extract_text()
	print(f"\n---PAGE{page_num +1} ---\n")
	print(text)
	print(f"Type: {type(text)}")
	