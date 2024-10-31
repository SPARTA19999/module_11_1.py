from PIL import Image, ImageDraw, ImageFont

img = Image.open("tigr.jpg")
new_size = (1500, 1000)
resized_image = img.resize(new_size)
resized_image.save('resized_image.jpg')
draw = ImageDraw.Draw(resized_image)
font = ImageFont.truetype('arial.ttf', 70)
text = "Привет, мир!"
position = (150, 400)
text_color = (300, 155, 255)
draw.text(position, text, font=font, fill=text_color)
resized_image.save('tiger_with_text.jpg')
resized_image.show()
