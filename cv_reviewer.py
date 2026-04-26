import os
from dotenv import load_dotenv
from openai import OpenAI
import PyPDF2
import docx


load_dotenv()

api_key = os.getenv("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")

print("DEBUG KEY:", api_key)  # temporary check

client = OpenAI(api_key=api_key)

#  Read PDF
def read_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text


# 📄 Read DOCX
def read_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])


# Get feedback from AI
def get_cv_feedback(cv_text):
    prompt = f"""
You are an expert HR recruiter and CV reviewer.
Analyze the following CV and provide:

1. Loads a cv file
2. Extracts the PDF
3. sends Cv to AI
4. AI analyzes the CV
{cv_text}
"""

    try:
        response = client.responses.create(
            model="gpt-4.1",
            input=prompt
        )

        return response.output_text

    except Exception as e:
        return f"Error: {str(e)}"


#  Main program
def main():
    print("=== CV Reviewer Tool ===")
    print("1. Paste CV")
    print("2. Upload file (PDF/DOCX)")

    choice = input("Choose option (1/2): ")

    if choice == "2":
        file_path = "C:/Users/admin/Desktop/file_path/cv.pdf"

        if not os.path.exists(file_path):
            print("File not found.")
            return

        if file_path.endswith(".pdf"):
            cv_text = read_pdf(file_path)

        elif file_path.endswith(".docx"):
            cv_text = read_docx(file_path)

        else:
            print("Unsupported file type.")
            return

    else:
        print("\nPaste your CV (press ENTER twice to finish):\n")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)

        cv_text = "\n".join(lines).strip()

    if not cv_text:
        print("No CV content found.")
        return

    print("\nAnalyzing...\n")

    feedback = get_cv_feedback(cv_text)

    print("=== RESULT ===\n")
    print(feedback)


if __name__ == "__main__":
    main()
