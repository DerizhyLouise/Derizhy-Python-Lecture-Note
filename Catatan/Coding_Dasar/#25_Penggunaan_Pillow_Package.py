from PIL import Image

im = Image.open("JOKER.PNG")

print("Format file: " + im.format)
print("Ukuran file: " + str(im.size))
print("Mode file: " + im.mode)

im.show()