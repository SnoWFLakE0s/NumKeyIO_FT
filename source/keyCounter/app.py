import tkinter as tk
from tkinter import *
import os
from tkinter.filedialog import Directory

root = tk.Tk()
root.title("SnoW Variable Package Installer v0.1")
root.resizable(width=False, height=False)

frm_main = tk.Frame(master=root, bg="#2f3136", padx=20, pady=20)

frm_selectFile = tk.Frame(master=frm_main, bg="#2f3136")
frm_selectFile.grid(row=0, column=0, sticky="news")
btn_selectFile = tk.Button(master=frm_selectFile, text="Select Aircraft File", padx=10, pady=5, width=20, bg="#375a7f", fg="white")
btn_selectFile.grid(row=0, column=0)
ent_fileDirectory = tk.Entry(master=frm_selectFile, width=75, bg="white")
ent_fileDirectory.insert(0, "File Directory")
ent_fileDirectory.grid(row=0, column=1, sticky="news", padx=(10,0))

frm_installPackage = tk.Frame(master=frm_main, bg="#2f3136")
frm_installPackage.grid(row=1, column=0, sticky="news")
btn_installPackage = tk.Button(master=frm_installPackage, text="Install Variable Package", padx=10, pady=5, width=20, bg="#375a7f", fg="white")
btn_installPackage.grid(row=0, column=0)
lbl_status = tk.Label(master=frm_installPackage, text="Installation Status: Pending", pady=5, width=64, bg="#2f3136", fg="white")
lbl_status.grid(row=0, column=1, sticky="news", padx=(10,0))

frm_footer = tk.Frame(master=frm_main, bg="#2f3136")
frm_footer.grid(row=2, column=0, sticky="news")
lbl_footer = tk.Label(master=frm_footer, text="Published under MIT License\nMade by Joshua \"SnoWFLakE0s\" Eah, 2021\nVersion 0.1 Alpha", bg="#2f3136", fg="white")
lbl_footer.pack(pady=(20,0))

frm_main.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

root.mainloop()