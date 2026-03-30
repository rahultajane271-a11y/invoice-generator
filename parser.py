import pdfplumber
import tkinter as tk

pdf_path = "invoice.pdf"

def read_invoice():
    text = ""
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, text)

# Create window
window = tk.Tk()
window.title("Invoice Reader")
window.geometry("600x400")

# Button
read_button = tk.Button(window, text="Read Invoice", command=read_invoice)
read_button.pack(pady=10)

# Text box
output_box = tk.Text(window, height=20, width=70)
output_box.pack()

window.mainloop()