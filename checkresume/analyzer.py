import pdfplumber
import spacy
import json
from groq import Groq
# using for extract text from pdf


def exrtract_text_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    
    return text.strip()
API_KEY = "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"

def analyze_resume_with_llm(resume: str, job_description: str) -> dict:
    promt=f"""
            You are a AI assistant that helps to analyze resume and job description.
            You have to analyze the resume and job description to find the best match.
            Given a resume and a job description,extract the following details:

            1. Identify all skills mentioned in the resume and job description.
            2. calculate the all years of experience mentioned in the resume.
            3. Identify the education qualification mentioned in the resume.
            4. Identify the experience level of the candidate.
            5. categories the projects based on domain(e.g AI, webdevelopment,Cloud etc).
            6. Rank the resume relevance to the job description on a scale of 0 to 100.

            Resume:
            {resume_text}
            job_description:
            {job_description}

            provide the valid output in json format with this structure :
            {{
                "rank":"<parcentage>",
                "skills":["<skill1>","<skill2>"],
                "experience":"<years>",
                "project_category":["<category1>","<category2>"],
            }}
            """
    try:
        client = Groq(api_key=API_KEY)
        response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
        {
            "role": "user",
            "content": promt,}],
        temperature=0.7,
        response_format="json_object",
        )
        result = response.choices[0].messages.content
        return json.loads(result)
    except Exception as e:
        print(e) 


def process_resume(resume_path, job_description):
    try:
        resume_text = exrtract_text_pdf(resume_path)
        data = analyze_resume_with_llm(resume_text, job_description)
        return data
    except Exception as e:
        print(e)