from PIL import Image
import numpy as np
import noise
import time

def generate_seamless_texture(width, height, scale, octaves, persistence, lacunarity, seed):
    """
    Generate a seamless texture using simplex noise.

    Args:
        width (int): The width of the texture.
        height (int): The height of the texture.
        scale (float): The scaling factor for the noise.
        octaves (int): The number of octaves in the noise.
        persistence (float): The persistence of the noise.
        lacunarity (float): The lacunarity of the noise.
        seed (int): The seed for the noise generation.

    Returns:
        Image: The generated seamless texture as a PIL Image.
    """
    start_time = time.time()
    # Generar una matriz de ruido simplex
    noise_array = np.zeros((height, width))
    for y in range(height):
        for x in range(width):
            noise_array[y][x] = (noise.snoise2(x / scale, 
                                               y / scale, 
                                               octaves=octaves, 
                                               persistence=persistence, 
                                               lacunarity=lacunarity, 
                                               repeatx=width, 
                                               repeaty=height, 
                                               base=seed) + 1) * 127

    # Crear una imagen PIL desde la matriz de ruido
    end_time = time.time()
    print("Tiempo de ejecución:", end_time - start_time)
    return Image.fromarray(noise_array.astype(np.uint8))

""" 
start_time = time.time()
# Parámetros de generación de ruido simplex
width = 512
height = 512
scale = 100.0
octaves = 6
persistence = 0.5
lacunarity = 2.0
seed = 1

# Generar la textura seamless
seamless_texture = generate_seamless_texture(width, height, scale, octaves, persistence, lacunarity, seed)

# Guardar la textura
seamless_texture.save("seamless_texture_2.png")
end_time = time.time()
print("Tiempo de ejecución:", end_time - start_time)
 """


