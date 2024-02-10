from PIL import Image

def get_channel_mix(path_r, path_g, path_b, path_a, size):
    imr = Image.open(path_r).convert('L')
    imr = imr.resize((size, size))
    img = Image.open(path_g).convert('L')
    img = img.resize((size, size))
    imb = Image.open(path_b).convert('L')
    imb = imb.resize((size, size))
    ima = Image.open(path_a).convert('L')
    ima = ima.resize((size, size))

        
    return Image.merge('RGBA', (imr, img, imb, ima))
