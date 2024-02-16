from PIL import Image

def get_atlas(path_tl, path_tr,path_bl,path_br, size):
    imtl = None
    if path_tl != '':
        imtl = Image.open(path_tl).convert('RGBA')
        imtl = imtl.resize((size//2, size//2))
    else:
        imtl = Image.new('RGBA', (size//2, size//2))
    
    imtr = None
    if path_tr != '':
        imtr = Image.open(path_tr).convert('RGBA')
        imtr = imtr.resize((size//2, size//2))
    else:
        imtr = Image.new('RGBA', (size//2, size//2))
    
    imbl = None
    if path_bl != '':
        imbl = Image.open(path_bl).convert('RGBA')
        imbl = imbl.resize((size//2, size//2))
    else:
        imbl = Image.new('RGBA', (size//2, size//2))
    
    imbr = None
    if path_br != '':
        imbr = Image.open(path_br).convert('RGBA')
        imbr = imbr.resize((size//2, size//2))
    else:
        imbr = Image.new('RGBA', (size//2, size//2))


    atlas = Image.new('RGBA', (size, size))
    atlas.paste(imtl, (0, 0))
    atlas.paste(imtr, (size//2, 0))
    atlas.paste(imbl, (0, size//2))
    atlas.paste(imbr, (size//2, size//2))
        
    return atlas