import qrcode
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog

def generate_qr():
    input_data = data_entry.get()
    filename = filename_entry.get()
    qr_color = qr_color_entry.get() or "black"
    background_color = bg_color_entry.get() or "white"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(input_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=qr_color, back_color=background_color)
    img = img.resize((300, 300), Image.LANCZOS)  # Use LANCZOS for resizing
    img_tk = ImageTk.PhotoImage(img)

    qr_label.config(image=img_tk)
    qr_label.image = img_tk

    img.save(filename)
    tk.messagebox.showinfo("QR Code Generated", f"QR code generated successfully as {filename}")

def browse_save_path():
    directory = filedialog.askdirectory()
    save_path_entry.delete(0, tk.END)
    save_path_entry.insert(0, directory)

# Create main window
window = tk.Tk()
window.title("QR Code Generator")

# Create input fields
data_label = tk.Label(window, text="Data for QR code:")
data_label.pack()
data_entry = tk.Entry(window)
data_entry.pack()

filename_label = tk.Label(window, text="Filename (include extension):")
filename_label.pack()
filename_entry = tk.Entry(window)
filename_entry.pack()

qr_color_label = tk.Label(window, text="QR code color (default is black):")
qr_color_label.pack()
qr_color_entry = tk.Entry(window)
qr_color_entry.pack()

bg_color_label = tk.Label(window, text="Background color (default is white):")
bg_color_label.pack()
bg_color_entry = tk.Entry(window)
bg_color_entry.pack()

save_path_label = tk.Label(window, text="Save path (default is current directory):")
save_path_label.pack()
save_path_entry = tk.Entry(window)
save_path_entry.pack()

browse_save_path_button = tk.Button(window, text="Browse", command=browse_save_path)
browse_save_path_button.pack()

generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr)
generate_button.pack()

# QR code display
qr_label = tk.Label(window)
qr_label.pack()

# Run the GUI
window.mainloop()
