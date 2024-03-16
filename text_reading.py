from PIL import Image
import pytesseract

img=Image.open("D:\opencv_udemy/12_text_reading/text.png")

text=pytesseract.image_to_string(img,lang="eng")
print(text)
