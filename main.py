# comvert PDF to MP3
import pyttsx3, PyPDF2, sys
from pathlib import Path
from io import BytesIO


@staticmethod
def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'Running Python {get_python_version()}')

    with  Path.open('book.pdf','rb') as pdfFile:
        pdfStream = BytesIO(pdfFile.read())
        pdfReader = PyPDF2.PdfReader(pdfStream)
        speaker = pyttsx3.init()
        # process each individual page
        page_num: int = 0
        text:str = ''
        clean_text: str = ''
        for page_num in range(len(pdfReader.pages)):
            text = pdfReader.pages[page_num].extract_text()
            clean_text = text.strip().replace('\n', ' ')
            print(clean_text)

        speaker.save_to_file(clean_text, 'story.mp3')
        speaker.runAndWait()

        speaker.stop()