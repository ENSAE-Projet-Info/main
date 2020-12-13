colour_dict = {'#FFFFFF' : 'Blanc',
              '#000000' : 'Noir',
              '#C0C0C0' : 'Gris',
              '#FF0000': 'Rouge',
              '#800000': 'Marron',
              '#FFFF00': 'Jaune',
              '#008000': 'Vert',
              '#00FFFF' : 'Cyan',
              '#0000FF' : 'Bleu',
              '#000061' : 'Bleu',
              '#800080' : 'Violet',
              '#ff00aa': 'Rose'}


str_to_var = {'pull': pull,
              'pantalon' : pantalon,
              'tshirt' : tshirt,
              'short' : short}
    

def closest_colour(requested_colour):
    """Prend en entré un triplet (r,g,b) correspondant au RGB d'un pixel d'une image,
    et renvoie la couleur la plus proche associée (distance euclidienne)
    
    Parameters
    ----------
    arg1 : tuple
        Triplet RGB (r,g,b) d'un pixel

    Returns
    -------
    str
        Couleur associé au pixel (choisi dans le dictionnaire colour_dict)
    
    """
    min_colours = {}
    for key, name in colour_dict.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def crop(image):
    """Prend en entrée une image au format PIL et renvoie la même image au même format, zoomée.
    
    Parameters
    ----------
    arg1 : PIL.JpegImagePlugin.JpegImageFile
        Image à zoomer

    Returns
    -------
    PIL.JpegImagePlugin.JpegImageFile
        Image zoomée
    
    
    """
    width, height = image.size 
    left = 50
    top = height / 4
    right = 150
    bottom = 3 * height / 4
    return(image.crop((left, top, right, bottom)))


def major_colour(image_matrix):
    """Prend en entrée un image RGB sous forme de matrice de dimension 3, calcule pour chaque pixel la couleur la plus proche
    (avec request_colour) et renvoie la couleur qui a le plus de pixel comptabilisés.
    
    Parameters
    ----------
    arg1 : numpy.ndarray
        Array numpy de dimension 3 : contient le code RGB de chaque pixel de l'image.

    Returns
    -------
    str
        Couleur majoritaire de l'image
    
    """
    colour_count = {'Blanc' :0,
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
            if image_matrix[i,j,0] == 255 and image_matrix[i,j,1] == 255 and image_matrix[i,j,2] == 255: #On ne compte pas le fond blanc
                pass
            else:
                colour_count[closest_colour(image_matrix[i,j,:])]+=1
    return(max(colour_count, key=lambda key: colour_count[key]))

def colour_repartition_mean(classe):
    """Prend une entrée un type de vetement au format str et renvoie la repartition de la couleur majoritaire pour chaque image
    du type de vêtement avec la méthode "mean".
    Méthode "mean" : étant donné une image, calcule la couleur la plus proche (distance euclidienne)
    de la moyenne RGB de tous les pixels
    
    Parameters
    ----------
    arg1 : str
        Nom de la classe (type d'habit) à analyser, au format str. Par exemple 'pull'

    Returns
    -------
    dict
        Dictionnaire dont les clés sont les couleurs, et les valeurs le nombre d'image ayant la couleur associé à la clé.
    
    """
    colour_count = {'Blanc' :0,
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
    vclasse = str_to_var[classe]
    for i in range(len(vclasse)):
    #Importation de l'image en rgb
        img = Image.open(path + '\\' + classe + '/' + vclasse[i])
        img_cropped = crop(img)
    
        M = np.array(img_cropped)
        if M.ndim==3:
            M = M.mean(axis=0).mean(axis=0)
            r,g,b = M[0], M[1], M[2]
            colour_count[str(closest_colour((r,g,b)))]+=1
        else:
            pass
    return(colour_count)

def colour_repartition_major(classe):
    """Prend une entrée un type de vetement au format str et renvoie la repartition de la couleur majoritaire pour chaque image
    du type de vêtement avec la méthode "major".
    Méthode "major" : la couleur d'un vêtement est donné par la fonction "major_colour" 
    
    Parameters
    ----------
    arg1 : str
        Nom de la classe (type d'habit) à analyser, au format str. Par exemple 'pull'

    Returns
    -------
    dict
        Dictionnaire dont les clés sont les couleurs, et les valeurs le nombre d'image ayant la couleur associé à la clé.
    """
    colour_count = {'Blanc' :0,
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
    vclasse = str_to_var[classe]
    for i in range(len(vclasse)):
    #Importation de l'image en rgb
        img = Image.open(path + '\\' + classe + '/' + vclasse[i])
        img_cropped = crop(img)
    
        M = np.array(img_cropped)
        if M.ndim==3:
            colour = major_colour(M)
            colour_count[colour]+=1
        else:
            pass
    return(colour_count)

def colour_repartition_cluster(classe, ncluster =5):
    """Prend une entrée un type de vetement au format str, et un nombre de cluster (par défaut 5)
    et renvoie la repartition de la couleur majoritaire pour chaque image du type de vêtement avec la méthode "cluster".
    Méthode cluster : Trouve la couleur majoritaire d'un vêtement avec la méthode des k-means
    
    Parameters
    ----------
    arg1 : str
        Nom de la classe (type d'habit) à analyser, au format str. Par exemple 'pull'

    Returns
    -------
    dict
        Dictionnaire dont les clés sont les couleurs, et les valeurs le nombre d'image ayant la couleur associé à la clé.
    """
    colour_count = {'Blanc' :0,
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
    vclasse = str_to_var[classe]
    for i in range(len(vclasse)):
    #Importation de l'image en rgb
        img = Image.open(path + '\\' + classe + '/' + vclasse[i])
        img_cropped = crop(img)
    
        #Test si l'image est en noir et blanc
        M = np.array(img_cropped)
        if M.ndim==3:
            shape = M.shape
            M = M.reshape(np.product(shape[:2]), shape[2]).astype(float)

            codes, dist = scipy.cluster.vq.kmeans(M, ncluster)
            vecs, dist = scipy.cluster.vq.vq(M, codes)        
            counts, bins = np.histogram(vecs, len(codes))    
            index_max = np.argmax(counts)                    
            peak = codes[index_max]
            colour_count[closest_colour((peak[0],peak[1],peak[2]))]+=1
        else:
            pass
    return(colour_count)
