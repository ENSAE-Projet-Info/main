colour_dict = {'#FFFFFF': 'Blanc',
               '#000000': 'Noir',
               '#C0C0C0': 'Gris',
               '#FF0000': 'Rouge',
               '#800000': 'Marron',
               '#FFFF00': 'Jaune',
               '#008000': 'Vert',
               '#00FFFF': 'Cyan',
               '#0000FF': 'Bleu',
               '#000061': 'Bleu',
               '#800080': 'Violet',
               '#ff00aa': 'Rose'}

str_to_var = {'pull': pull,
              'pantalon': pantalon,
              'tshirt': tshirt,
              'short': short}


def closest_colour(requested_colour):
    """Prend en entré un triplet (r,g,b) correspondant au RGB d'un pixel d'une image,
    et renvoie la couleur la plus proche associée (distance euclidienne)"""
    min_colours = {}
    for key, name in colour_dict.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def crop(image):
    """Prend en entrée une image au format PIL et renvoie la même image au même format, zoomée."""
    width, height = image.size
    left = 50
    top = height / 4
    right = 150
    bottom = 3 * height / 4
    return (image.crop((left, top, right, bottom)))


def major_colour(image_matrix):
    """Prend en entrée un image RGB sous forme de matrice de dimension 3, calcule pour chaque pixel la couleur la plus proche
    (avec request_colour) et renvoie la couleur qui a le plus de pixel comptabilisés."""
    colour_count = {'Blanc': 0,
                    'Noir': 0,
                    'Gris': 0,
                    'Rouge': 0,
                    'Marron': 0,
                    'Jaune': 0,
                    'Vert': 0,
                    'Cyan': 0,
                    'Bleu': 0,
                    'Violet': 0,
                    'Rose': 0}
    for i in range(image_matrix.shape[0]):
        for j in range(image_matrix.shape[1]):
            if image_matrix[i, j, 0] == 255 and image_matrix[i, j, 1] == 255 and image_matrix[
                i, j, 2] == 255:  # On ne compte pas le fond blanc
                pass
            else:
                colour_count[closest_colour(image_matrix[i, j, :])] += 1
    return (max(colour_count, key=lambda key: colour_count[key]))