import os
from PIL import Image

base = """

define gui.textbox_height = 10

label start:

  scene black 

"""


for file in sorted(os.listdir("./images")):
	image = Image.open("./images/" + file)
	width, height = image.size
	
	#print "{} {} {}".format(file, width, height)


	if height > 800:
		base += """show {}:
    subpixel True
    yalign 0.0
    linear 10.0 yalign 1.0\n""\n\nhide {} \n\n""".format(file.split(".")[0], file.split(".")[0])
	else:
		base += "show {} at top\n\"\"\nhide {} \n\n".format(file.split(".")[0], file.split(".")[0])

script = open("script.rpy", "w")
script.write(base)
script.close()
