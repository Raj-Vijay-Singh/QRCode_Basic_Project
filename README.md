This project is made by Raj Vijay Singh, pursuing his bachelor's degree in B. Tech AI & DS, 4th Semester from World College of Technology & Management in Fahrukhnagar.

This project utilises two different libraries to generate QR does.

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