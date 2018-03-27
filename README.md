# ComicToVisualNovel

This is the Linux distribution of a RenPy game that displays _The Best We Could Do_ as a visual novel.

## Description

I used https://github.com/Xonshiz/comic-dl to download the first thirty-ish pages of _The Best We Could Do_ from online. 

Then, I used an algorithm as feature here: https://github.com/mozillamonks/comicstrip which does its best to split a comic page into multiple dfferent panels. You can see the code which does this reproduced below

```python
import os

for file in os.listdir("./source"):
	os.system('python comicstrip.py -f ./source/{} --min-width=300 --min-height=300 --prefix=./output/{}'.format(file, file.split(".")[0],))

```

Then, I wrote some code which generates a script for the game which you can find in `game/scipt_generator.py`. It is also reproduced below

```python 
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
```

Simply put, it's a slightly more interactive slideshow of images. For images that are larger than the game window, the code will add a panning effect to the images. 

## Why Do This??

This was an attempt to show how the comic book medium interacts with the visual novel medium for the class _Graphic Asia_. If a significant more amount of time is placed into the development of this, you could hypothetically extract the text from each panel, and have it overlayed upon the comic as you read and interact with the material. You could detect the positive/negative sentiment of the text you extract, and change the color of the background which could add more mood to the scene, and much more. The possibilities are limitless 