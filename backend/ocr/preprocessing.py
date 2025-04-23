from PIL import Image, ImageEnhance, ImageFilter

def preprocess_image(image):
    # Convert to grayscale
    image = image.convert("L")
    # Enhance the image
    image = image.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)
    return image
