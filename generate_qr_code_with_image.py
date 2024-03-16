import os
import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageDraw, ImageTk

def generate_qr():
    input_data = data_entry.get()
    filename = filename_entry.get()
    qr_color = qr_color_entry.get() or "black"
    background_color = bg_color_entry.get() or "white"
    logo_path = logo_path_entry.get()
    save_path = save_path_entry.get() or os.getcwd()  # Default to current directory

    try:
        generate_qr_code(input_data, filename, qr_color, background_color, logo_path, save_path)
        messagebox.showinfo("QR Code Generated", f"QR code generated successfully as {os.path.join(save_path, filename)}")

        # Load and display the generated QR code in the UI window
        img = Image.open(os.path.join(save_path, filename))
        img = img.resize((300, 300), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        qr_label.config(image=img_tk)
        qr_label.image = img_tk
    except Exception as e:
        messagebox.showerror("Error", f"Error generating QR code: {str(e)}")

def generate_qr_code(input_data, filename, qr_color="black", background_color="white", logo_path=None, save_path="."):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Highest error correction level
        box_size=10,
        border=4,
    )
    qr.add_data(input_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=qr_color, back_color=background_color)

    if logo_path:
        logo = Image.open(logo_path)

        # Calculate the maximum size of the logo that fits within the QR code
        max_logo_size = min(img.size[0], img.size[1]) // 5

        # Resize the logo image while maintaining aspect ratio
        logo_aspect_ratio = logo.size[0] / logo.size[1]
        logo_width = max_logo_size
        logo_height = int(logo_width / logo_aspect_ratio)
        logo = logo.resize((logo_width, logo_height), Image.LANCZOS)

        # Creating a circular mask
        mask_size = (logo_width, logo_height)
        mask = Image.new("L", mask_size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, mask.size[0], mask.size[1]), fill=255)

        # Applying the circular mask and pasting logo
        img.paste(logo, ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2), mask=mask)

    img.save(os.path.join(save_path, filename))

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

logo_path_label = tk.Label(window, text="Logo image path (optional):")
logo_path_label.pack()
logo_path_entry = tk.Entry(window)
logo_path_entry.pack()

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
