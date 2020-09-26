from PIL import Image

# Open up given image and calculate the height from the given `width` clue (304)
im = Image.open("input.jpg")

width = 304
height = int(im.width / width)

new = Image.new("RGB", (width, height))

for idx in range(width):
	# Crop image to get the current column (on its side)
	crop = im.crop((idx * height, 0, (idx + 1) * height, 1))

	# Rotate to make it a column and `expand=1` to adjust image size accordingly
	rotate = crop.rotate(-90, expand=1)

	# Add the column to the new image
	new.paste(rotate, (idx, 0))

# Save final result
new.save("output.png")