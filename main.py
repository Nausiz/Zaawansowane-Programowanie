import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'E:\Inne\Tesseract\tesseract'
print(pytesseract.image_to_string(r'C:\Users\marty\Desktop\zadanie9\text4.png'))