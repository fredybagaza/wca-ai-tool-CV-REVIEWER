
#What your project does 
1. Loads a CV file (PDF or DOCX) You give it a file like:
cv.pdf
cv.docx
 It reads the text inside the document.
 2. Extracts the text PDF → converts pages into text
DOCX → reads paragraphs
Output becomes plain text like:
Name: John Doe Experience: Software Developer... Skills: Python, Java...
3. Sends CV to AI (OpenAI) It sends your CV text with instructions:
“You are a recruiter. Analyze this CV.”
4. AI analyzes it like a recruiter It generates:
Strengths Good skills, Experience, Formatting
 Improvements What to add
What to fix
Better wording
 5. Prints result in terminal You see something like:

