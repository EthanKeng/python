from PIL import Image
import os

path_to_image = 'supplier-data/images/'
image_files = [img for img in os.listdir(path_to_image) if img.endswith("tiff") ]
# print(len(image_files))


for i in image_files:
  im = Image.open(os.path.join(path_to_image, i))

  im = im.rotate(angle=90).resize((600, 400)).convert('RGB')
#  im.show()

  im.save(os.path.join("supplier-data/images/",i.replace("tiff","jpeg")),format="jpeg")
  print(im.format, im.size, im.mode)