import qrcode
import time

user_choice = "y"

def generate_qr_code():
    data = input("Enter your data or URL: ")
    qr = qrcode.make(data)
    qr_img_name = f"qr_code_{int(time.time())}.png"

    qr.save(f"QR_Codes/{qr_img_name}")
    print(f"\nYour QR Code is successfully generated!\n"
          f"It is saved in the QR_Codes folder.\n"
          f"Name of your QR_Code: {qr_img_name}\n")

while user_choice == "y":
    generate_qr_code()
    user_choice = ""
    while user_choice not in ("y", "n"):
        user_choice = input("Do you want to generate another qr_code? (y/n): ").lower()

print("Exiting program...")


