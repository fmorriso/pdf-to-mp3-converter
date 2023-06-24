# Convert PDF to Audio mp3
## References
* [video tutorial: Automating My Life With Python](https://www.youtube.com/watch?v=LXsdt6RMNfY)
* [Original tutorial GitHub repo](https://github.com/TiffinTech/python-pdf-audo)
* [pypdf developer introduction](https://pypdf.readthedocs.io/en/latest/dev/intro.html)
* [pypdf extract text](https://pypdf.readthedocs.io/en/latest/user/extract-text.html)
## Changes required due to deprecated features of PyPDF2
* ```PdfFileReader``` replaced by ```PdfReader```
* ```reader.numpages``` replaced by ```len(reader.pages)```
* ```pdfReader.getPage(page_num)``` replaced by ```pdfReader.pages[page_num]```
* ```pdfReader.pages[page_num].extractText()``` replaced by ```pdfReader.pages[page_num].extract_text()```
## Conversion from PyPDF2 to PyPDF
* ```pip install pypdf```