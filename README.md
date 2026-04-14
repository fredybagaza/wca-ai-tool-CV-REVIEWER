# -wca-ai-tool--CV-REVIEWER-
import PyPDF2
import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

# 🔴 SET YOUR TESSERACT PATH (Windows users)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def select_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select your CV",
        filetypes=[
            ("All supported", "*.pdf *.png *.jpg *.jpeg"),
            ("PDF files", "*.pdf"),
            ("Image files", "*.png *.jpg *.jpeg")
        ]
    )
    return file_path


def read_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text.lower()


def read_image(file_path):
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    return text.lower()


def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return read_pdf(file_path)
    elif ext in [".png", ".jpg", ".jpeg"]:
        return read_image(file_path)
    else:
        return ""


def score_cv(text):
    score = 0
    feedback = []

    # Sections (60 points)
    sections = {
        "education": 15,
        "experience": 20,
        "skills": 15,
        "projects": 10
    }

    for section, points in sections.items():
        if section in text:
            score += points
            feedback.append(f"✅ {section.capitalize()} section found (+{points})")
        else:
            feedback.append(f"❌ Missing {section.capitalize()} section (0/{points})")

    # Contact info (10 points)
    if "@" in text:
        score += 10
        feedback.append("✅ Email found (+10)")
    else:
        feedback.append("❌ Missing email (0/10)")

    # Length check (10 points)
    if len(text) > 1000:
        score += 10
        feedback.append("✅ Good CV length (+10)")
    else:
        feedback.append("⚠️ CV too short (0/10)")

    # Keywords (20 points)
    keywords = ["python", "java", "teamwork", "communication", "leadership"]
    found = sum(1 for word in keywords if word in text)
    keyword_score = (found / len(keywords)) * 20
    score += keyword_score

    feedback.append(f"✅ Keywords score: {int(keyword_score)}/20")

    return int(score), feedback


def main():
    print("Select your CV (PDF or Image)...")

    file_path = select_file()

    if not file_path:
        print("No file selected.")
        return

    try:
        text = extract_text(file_path)

        if not text.strip():
            print("Could not extract text. Try a clearer file.")
            return

        score, feedback = score_cv(text)

        print("\n--- CV ANALYSIS RESULT ---")
        print(f"⭐ CV Score: {score}/100\n")

        for item in feedback:
            print(item)

        print("\n💡 Tips:")
        if score < 50:
            print("- Add more sections like projects and skills")
            print("- Improve CV content and structure")
        elif score < 80:
            print("- Add more strong keywords")
            print("- Improve experience descriptions")
        else:
            print("- Great CV! Just fine-tune formatting")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
