from PIL import Image, ImageEnhance, ImageOps

cat = Image.open("cat-test.jpeg")
bw_cat = cat.convert("L")

bw_cat.save("bw_cat.jpg")

with Image.open("bw_cat.jpg") as img:
    img = ImageOps.mirror(img)
    img.save("img.jpg")