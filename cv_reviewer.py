import os
import argparse
from docx import document
from dotenv import load_dotenv
from openai import OpenAI
from PyPDF2 import PdfFileReader
import docx

load_dotenv()
client = OpenAI(api_key=os.getenv("openAI_API_key"))
#extract text from pdf
def extract_text ():"C:\Users\admin\Desktop\cv reviewer\cv.pdf.pdf"

from docx import Document

file_path = r"C:\Users\admin\Desktop\cv reviewer\cv.docx"

if file_path.endswith(".docx"):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    print(text)

import PyPDF2

file_path = r"C:\Users\admin\Desktop\cv reviewer\cv.pdf"

if file_path.endswith(".pdf"):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    
    print(text)

