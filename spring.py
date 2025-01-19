import tkinter as tk
from tkinter import ttk
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="CSDBORA",
    user="iie17",
    password="uyaufqia",  
    database="db_string"
)
cursor = conn.cursor()


def calculate_rating(job_type, company, keyword, job_title, job_description):
    # Apply rating strategies
    rating = 100  # Default rating

    # Convert keyword to string if it's not already
    keyword = str(keyword)

    # Convert job_title and job_description to strings if they are not already
    job_title = str(job_title) if job_title else ""
    job_description = str(job_description) if job_description else ""

    # Apply rating penalty based on job type
    if job_type != searched_job_type:
        rating -= 5  # For example, decrease rating by 5%

    # Apply rating penalty based on company
    if company != searched_company:
        rating -= 5  # For example, decrease rating by 10%

    # Check if the company is similar to the searched company
    if searched_company and company.startswith(searched_company):
        rating -= 5  # For example, decrease rating by 5%

    # Apply rating penalty if keyword is not found in job title or description
    if keyword and not (keyword.lower() in job_title.lower() or keyword.lower() in job_description.lower()):
        rating -= 15  # For example, decrease rating by 15%

    return rating


def search_jobs():
    global searched_job_type, searched_company

    searched_job_type = job_type_var.get()
    searched_company = company_var.get()
    keyword = keyword_entry.get().lower()

    sql = "SELECT * FROM job_table WHERE 1=1"
    conditions = []

    if searched_job_type:
        conditions.append(f"job_type = '{searched_job_type}'")
    if searched_company:
        conditions.append(f"(company = '{searched_company}' OR company LIKE '%{searched_company}%')")

    if conditions:
        sql += " AND " + " AND ".join(conditions)

    cursor.execute(sql)
    jobs = cursor.fetchall()

    display_jobs(jobs, keyword)


def display_jobs(jobs, keyword):
    result_text.delete('1.0', tk.END)

    if jobs:
        for job in jobs:
            job_title, company, job_description, specialization, job_type = job[:5]

            # Calculate rating
            rating = calculate_rating(job_title, company, keyword, job_title, job_description)

            result_text.insert(tk.END, f"Specialization: {job_title}\n")
            result_text.insert(tk.END, f"Job Title: {company} (Rating: {rating}%)\n")
            result_text.insert(tk.END, f"Job Type: {job_description}\n")
            result_text.insert(tk.END, f"Company: {specialization}\n")
            result_text.insert(tk.END, f"Description: {job_type}\n")
            
    else:
        result_text.insert(tk.END, "No jobs found.")


# Create GUI
root = tk.Tk()
root.title("Job Search")

main_frame = ttk.Frame(root)
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Job Type
job_type_label = ttk.Label(main_frame, text="Job Type:")
job_type_label.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)

job_type_var = tk.StringVar()
job_type_combobox = ttk.Combobox(main_frame, textvariable=job_type_var, width=20)
job_type_combobox.grid(column=1, row=0, padx=10, pady=10)
job_type_combobox['values'] = ['', 'regular', 'entry_level', 'intern']
job_type_combobox.current(0)

# Company
company_label = ttk.Label(main_frame, text="Company:")
company_label.grid(column=0, row=1, sticky=tk.W, padx=10, pady=10)

company_var = tk.StringVar()
company_combobox = ttk.Combobox(main_frame, textvariable=company_var, width=20)
company_combobox.grid(column=1, row=1, padx=10, pady=10)
company_combobox['values'] = ['', 'Facebook', 'Google', 'Microsoft', 'Meta', 'Amazon', 'Apple', 'IBM', 'Netflix',
                               'Adobe', 'Tesla', 'Twitter', 'LinkedIn', 'Goldman Sachs', 'Salesforce']
company_combobox.current(0)

# Keyword
keyword_label = ttk.Label(main_frame, text="Keyword:")
keyword_label.grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)

keyword_entry = ttk.Entry(main_frame, width=20)
keyword_entry.grid(column=1, row=2, padx=10, pady=10)

# Search Button
search_button = ttk.Button(main_frame, text="Search", command=search_jobs)
search_button.grid(column=0, row=3, columnspan=2, pady=10)

# Results
result_text = tk.Text(main_frame, width=80, height=20)
result_text.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

root.mainloop()

# Close database connection
cursor.close()
conn.close()
