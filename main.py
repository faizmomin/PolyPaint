from PIL import Image

 # hi

# Create an Image object from an Image

imageObject  = Image.open("./whale.jpg")

 

# Crop the iceberg portion

cropped = imageObject.crop((100,30,400,300))

 

# Display the cropped portion

imageObject.show()