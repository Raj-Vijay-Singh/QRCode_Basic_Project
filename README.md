This project is made by Raj Vijay Singh, pursuing his bachelor's degree in B. Tech AI & DS, 4th Semester from World College of Technology & Management in Fahrukhnagar.

# Algorithm:
- Initialise a `user_choice` variable, with the value "y", that stores if the program should continue to run or not.
- Create function to generate QR code which asks user for data input and saves the QR Code with a timestamped file name.
- Run the function in a loop.
- At the end of each iteration, ask user input — if they want to generate another QR code (user_choice = "y") or exit (user_choice = "n")
- If user_choice = "n", exit. If user_choice = "y", continue loop. Otherwise, ask for input again.

This project utilises two different libraries to generate QR codes.
# Using PyQRCode Library
PyQRCode is a more lightweight and basic approach. It is entirely Python based. 

### Pros:
- Lightweight and faster.
- Supports SVG.

### Cons:
- Less customisation.
- Lack of custom colors.
- Only supports PNG and SVG formats.

# Using QRCode Library
QRCode is a better and more customisable approach to generating QR Codes.

### Pros:
- Custom colors.
- Supports multiple file formats like PNG, JPG and GIFs.
- Supports Logos.

### Cons:
- Lacks SVG support.
- A little slower than PyQRCode.

# Why Use Time Module?
I used time module to generate a unique name for each file. I did that by adding the timestamp of the file's creation time at the end of the file name.
This avoids any naming conflicts that might have risen. 

# How To Run?
Execute **main_qrcode.py** to generate QR code with the QRCode Library.

Execute **main_pyqrcode.py** to generate QR code with the PyQRCode Library.

## Requirements To Run
- Requires Python installed.
- Run in a virtual environment with the needed libraries (PyQRCode (with PyPNG), QRCode or both) installed.
  - Install using the commands:
    - `pip install pyqrcode, pypng` (for main_pyqrcode.py)
    - `pip install qrcode[pil]` (for main_qrcode.py)
- In the folder where the script is being run, there needs to be a folder named "QR_Codes" where the images will be saved.