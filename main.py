# comvert PDF to MP3

import pathlib
import sys
from io import BytesIO
from pathlib import Path

# https://pypdf.readthedocs.io/en/latest/
import pypdf
import pyttsx3
from PyPDF2 import PdfReader
from pyttsx3 import Engine


@staticmethod
def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


if __name__ == '__main__':
    print(f'Running Python {get_python_version()}')

    outputFilename: str = 'story.mp3'
    outputFilePath: Path = pathlib.Path(outputFilename)
    outputFilePath.unlink(missing_ok=True)

    inputFilename: str = 'book.pdf'
    inputFilePath: Path = pathlib.Path(inputFilename)

    pdfStream: BytesIO = None
    pdfReader: PdfReader = None
    speaker: Engine = None

    with inputFilePath.open() as pdfFile:
        pdfReader = PdfReader(inputFilePath)
        speaker = pyttsx3.init()
        # process each individual page
        page_num: int = 0
        text: str = ''
        clean_text: str = ''
        for page in pdfReader.pages:
            page_num += 1
            print(f'processing page {page_num}')
            text = page.extract_text()
            clean_text = text.strip().replace('\n', ' ')
            print(clean_text)

        speaker.save_to_file(clean_text, outputFilename)
        speaker.runAndWait()

        speaker.stop()
