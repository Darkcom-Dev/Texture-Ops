from PIL import Image

def get_channel_mix(path_r, path_g, path_b, path_a, size):

    imr = None
    if path_r != '':
        imr = Image.open(path_r).convert('L')
        imr = imr.resize((size, size))
    else:
        imr = Image.new('L', (size, size), color=255)
    
    img = None
    if path_g != '':
        img = Image.open(path_g).convert('L')
        img = img.resize((size, size))
    else:
        img = Image.new('L', (size, size), color=255)
    
    imb = None
    if path_b != '':
        imb = Image.open(path_b).convert('L')
        imb = imb.resize((size, size))
    else:
        imb = Image.new('L', (size, size), color=255)

    ima = None
    if path_a != '':
        ima = Image.open(path_a).convert('L')
        ima = ima.resize((size, size))
    else:
        ima = Image.new('L', (size, size), color=255)
    """     
    imr = Image.open(path_r).convert('L')
    imr = imr.resize((size, size))
    img = Image.open(path_g).convert('L')
    img = img.resize((size, size))
    imb = Image.open(path_b).convert('L')
    imb = imb.resize((size, size))
    ima = Image.open(path_a).convert('L')
    ima = ima.resize((size, size))
 """
        
    return Image.merge('RGBA', (imr, img, imb, ima))

def get_channel_split(path, size):
    im = Image.open(path)
    im = im.resize((size, size))
    return im.getchannel('R'), im.getchannel('G'), im.getchannel('B'), im.getchannel('A')