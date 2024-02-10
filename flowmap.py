from PIL import Image
import numpy as np


def get_flowmap(path):
# Open grayscale image to numpy array
    im = Image.open(path).convert('RGB')
    size = im.size
    matrix = np.array(im)


    # Restar el valor del pixel actual con el pixel anterior y sumar 128 entre columnas
    column_flows = np.diff(matrix, axis=1) + 128
    last_column = matrix[:, 0] - matrix[:, -1] + 128
    column_flows = np.insert(column_flows, column_flows.shape[1], last_column, axis=1)
    # Restar el valor del pixel actual con el pixel anterior y sumar 128 entre filas
    row_flows = np.diff(matrix, axis=0) + 128
    last_row = matrix[0, :] - matrix[-1, :] + 128
    row_flows = np.insert(row_flows, row_flows.shape[0], last_row, axis=0)

    matrix[:, :, 0] = row_flows[:, :, 0]
    matrix[:, :, 1] = column_flows[:, :, 1]

    # Create new image from matrix
    return Image.fromarray(matrix)
    # im2.save('flow_tuerca.png')
