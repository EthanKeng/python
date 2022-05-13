from PIL import Image
import os

path_to_image = 'images/'
image_files = [img for img in os.listdir(path_to_image) ]
# print(len(image_files))


for i in image_files:
  im = Image.open(os.path.join(path_to_image, i))

  im = im.rotate(angle=90).resize((128, 128)).convert('RGB')
#  im.show()
  print(im.format, im.size, im.mode)

  im.save(os.path.join("/opt/icons/",i),format="jpeg")
