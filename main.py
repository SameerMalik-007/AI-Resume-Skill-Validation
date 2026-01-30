import tkinter as tk
from tkinter import filedialog, messagebox
from skill_matcher import extract_skills, calculate_score

def load_resume():
    file_path = filedialog.askopenfilename(
        title="Select Resume",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            resume_text.delete("1.0", tk.END)
            resume_text.insert(tk.END, file.read())

def analyze_resume():
    resume = resume_text.get("1.0", tk.END)
    job_skills_input = job_skills_entry.get()

    if not resume or not job_skills_input:
        messagebox.showerror("Error", "Please provide resume and job skills")
        return

    job_skills = [skill.strip().lower() for skill in job_skills_input.split(",")]

    resume_skills = extract_skills(resume)
    score, matched = calculate_score(resume_skills, job_skills)

    result_label.config(
        text=f"Skill Match Score: {score}%\nMatched Skills: {matched}"
    )

# GUI window
root = tk.Tk()
root.title("AI Resume Skill Validation Tool")
root.geometry("500x500")

tk.Label(root, text="AI Resume Skill Validator", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Upload Resume (TXT)", command=load_resume).pack()

resume_text = tk.Text(root, height=10, width=55)
resume_text.pack(pady=10)

tk.Label(root, text="Enter Job Skills (comma separated):").pack()
job_skills_entry = tk.Entry(root, width=50)
job_skills_entry.pack(pady=5)

tk.Button(root, text="Analyze Resume", command=analyze_resume).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
