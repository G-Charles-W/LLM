import pymupdf4llm
import pathlib
md_text = pymupdf4llm.to_markdown("data/admire_guide.pdf")
print(md_text)


output_file = pathlib.Path("output.md")
output_file.write_bytes(md_text.encode())