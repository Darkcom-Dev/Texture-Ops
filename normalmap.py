from PIL import Image
import numpy as np

def grayscale_to_normalmap(img):
    # Convertir la imagen a un arreglo numpy
    img_array = np.array(img)
    
    # Calcular las derivadas parciales en x y y
    dx, dy = np.gradient(img_array)
    
    # Calcular el vector normal
    normal_map = np.dstack((-dx, -dy, np.ones_like(img_array)))
    
    # Normalizar el vector normal
    norm = np.sqrt(np.sum(normal_map ** 2, axis=2, keepdims=True))
    normal_map /= norm
    
    # Escalar los valores al rango 0-255
    normal_map = ((normal_map + 1) * 127.5).astype(np.uint8)
    
    # Crear una imagen desde el array de numpy
    normal_img = Image.fromarray(normal_map)
    
    return normal_img


from PIL import Image
import numpy as np

def normalmap_to_grayscale(normal_img):
    # Convertir la imagen a un arreglo numpy
    normal_map = np.array(normal_img)
    
    # Escalar los valores de píxel al rango -1 a 1
    normal_map = (normal_map / 255) * 2 - 1
    
    # Calcular la magnitud del vector normal
    intensity = np.sqrt(np.sum(normal_map ** 2, axis=2))
    
    # Escalar los valores de intensidad al rango 0-255
    intensity = ((intensity - intensity.min()) / (intensity.max() - intensity.min())) * 255
    
    # Crear una imagen en escala de grises desde el array de numpy
    grayscale_img = Image.fromarray(intensity.astype(np.uint8))
    
    return grayscale_img


