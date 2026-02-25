import tkinter as tk
from tkinter import messagebox, filedialog

# -----------------------------
# Student Storage
# -----------------------------
students = []

# -----------------------------
# Preloaded 20 Random Students
# -----------------------------
preloaded_students = [
    {"ID":"48273619","First":"Brian","Last":"Mwangi","Courses":"Mathematics, Physics, Computer Science","Phone":"0712345678"},
    {"ID":"59381724","First":"Faith","Last":"Achieng","Courses":"Biology, Chemistry, Environmental Science","Phone":"0723456789"},
    {"ID":"84726135","First":"Kevin","Last":"Otieno","Courses":"Economics, Business Studies, Accounting","Phone":"0734567890"},
    {"ID":"73649281","First":"Sharon","Last":"Wanjiku","Courses":"English, Literature, History","Phone":"0745678901"},
    {"ID":"91827364","First":"Daniel","Last":"Kiptoo","Courses":"Mathematics, Computer Science, Statistics","Phone":"0756789012"},
    {"ID":"56473829","First":"Mercy","Last":"Njeri","Courses":"Nursing, Biology, Community Health","Phone":"0767890123"},
    {"ID":"82736491","First":"Victor","Last":"Mutua","Courses":"Mechanical Engineering, Physics, Calculus","Phone":"0778901234"},
    {"ID":"19384756","First":"Cynthia","Last":"Atieno","Courses":"Law, Political Science, Sociology","Phone":"0789012345"},
    {"ID":"67482915","First":"Collins","Last":"Kamau","Courses":"Architecture, Design, Mathematics","Phone":"0701234567"},
    {"ID":"38592017","First":"Ruth","Last":"Chebet","Courses":"Pharmacy, Chemistry, Human Anatomy","Phone":"0713456789"},
    {"ID":"74628193","First":"Samuel","Last":"Ochieng","Courses":"Information Technology, Networking, Cyber Security","Phone":"0724567891"},
    {"ID":"21938475","First":"Grace","Last":"Wambui","Courses":"Education, English, Psychology","Phone":"0735678902"},
    {"ID":"95837261","First":"Peter","Last":"Kibet","Courses":"Civil Engineering, Structural Design, Physics","Phone":"0746789013"},
    {"ID":"62193748","First":"Lydia","Last":"Akinyi","Courses":"Journalism, Media Studies, Communication","Phone":"0757890124"},
    {"ID":"83472615","First":"George","Last":"Maina","Courses":"Finance, Economics, Statistics","Phone":"0768901235"},
    {"ID":"47281936","First":"Esther","Last":"Jepchirchir","Courses":"Public Health, Biology, Research Methods","Phone":"0779012346"},
    {"ID":"30918274","First":"John","Last":"Kariuki","Courses":"Software Engineering, Programming, Databases","Phone":"0780123457"},
    {"ID":"58637492","First":"Irene","Last":"Naliaka","Courses":"Tourism, Hospitality Management, Geography","Phone":"0702345678"},
    {"ID":"71928364","First":"Mark","Last":"Musyoka","Courses":"Electrical Engineering, Circuit Analysis, Mathematics","Phone":"0714567890"},
    {"ID":"86429137","First":"Agnes","Last":"Nyambura","Courses":"Criminology, Law, Forensic Science","Phone":"0725678901"},
]

students.extend(preloaded_students)

# -----------------------------
# Functions
# -----------------------------
def refresh_listbox():
    listbox.delete(0, tk.END)
    for student in students:
        listbox.insert(tk.END, f"{student['ID']} - {student['First']} {student['Last']}")

def add_student():
    student_id = entry_id.get()
    first = entry_first.get()
    last = entry_last.get()
    courses = entry_courses.get()
    phone = entry_phone.get()

    if not student_id or not first or not last or not courses or not phone:
        messagebox.showerror("Error", "All fields are required!")
        return

    if len(student_id) != 8 or not student_id.isdigit():
        messagebox.showerror("Error", "Student ID must be 8 digits!")
        return

    if not phone.startswith("07") or len(phone) != 10:
        messagebox.showerror("Error", "Phone must start with 07 and be 10 digits!")
        return

    new_student = {
        "ID": student_id,
        "First": first,
        "Last": last,
        "Courses": courses,
        "Phone": phone
    }

    students.append(new_student)
    refresh_listbox()
    clear_fields()
    messagebox.showinfo("Success", "Student added successfully!")

def clear_fields():
    entry_id.delete(0, tk.END)
    entry_first.delete(0, tk.END)
    entry_last.delete(0, tk.END)
    entry_courses.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

def export_students():
    if not students:
        messagebox.showwarning("Warning", "No students to export!")
        return

    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text files", "*.txt")])
    if file:
        with open(file, "w") as f:
            for s in students:
                f.write(f"Student ID: {s['ID']}\n")
                f.write(f"First Name: {s['First']}\n")
                f.write(f"Last Name: {s['Last']}\n")
                f.write(f"Courses: {s['Courses']}\n")
                f.write(f"Phone: {s['Phone']}\n")
                f.write("-" * 40 + "\n")
        messagebox.showinfo("Success", "Exported successfully!")

# -----------------------------
# GUI
# -----------------------------
root = tk.Tk()
root.title("School Management System")
root.geometry("600x650")

tk.Label(root, text="School Management System", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Student ID (8 digits)").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="First Name").pack()
entry_first = tk.Entry(root)
entry_first.pack()

tk.Label(root, text="Last Name").pack()
entry_last = tk.Entry(root)
entry_last.pack()

tk.Label(root, text="Courses (comma separated)").pack()
entry_courses = tk.Entry(root, width=50)
entry_courses.pack()

tk.Label(root, text="Phone Number (07XXXXXXXX)").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

tk.Button(root, text="Add Student", command=add_student, bg="green", fg="white").pack(pady=10)
tk.Button(root, text="Export to Text File", command=export_students, bg="blue", fg="white").pack(pady=5)

tk.Label(root, text="Student List", font=("Arial", 12, "bold")).pack(pady=10)
listbox = tk.Listbox(root, width=70)
listbox.pack(pady=10)

refresh_listbox()

root.mainloop()