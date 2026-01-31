#  AI-Resume-Skill-Validation

A simple and user-friendly desktop application built using Python (Tkinter) and Natural Language Processing (spaCy), designed to help recruiters and users analyze resumes and validate skills by comparing them with job requirements through a clean graphical interface.
---

##  Features :
- Upload Resume (TXT format)
- AI-based Skill Extraction using NLP
- Automatic Skill Match Percentage Calculation
- Displays Matched Skills Clearly
- Simple and Interactive Tkinter GUI
- Modular Code Structure (Separate AI logic and GUI files)
- GitHub Collaboration with Version Control
---

##  Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.x | Core programming |
| Tkinter | GUI |
| SpaCy | Natural Language Processing |
| Git & GitHub | Collaboration and version control |

---

## 🗂️ Project Structure

├── main.py              # Entry point of the application (Tkinter GUI)
├── skill_matcher.py     # Handles AI skill extraction and matching logic
├── requirements.txt    # Required Python libraries
├── README.md           # Project documentation (this file)
├── resume.txt   # Sample resume for testing
├── assets/screenshots/ # Application screenshots (used in report)

## How to Run the Project
# Install Dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# Run the Application
python main.py

# How to Use

- Click Upload Resume (TXT)
- Select a resume file

- Enter required job skills (comma-separated)
Example:

python, machine learning, sql

- Click Analyze Resume

- View the skill match score and matched skills

# Group Members
# Name	Roll Number
- Sameer Malik	F2023105007
- M Huzaifa Mahmood	F2023105004

# Screenshots
You can find all screenshots in the /assets/screenshots/ folder, and they're also included in the project report.
