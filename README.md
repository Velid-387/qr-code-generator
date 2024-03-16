# QR Code Generator Scripts
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

This repository contains two Python scripts for generating QR codes with various customization options.

## Script 1: QR Code Generator (With the image in the middle of the QR Code)

### Description
- This script generates a QR code with custom options such as QR code color, background color, and data input.
- Users can specify a filename (including extension) for the generated QR code.
- Optionally, users can choose the QR code color and background color, but also some image if he wants to have it in the middle of the QR Code. It just needs to provied a path to that image.
- The script provides an input field to enter the data for the QR code.
- Users can also specify a save path for the generated QR code. The default save path is the current directory of the script.
- The script uses the `qrcode` and `PIL` libraries for QR code generation and image processing.

### Usage
1. Run the script `generate_qr_code_with_image.py` in your Python environment.
2. Enter the data for the QR code, filename, QR code color, background color (optional), and save path (optional).
3. Click the "Generate QR Code" button to generate the QR code.
4. The generated QR code will be saved in the specified save path or the default directory.

## Script 2: QR Code Generator (Without the image in the middle of the QR Code)

### Description
- This script provides a graphical user interface (GUI) for generating QR codes with customizable options.
- Users can input data, specify a filename, choose QR code color, background color, and provide a logo image path.
- Additionally, users can specify a save path for the generated QR code. The default save path is the current directory of the script.
- The script uses the `tkinter`, `qrcode`, and `PIL` libraries for GUI creation, QR code generation, and image processing.

### Usage
1. Run the script `generate_qr_code.py` in your Python environment.
2. Enter the data, filename, QR code color, background color, logo image path (optional), and save path (optional) in the GUI.
3. Click the "Generate QR Code" button to generate the QR code.
4. The generated QR code will be displayed in the GUI window and saved in the specified save path or the default directory.

## Dependencies
- Python 3.x
- tkinter (for GUI)
- qrcode
- PIL (Python Imaging Library)

## Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/qr-code-generator.git
2. Navigate to the project directory:
   ```bash
    cd qr-code-generator
3. Create a virtual environment (optional but recommended):
   ```bash
    python -m venv venv
4. Activate the virtual environment:
- On Windows:
   ```bash
    venv\Scripts\activate
- On macOS/Linux:
   ```bash
    source venv/bin/activate
5. Install the required dependencies:
   ```bash
    pip install -r requirements.txt

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.
