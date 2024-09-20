import pdfplumber


with pdfplumber.open('test.pdf') as pdf:
    page = pdf.pages[0]
    te = page.extract_text()

print(page)
print(type(page))
print(te)