import tkinter as tk
from tkinter import ttk, messagebox, filedialog

students = []

def add_student():
    data = [id_e.get(), fn_e.get(), ln_e.get(), course_e.get(), phone_e.get()]
    if "" in data:
        messagebox.showerror("Error", "All fields required")
        return
    if any(s[0] == data[0] for s in students):
        messagebox.showerror("Error", "ID exists")
        return
    students.append(data)
    tree.insert("", tk.END, values=data)
    clear()

def delete_student():
    for item in tree.selection():
        students[:] = [s for s in students if s[0] != tree.item(item)["values"][0]]
        tree.delete(item)

def search_student():
    key = search_e.get().lower()
    tree.delete(*tree.get_children())
    for s in students:
        if key in str(s).lower():
            tree.insert("", tk.END, values=s)

def export_students():
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    if not file: return
    with open(file, "w") as f:
        for s in students:
            f.write(", ".join(s) + "\n")
    messagebox.showinfo("Success", "Exported")

def clear():
    for e in [id_e, fn_e, ln_e, course_e, phone_e]:
        e.delete(0, tk.END)

# --- UI ---
root = tk.Tk()
root.title("Simple School System")
root.geometry("900x500")

labels = ["ID", "First Name", "Last Name", "Course", "Phone"]
entries = []

for i, text in enumerate(labels):
    tk.Label(root, text=text).grid(row=0, column=i)
    e = tk.Entry(root)
    e.grid(row=1, column=i)
    entries.append(e)

id_e, fn_e, ln_e, course_e, phone_e = entries

tk.Button(root, text="Add", command=add_student).grid(row=2, column=0)
tk.Button(root, text="Delete", command=delete_student).grid(row=2, column=1)
tk.Button(root, text="Export", command=export_students).grid(row=2, column=2)

search_e = tk.Entry(root)
search_e.grid(row=2, column=3)
tk.Button(root, text="Search", command=search_student).grid(row=2, column=4)

tree = ttk.Treeview(root, columns=labels, show="headings")
for col in labels:
    tree.heading(col, text=col)
    tree.column(col, width=150)
tree.grid(row=3, column=0, columnspan=5, sticky="nsew")

root.mainloop()