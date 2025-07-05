from PIL import Image
import numpy as np

# a small set of ascii chars from dark to light
ASCII_CHARS = "@%#*+=-:. "

def to_ascii(img, new_width=80):
    """
    Convert a BGR image (numpy array) to grayscale ASCII art string.
    """
    # convert to PIL grayscale
    pil = Image.fromarray(img[..., ::-1]).convert("L")
    width, height = pil.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    pil = pil.resize((new_width, new_height))
    pixels = np.array(pil)
    # map each pixel to a char
    chars = [ASCII_CHARS[pix * len(ASCII_CHARS) // 256] for pix in pixels.flatten()]
    # build the string
    lines = [
        "".join(chars[i : i + new_width])
        for i in range(0, len(chars), new_width)
    ]
    return "\n".join(lines)
