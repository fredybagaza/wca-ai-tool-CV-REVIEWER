# Coverpage
Group name=AI code
Member names=Bagaza Rugari FRedy, asachi beverly, David raul
Github link= https://github.com/fredybagaza/wca-ai-tool-CV-REVIEWER
Tool name= wca-ai-tool-CV-REVIEWER
Date= 26th April 2026

#2. Problem Statement:what problems does it solve
*poorly written CVs
-spellings
-grammar errors
-messy formatting
* A Cv reviewer helps make the CV stronger, 
cleaner, and more attention-grabbing quicky

*who benefits
fresh graduates- need help creating first professional CVs
job seekers-people applying for jobs need better CVs for better chances of interviews

#TOOL DESCRIPTION:what it does
1. Loads a cv file
2. Extracts the PDF
3. sends Cv to AI
4. AI analyzes the CV 
*How does a user interface with it
-through a website
-a mobile up
-desktop app
-chat tool where they upload or paste their cv and receive feedback

#4. AI Instruction Design (R-T-C-C-O Framework)
Role-You are an expert CV reviewer and HR recruiter
Task-Analyze the uploaded CV and provide professional feedback
-states what the AI must do
Tone-helpful,clear and professional 
-controls writing style
Context-Applying for entry-level jobs
-gives background information
Output Format-Numbered list with scores and sections
-structure the answer 

#5. TECHNICAL OVERVIEW- how the python code works(with key code snippets)
-python code usually follows simple pipeline
*upload or read the cv file
*extract text from PDF
*clean the text
*send the text to AI
*generates feedback
*shows results tothe user

# IMPORT  REQUIRED LIBRARIES
-Libraries help read files 
-os-reads environment variables
-dotenv-loads API key from .env
-OpenAI-connects to AI model
-PyPDF2-reads PDF cv files

LOAD API KEY
load _dotenv
-securely loads API key without hardcoding it

READ THE CV FILE
-def:extract _ pdf_text
-reads each page of the pdf and combines all text  
 
 BUILD THE PROMPT
-cv_text=extract_pdf_text
-tells AI exactly how to review the cv

SEND TO THE AI MODEL
-response= client.response.create
-sends the CV text to the AI for analysis

PRINT THE RESULTS
print(response.output_text)
-shows the review in the terminal

#6.Challenges and solutions
-API key not working
*authentication failed
*invalid AI key
solution-
-Syntax error
*i.e Syntaxerror:invalid syntax

7. Ethics Reflection

8. Conclusion and future improvements

9. Appendix
