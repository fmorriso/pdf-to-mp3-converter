# Convert PDF to Audio mp3
## References
* [Automating My Life With Python](https://www.youtube.com/watch?v=LXsdt6RMNfY)
* [GitHub repo](https://github.com/TiffinTech/python-pdf-audo)
## Changes required due to deprecated features of PyPDF2
* PdfFileReader replaced by PdfReader
* reader.numpages replaced by len(reader.pages)
* pdfReader.getPage(page_num) replaced by pdfReader.pages[page_num]
* pdfReader.pages[page_num].extractText() replaced by pdfReader.pages[page_num].extract_text()
* 