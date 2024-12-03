import streamlit as st
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, pdf_content, job_description):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"{input_prompt}\n\nResume Content:\n{pdf_content}\n\nJob Description:\n{job_description}"
    response = model.generate_content(prompt)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

## Streamlit App

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description goes here: ", key="input")
uploaded_file = st.file_uploader("Upload your Resume in PDF format", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully!")

submit1 = st.button("Tell Me About the Resume!")
submit2 = st.button("How Can I Improvise my Skills?")
submit3 = st.button("Percentage match!")

input_prompt1 = """
As an experienced Technical Human Resource Manager with expertise in talent acquisition and candidate evaluation, your task is to thoroughly review the provided resume against the job description. Please provide a detailed professional evaluation addressing the following points:

1. Overall alignment: Assess how well the candidate's profile matches the role requirements.
2. Key strengths: Identify and elaborate on the top 3-5 strengths of the applicant that are particularly relevant to the job.
3. Areas for improvement: Highlight any gaps or weaknesses in the candidate's profile relative to the job requirements.
4. Technical skills assessment: Evaluate the candidate's technical skills and how they align with the specific technologies or tools mentioned in the job description.
5. Experience relevance: Analyze how the candidate's past experiences and projects relate to the responsibilities outlined in the job description.
6. Cultural fit: Based on the resume and job description, comment on potential cultural fit within the organization.
7. Unique selling points: Identify any standout qualities or experiences that set this candidate apart.

Conclude with a summary recommendation on the candidate's suitability for the role.
"""

input_prompt2 = """
As an expert career coach with extensive knowledge of the current job market, industry trends, and professional skill development, your task is to provide a comprehensive skill improvement plan based on the candidate's resume and the given job description. Structure your response as follows:

1. Skill Gap Analysis:
   Identify the top 3-5 key areas where the candidate's skills don't fully align with the job requirements. For each area, briefly explain its importance in the context of the job.

2. Prioritized Improvement Plan:
   Rank the identified skill gaps in order of importance and provide a strategic plan to address each one. Consider both short-term and long-term development goals.

3. Specific Skill Enhancement Recommendations:
   For each identified skill gap, provide detailed, actionable advice:
   a. Online Courses: Suggest 2-3 specific online courses or MOOCs (e.g., from Coursera, edX, Udacity) that address the skill gap. Include course names and platforms.
   b. Certifications: Recommend relevant professional certifications that would boost the candidate's credentials in this area.
   c. Practical Projects: Propose 1-2 hands-on projects or contributions (e.g., open-source projects, personal projects) that would demonstrate proficiency in the skill.
   d. Books or Resources: Suggest key books, websites, or other resources for self-study.

4. Soft Skills Development:
   Identify any soft skills (e.g., communication, leadership, problem-solving) that could be improved based on the job description. Provide specific strategies for developing these skills.

5. Networking and Industry Engagement:
   Suggest ways for the candidate to engage with the industry to support their skill development, such as joining professional associations, attending conferences, or participating in relevant online communities.

6. Timeline and Milestones:
   Propose a realistic timeline for acquiring or improving the identified skills, including key milestones to track progress.

7. Leveraging Existing Strengths:
   Identify the candidate's current strengths that are relevant to the job and suggest ways to further enhance and showcase these skills.

8. Future-Proofing Strategy:
   Based on industry trends related to the job description, recommend 1-2 emerging skills or technologies that the candidate should consider learning to stay competitive in the long term.

9. Tailoring the Resume:
   Provide advice on how the candidate can better highlight their skills and ongoing learning efforts in their resume to align with the job requirements.

Conclude with a motivational summary that encourages the candidate to pursue continuous learning and emphasizes the potential impact of these improvements on their career prospects.
"""

input_prompt3 = """
As a sophisticated ATS (Applicant Tracking System) scanner with advanced algorithms and a deep understanding of data science and modern recruitment practices, your task is to conduct a comprehensive evaluation of the resume against the provided job description. Please structure your analysis as follows:

1. Percentage Match: Begin with an overall percentage match between the resume and job description. Express this as a specific number (e.g., 75%).

2. Keyword Analysis:
   a. Present a list of keywords from the job description that are successfully matched in the resume.
   b. Identify important keywords or phrases from the job description that are missing in the resume.

3. Skills Assessment:
   a. List the technical skills found in the resume that align with the job requirements.
   b. Highlight any critical skills mentioned in the job description that are absent from the resume.

4. Experience Alignment:
   Evaluate how well the candidate's experience aligns with the job requirements, noting any gaps or particularly strong matches.

5. Education and Certifications:
   Comment on the relevance of the candidate's educational background and any certifications to the job requirements.

6. ATS Optimization Suggestions:
   Provide specific recommendations for improving the resume's ATS compatibility and increasing its match percentage.

7. Final Thoughts:
   Summarize the overall suitability of the candidate for the position based on this ATS analysis, highlighting both strengths and areas for improvement.

Ensure that your analysis is data-driven, objective, and provides actionable insights for both the candidate and potential employers.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("Resume Review:")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("Skills Improvement Suggestions:")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("ATS Percentage match:")
        st.write(response)
    else:
        st.write("Please upload the resume")