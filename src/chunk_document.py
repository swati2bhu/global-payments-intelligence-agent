from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
pdf_path = r"D:\paymentsCopilot\docs\1794363534901.pdf"
reader = PdfReader(pdf_path)
all_text = ""
for page in reader.pages:
	text = page.extract_text()
	if text:
		all_text += text
print(f"Total Document Length = {len(all_text)}")

splitter = RecursiveCharacterTextSplitter(
	chunk_size = 1000,
	chunk_overlap = 200
)

chunks = splitter.split_text(all_text)
print(f"total chunks create = 	{len(chunks)}")

for i, chunk in enumerate(chunks):
	print(f"\n............chunk{i+1}..........\n")
	print(chunk[:300])
