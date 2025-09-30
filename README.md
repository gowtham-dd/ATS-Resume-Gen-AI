
# Resume ATS Expert

This project is a **Resume ATS (Applicant Tracking System) Expert** built using **Python** and **Streamlit**. It leverages **Google Gemini AI** (Generative AI) to analyze resumes and provide insights for job applications.

---

## Features

1. Upload a **resume in PDF format**.
2. Provide a **job description** for comparison.
3. Analyze the resume to:
   - Summarize the candidate’s background, experience, education, and skills.
   - Suggest improvements for skills and career growth.
   - Provide a percentage match between the resume and the job description.

---

## How It Works

1. The uploaded PDF resume is processed using **PyMuPDF (fitz)** to extract text from the pages.
2. The extracted text, along with the job description and input prompts, is sent to **Google Gemini AI**.
3. Gemini AI generates responses based on the selected action:
   - **Tell me about the resume**
   - **How can I improve my skills**
   - **Percentage match with job description**
4. The results are displayed on the Streamlit web interface.

---

## Requirements

- Python 3.10+
- Streamlit
- PyMuPDF
- google-generativeai
- python-dotenv
- Pillow

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/gowtham-dd/ATS-Resume-Gen-AI.git
````

2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your Google API key:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## Running the App

```bash
streamlit run app.py
```

Open the displayed URL in your browser to access the Resume ATS interface.

---

## Usage

1. Enter the job description in the input box.
2. Upload the candidate’s PDF resume.
3. Click one of the buttons to analyze:

   * **Tell me about the Resume**
   * **How can I improve my skills**
   * **Percentage Match**
4. The response will be displayed below the selected action.

---

## Notes

* Ensure the PDF is **text-based** for accurate extraction.
* Only the **first page** is analyzed for now, but the code can be extended to multi-page resumes.
* Google Gemini AI account and API key are required.

