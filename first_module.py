from PIL import Image
import os

file_names = []
out_size_128 = (128, 128)
fill_color = (120, 8, 220)

# It recursively passes through the folders and find files
for subdir, dirs, files in os.walk("images"):
    for file in files:
        filepath = subdir + os.sep + file
        file_names.append(filepath)
file_names.remove('images/.DS_Store')

for file in file_names:
    im = Image.open(file).convert("RGBA")  # it had mode P after DL it from OP
    if im.mode in ('RGBA', 'LA'):
        background = Image.new(im.mode[:-1], im.size, fill_color)  # im.thumbnail(out_size_128)
        background.paste(im, im.split()[-1])  # omit transparency
        im = background
        im.rotate(90).convert("RGB").resize(out_size_128).save(file + ".jpg", "JPEG")
