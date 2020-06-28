from PIL import Image
import glob
import os

file_names = []
out_size_128 = (128,128)
fill_color = (120,8,220)


# It recursively passes through the folders and find files
for subdir, dirs, files in os.walk("images"):
    for file in files:
        filepath = subdir + os.sep + file
        file_names.append(filepath)
file_names.remove('images/.DS_Store')


for file in file_names:
    im = Image.open(file).convert("RGB")
    im.thumbnail(out_size_128)
    print(im.size,im.format)
    im.rotate(270).save(file+".jpg", "JPEG")



