from PIL import Image

def get_atlas(path_tl, path_tr,path_bl,path_br, size):
    imtl = Image.open(path_tl).convert('RGBA')
    imtl = imtl.resize((size//2, size//2))
    imtr = Image.open(path_tr).convert('RGBA')
    imtr = imtr.resize((size//2, size//2))
    imbl = Image.open(path_bl).convert('RGBA')
    imbl = imbl.resize((size//2, size//2))
    imbr = Image.open(path_br).convert('RGBA')
    imbr = imbr.resize((size//2, size//2))

    atlas = Image.new('RGBA', (size, size))
    atlas.paste(imtl, (0, 0))
    atlas.paste(imtr, (size//2, 0))
    atlas.paste(imbl, (0, size//2))
    atlas.paste(imbr, (size//2, size//2))
        
    return atlas