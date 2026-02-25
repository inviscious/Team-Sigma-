import tkinter as tk
from tkinter import messagebox, filedialog
import random

# =========================
# SCHOOL MANAGEMENT SYSTEM
# =========================

class SchoolManagementSystem:

    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("800x600")

        self.students = []

        # =====================
        # TITLE
        # =====================
        tk.Label(root, text="SCHOOL MANAGEMENT SYSTEM",
                 font=("Arial", 16, "bold")).pack(pady=10)

        # =====================
        # FORM FRAME
        # =====================
        form_frame = tk.Frame(root)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="School ID (8 digits):").grid(row=0, column=0, sticky="w")
        self.id_entry = tk.Entry(form_frame)
        self.id_entry.grid(row=0, column=1)

        tk.Label(form_frame, text="First Name:").grid(row=1, column=0, sticky="w")
        self.first_entry = tk.Entry(form_frame)
        self.first_entry.grid(row=1, column=1)

        tk.Label(form_frame, text="Last Name:").grid(row=2, column=0, sticky="w")
        self.last_entry = tk.Entry(form_frame)
        self.last_entry.grid(row=2, column=1)

        tk.Label(form_frame, text="Courses (comma separated):").grid(row=3, column=0, sticky="w")
        self.course_entry = tk.Entry(form_frame, width=40)
        self.course_entry.grid(row=3, column=1)

        tk.Label(form_frame, text="Phone (07XXXXXXXX):").grid(row=4, column=0, sticky="w")
        self.phone_entry = tk.Entry(form_frame)
        self.phone_entry.grid(row=4, column=1)

        tk.Button(form_frame, text="Add Student",
                  command=self.add_student,
                  bg="green", fg="white").grid(row=5, columnspan=2, pady=10)

        # =====================
        # LIST DISPLAY
        # =====================
        self.listbox = tk.Listbox(root, width=100)
        self.listbox.pack(pady=10)

        # =====================
        # EXPORT BUTTON
        # =====================
        tk.Button(root, text="Export to Text File",
                  command=self.export_students,
                  bg="blue", fg="white").pack(pady=10)

        # Load 10 students
        self.preload_students()

    # =========================
    # VALIDATION
    # =========================

    def validate_id(self, school_id):
        return school_id.isdigit() and len(school_id) == 8

    def validate_phone(self, phone):
        return phone.startswith("07") and phone.isdigit() and len(phone) == 10

    # =========================
    # ADD STUDENT
    # =========================

    def add_student(self):
        school_id = self.id_entry.get()
        first = self.first_entry.get()
        last = self.last_entry.get()
        courses = self.course_entry.get()
        phone = self.phone_entry.get()

        if not (school_id and first and last and courses and phone):
            messagebox.showerror("Error", "All fields are required!")
            return

        if not self.validate_id(school_id):
            messagebox.showerror("Error", "School ID must be exactly 8 digits!")
            return

        if not self.validate_phone(phone):
            messagebox.showerror("Error", "Phone must be Kenyan format 07XXXXXXXX")
            return

        student = {
            "id": school_id,
            "first": first,
            "last": last,
            "courses": courses,
            "phone": phone
        }

        self.students.append(student)

        self.listbox.insert(tk.END,
                            f"{school_id} | {first} {last} | {courses} | {phone}")

        self.clear_fields()

    # =========================
    # CLEAR FORM
    # =========================

    def clear_fields(self):
        self.id_entry.delete(0, tk.END)
        self.first_entry.delete(0, tk.END)
        self.last_entry.delete(0, tk.END)
        self.course_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    # =========================
    # EXPORT TO TEXT FILE
    # =========================

    def export_students(self):
        file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )

        if file:
            with open(file, "w") as f:
                for student in self.students:
                    f.write(f"ID: {student['id']}\n")
                    f.write(f"Name: {student['first']} {student['last']}\n")
                    f.write(f"Courses: {student['courses']}\n")
                    f.write(f"Phone: {student['phone']}\n")
                    f.write("-" * 40 + "\n")

            messagebox.showinfo("Success", "Students exported successfully!")

    # =========================
    # PRELOAD 10 STUDENTS
    # =========================

    def preload_students(self):

        first_names = ["Brian", "Faith", "Kevin", "Mercy", "James",
                       "Ann", "Daniel", "Esther", "Samuel", "Lydia"]

        last_names = ["Otieno", "Mwangi", "Wanjiku", "Ochieng",
                      "Kamau", "Njeri", "Kiptoo", "Achieng",
                      "Mutiso", "Wambui"]

        courses_list = [
            "Mathematics, English, Biology",
            "Physics, Chemistry, Mathematics",
            "Computer Science, Mathematics",
            "History, Geography, CRE",
            "Business, Economics, Mathematics"
        ]

        for i in range(10):
            school_id = str(random.randint(10000000, 99999999))
            first = first_names[i]
            last = last_names[i]
            courses = random.choice(courses_list)
            phone = "07" + str(random.randint(10000000, 99999999))[:8]

            student = {
                "id": school_id,
                "first": first,
                "last": last,
                "courses": courses,
                "phone": phone
            }

            self.students.append(student)

            self.listbox.insert(
                tk.END,
                f"{school_id} | {first} {last} | {courses} | {phone}"
            )


# =========================
# RUN PROGRAM
# =========================

if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolManagementSystem(root)
    root.mainloop()