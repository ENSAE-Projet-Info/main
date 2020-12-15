import pandas as pd
import seaborn as sns
import numpy as np
import scipy
import matplotlib.pyplot as plt
import os
import cv2 as cv
from PIL import Image
import webcolors
import random

from utils.desc_stats.vars import *

def first_stats():
    """Indique le nombre de vêtements dans chaque classe ainsi que le pourcentage entre parenthèse, et qui trace un histogramme de la
    taille de chaque fichier
    
    Paramètre
    ----------
    None
    Retours
    -------
    None
        
    
    """
    size = []
    for classe in ['pull', 'tshirt', 'pantalon', 'short']:
        for i in range(len(vars()[classe])):
                img = Image.open(path + '//' + classe + '/' + vars()[classe][i])
                size.append(os.path.getsize(path + '/' + classe + '/' + vars()[classe][i]))
    plt.title('Distribution de la taille de chaque fichier du dataset')
    sns.distplot(size)
    print('Il y a {} pulls ({}%), {} t-shirt ({}%), {} pantalons ({}%) et {} shorts ({}%) dans la base de données.'.format(len(pull),
                                                                                               round(len(pull)/len(pull+tshirt+pantalon+short) * 100,2),
                                                                                               len(tshirt),
                                                                                               round(len(tshirt)/len(pull+tshirt+pantalon+short) * 100,2),
                                                                                               len(pantalon),
                                                                                               round(len(pantalon)/len(pull+tshirt+pantalon+short) * 100,2),
                                                                                               len(short),
                                                                                               round(len(short)/len(pull+tshirt+pantalon+short) * 100,2)))

    
def two_random_images(classe):
    """Affiche deux images aléatoires de la classe "classe"
    
    Paramètre
    ----------
    classe : str
        Classe de vêtements dont on veut afficher deux images
    Retours
    -------
    None
        Deux images aléatoires de la classe "classe"
        
    """
    image1 = Image.open(path + '//' + classe + '/' + vars()[classe][random.choice(range(len(vars()[classe])))])
    image2 = Image.open(path + '//' + classe + '/' + vars()[classe][random.choice(range(len(vars()[classe])))])
    plt.imshow(image1)
    plt.show()
    plt.imshow(image2)
    plt.show()
    

def pie_chart_categories() :
    """Affiche le pie chart de la distribution des catégories de vêtements (avec les paramètres pré-calculés).
    Paramètres
    ----------
    None
    Retours
    -------
    None
        Un pie chart de la distribution des catégories de vêtements
 
    """
    n_tshirt = len(tshirt)
    n_pull = len(pull)
    n_pantalon = len(pantalon)
    n_short = len(short)
    n_all = n_tshirt + n_pull + n_pantalon + n_short
    pct_tshirt = n_tshirt/n_all
    pct_pull = n_pull/n_all
    pct_pantalon = n_pantalon/n_all
    pct_short = n_short / n_all
    labels = ['T-shirt','Pull', 'Pantalon', 'Short']
    sizes = [60,20,10,10]
    explode = (0.05, 0.05,0.05,0.05)
    colors = ['Wheat','PowderBlue','LightPink','MediumAquaMarine']
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',shadow=True, startangle=90)# Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    plt.title("Répartition des catégories de vêtements", fontsize=16)
    plt.tight_layout()
    plt.show()

def pie_chart_fond_blanc (path=path) :
    """Affiche le pie chart de la distribution des images sur fond blanc (avec les paramètres pré-calculés).
    
    Paramètres
    ----------
    None
    
    Retours
    -------
    None
        Un pie chart de la distribution des images sur fond blanc
 
    """
    import matplotlib.pyplot as plt
    labels = ['Fond Blanc', 'Reste']
    sizes = [86, 14]
    explode = (0.1, 0)
    colors = ['Lavender','#66b3ff']
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',shadow=True, startangle=90)# Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    plt.title("Répartition des fonds de photos", fontsize=16)
    plt.tight_layout()
    plt.show()
    
def pie_chart_logo () :
    """Affiche le pie chart de la distribution des T-shirts à logos (avec les paramètres pré-calculés).
    
    Paramètre
    ----------
    None
    
    Retours
    -------
    None
        Un pie chart de la distribution des T-shirts à logo
 
    """
    import matplotlib.pyplot as plt
    # Pie chart
    labels = ['Logo', 'Unicolore']
    sizes = [65.02, 100-65.02]
    explode = (0.1, 0)
    colors = ['Coral','LightPink']
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',shadow=True, startangle=90)# Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    plt.title("Répartition des types de T-shirts", fontsize=16)
    plt.tight_layout()
    plt.show()

def pie_chart_human_model () :
    """Affiche le pie chart de la distribution des vêtements portés par des humains (avec les paramètres pré-calculés).
    
    Paramètre
    ----------
    None
    
    Retours
    -------
    None
        Un pie chart de la distribution des vêtements portés par des humains
 
    """
    import matplotlib.pyplot as plt
    labels = ['Humain', 'Non-humain']
    sizes = [65.02, 100-65.02]
    explode = (0.1, 0)
    colors = ['AquaMarine','Khaki']
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',shadow=True, startangle=90)# Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    plt.title("Distribution des habits portés par des modèles humains", fontsize=16)
    plt.tight_layout()
    plt.show()
    
def closest_colour(requested_colour):
    """Prend en entré un triplet (r,g,b) correspondant au RGB d'un pixel d'une image,
    et renvoie la couleur la plus proche associée (distance euclidienne)
    
    Paramètre
    ----------
    requested_colour : tuple
        Triplet RGB (r,g,b) d'un pixel
    Retour
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
    
    Paramètre
    ----------
    image : PIL.JpegImagePlugin.JpegImageFile
        Image à zoomer
    Retour
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
    
    Paramètre
    ----------
    image_matrix : numpy.ndarray
        Array numpy de dimension 3 : contient le code RGB de chaque pixel de l'image.
    Retour
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

def colour_repartition_mean(classe, percentage=1):
    """Prend une entrée un type de vetement au format str et renvoie la repartition de la couleur majoritaire pour chaque image
    du type de vêtement avec la méthode "mean".
    Méthode "mean" : étant donné une image, calcule la couleur la plus proche (distance euclidienne)
    de la moyenne RGB de tous les pixels
    
    Paramètres
    ----------
    classe : str
        Nom de la classe (type d'habit) à analyser, au format str. Par exemple 'pull'
    percentage : float
        Pourcentage de la classe que l'on charge. Doit être très petit lorsque l'on veut voir comment le programme fonctionne,
        car ce dernier est très long. Vaut 1 par défaut
    Retour
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
    for i in range(percentage * len(vars()[classe])):
    #Importation de l'image en rgb
        img = Image.open(path + '//' + classe + '/' + vars()[classe][i])
        img_cropped = crop(img)
    
        M = np.array(img_cropped)
        if M.ndim==3:
            M = M.mean(axis=0).mean(axis=0)
            r,g,b = M[0], M[1], M[2]
            colour_count[str(closest_colour((r,g,b)))]+=1
        else:
            pass
    return(colour_count)

def colour_repartition_major(classe, percentage=1):
    """Prend une entrée un type de vetement au format str et renvoie la repartition de la couleur majoritaire pour chaque image
    du type de vêtement avec la méthode "major".
    Méthode "major" : la couleur d'un vêtement est donné par la fonction "major_colour" 
    
    Paramètres
    ----------
    classe : str
        Nom de la classe (type d'habit) à analyser, au format str. Par exemple 'pull'
    percentage : float
        Pourcentage de la classe que l'on charge. Doit être très petit lorsque l'on veut voir comment le programme fonctionne,
        car ce dernier est très long. Vaut 1 par défaut
    Retour
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
    for i in range(percentage * len(vars()[classe])):
    #Importation de l'image en rgb
        img = Image.open(path + '//' + classe + '/' + vars()[classe][i])
        img_cropped = crop(img)
    
        M = np.array(img_cropped)
        if M.ndim==3:
            colour = major_colour(M)
            colour_count[colour]+=1
        else:
            pass
    return(colour_count)

def colour_repartition_cluster(classe, percentage = 1, ncluster =5):
    """Prend une entrée un type de vetement au format str, et un nombre de cluster (par défaut 5)
    et renvoie la repartition de la couleur majoritaire pour chaque image du type de vêtement avec la méthode "cluster".
    Méthode cluster : Trouve la couleur majoritaire d'un vêtement avec la méthode des k-means
    
    Paramètres
    ----------
    classe : str
        Nom de la classe (type d'habit) à analyser, au format str. Par exemple 'pull'
    percentage : float
        Pourcentage de la classe que l'on charge. Doit être très petit lorsque l'on veut voir comment le programme fonctionne,
        car ce dernier est très long. Vaut 1 par défaut
    ncluster : int
        Nombre de clusters k-means. Vaut 5 par défaut
        
    Retour
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
    for i in range(percentage * len(vars()[classe])):
    #Importation de l'image en rgb
        img = Image.open(path + '//' + classe + '/' + vars()[classe][i])
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


  
  
def colour_mean(img_jpg) :
    """ Transforme chaque pixel de l'image initiale par sa "moyenne". La moyenne est faite sur sa propre couleur et sur celle de ses 8 pixels adjacents.
    Similaire au flou gaussien.
    
    Paramètres
    ----------
    img_jpg : Image
        Image d'entrée au format RGB.
        
    Retours
    ----------
    Image
        Renvoie l'image transformée.
    """
    img_arr = img_to_array(img_jpg)
    n = len(img_arr)
    m = len(img_arr[0])
    M= np.zeros([n,m,3])
    for i in range(1, n-1):  
        M[i,0] = img_arr[i,0]
        M[i,m-1] = img_arr[i,m-1] #On n'applique pas la moyenne aux bords, on considère qu'on peut les ignorer.
        for j in range(1,m-1) :
            M[0,j] = img_arr[0,j]
            M[n-1,j] = img_arr[n-1,j]   
            rgb_ij = [] #Couleurs rgb du pixel i,j de l'image en sortie
            for k in range(3):
                mean_k = float(int(1/9*(int(img_arr[i,j,k]) + int(img_arr[i-1,j,k]) + int(img_arr[i-1,j-1,k] )+ int(img_arr[i-1,j+1,k]) + int(img_arr[i,j-1,k]) + int(img_arr[i,j+1,k]) + int(img_arr[i+1,j-1,k]) + int(img_arr[i+1,j,k]) + int(img_arr[i+1,j+1,k]))))
                rgb_ij.append(mean_k)  
            M[i,j,:]= rgb_ij
        img_mean = array_to_img(M)
    return img_mean




def colour_var(img_jpg) :
    """ Transforme chaque pixel de l'image initiale par sa "variance". La variance calcule l'écart quadratique entre la couleur du pixel et sa moyenne.
    
    Paramètres
    ----------
    img_jpg : Image
        Image d'entrée au format RGB.
        
    Retours
    ----------
    Image
        Renvoie l'image transformée.
    """
    img_arr = img_to_array(img_jpg)
    img_mean = colour_mean(img_jpg)
    img_mean_arr = img_to_array(img_mean)
    img_var_arr = abs((img_arr - img_mean_arr))*1.2 #On rajoute un coefficient de façon à "accentuer" la variance. Ce ne sera donc pas la "vraie" variance, mais peu importe pour notre utilisation.
    img_var = array_to_img(img_var_arr)
    return img_var




def is_logo(img_jpg):    
    """Détecte si un t-shirt comporte un logo. Utilise une technique de détection par la variance.
    
    Paramètres
    ----------
    img_jpg : Image
        Image d'un T-shirt, au format RGB.
        
    Retours
    ----------
    bool
        Renvoie un booléen : 1 si le T-shirt comporte un logo, 0 sinon.
    """
    img_arr = img_to_array(img_jpg)
    n = len(img_arr)
    m = len(img_arr[0])
    #Ci-dessous : les pourcentages de zoom que l'on souhaite pour couper l'image en haut, en bas, à gauche et à droite pour centrer la photo sur le t-shirt.
    #Les valeurs ont été choisies arbitrairement.
    zoom_y_haut = 0.078125
    zoom_y_bas = 0.9765625
    zoom_x_gauche = 0.25390625
    zoom_x_droite = 0.68359375
    #Ci-dessous : les abscisses et ordonnées délimitant la nouvelle image zoomée.
    n_0 = int(n*zoom_y_haut) 
    n_1 = int(n*zoom_y_bas)
    m_0 = int(m*zoom_x_gauche)
    m_1 = int(m*zoom_x_droite)
        
    img_arr_zoom =img_arr[n_0:n_1,m_0:m_1,:]
    img_zoom = array_to_img(img_arr_zoom)

    img_var = colour_var(img_zoom) #image des variances
    img_var_arr = img_to_array(img_var)
    score0 = img_var_arr[:,:,0].sum() #somme des variances
    score1 = img_var_arr[:,:,1].sum()
    score2 = img_var_arr[:,:,2].sum()
    score = log(score0 + score1 + score2) #Logarithme pour "aplatir" les scores, qui sont immenses et peu commodes à comparer.        
    if score>12.55 :
        return 1
    else :
        return 0




def is_logo_feedback(img_jpg):    
    """Fonction is_logo enrichie d'un retour à l'utilisateur. Imprime l'image obtenue par la technique de variance. 
    Détecte si un t-shirt comporte un logo. Utilise une technique de détection par la variance.
    
    Paramètres
    ----------
    img_jpg : Image
        Image d'un T-shirt, au format RGB.
        
    Retours
    ----------
    bool
        Renvoie un booléen : 1 si le T-shirt comporte un logo, 0 sinon.
    float
        Renvoie le "score" de variance. Il a été choisi arbitrairement qu'un score supérieur à 12.6 signifiait qu'un t-shirt comportait un logo.
    """
    img_arr = img_to_array(img_jpg)
    n = len(img_arr)
    m = len(img_arr[0])
    #Ci-dessous : les pourcentages de zoom que l'on souhaite pour couper l'image en haut, en bas, à gauche et à droite pour centrer la photo sur le t-shirt.
    #Les valeurs ont été choisies arbitrairement.
    zoom_y_haut = 0.078125
    zoom_y_bas = 0.9765625
    zoom_x_gauche = 0.25390625
    zoom_x_droite = 0.68359375
    #Ci-dessous : les abscisses et ordonnées délimitant la nouvelle image zoomée.
    n_0 = int(n*zoom_y_haut) 
    n_1 = int(n*zoom_y_bas)
    m_0 = int(m*zoom_x_gauche)
    m_1 = int(m*zoom_x_droite)
        
    img_arr_zoom =img_arr[n_0:n_1,m_0:m_1,:]
    img_zoom = array_to_img(img_arr_zoom)

    img_var = colour_var(img_zoom) #image des variances
    img_var_arr = img_to_array(img_var)
    score0 = img_var_arr[:,:,0].sum() #somme des variances
    score1 = img_var_arr[:,:,1].sum()
    score2 = img_var_arr[:,:,2].sum()
    score = log(score0 + score1 + score2) #Logarithme pour "aplatir" les scores, qui sont immenses et peu commodes à comparer.
    
    plt.imshow(img_jpg)
    plt.show()
    plt.imshow(img_var)
    plt.show()
    if score>12.55 :
        print("LOGO. Score :",score)
        return (1,score)
    else :
        print("PAS DE LOGO. Score :",score)
        return (0,score)

    

    
def is_white(pixel, threshold=245, dist=5):
    """Détecte si un pixel est blanc (ou assez proche du blanc, selon un certain threshold et une certaine distance) ou non.
    
    Paramètres
    ----------
    pixel : list
        Un pixel donné, au format r,g,b (donc une liste de longueur 3).
    threshold : int
        Threshold pour la limite du blanc.
    dist : int
        Distance pour la limite du blanc.
        
    Retours
    ----------
    bool
        Renvoie un booléen : 1 si le pixel est blanc, 0 sinon.
    """
    r,g,b = pixel
    if (r>threshold)& (g>threshold)& (b>threshold)& (np.abs(r-g)<dist)& (np.abs(r-b)<dist)& (np.abs(g-b)<dist) : 
        return True
    else :
        return False



    
def white_percentage(img_jpg,threshold=245, dist=5) :
    """Donne le pourcentage de pixels blanc (selon une certaine notion de distance et un certain threshold) d'une image.
    
    Paramètres
    ----------
    img_jpg : Image
        Image d'entrée au format RGB.
    threshold : int
        Threshold pour la limite du blanc.
    dist : int
        Distance pour la limite du blanc.
        
    Retours
    ----------
    float
        Renvoie le pourcentage de blanc de l'image d'entrée.
    """
    img_arr = img_to_array(img_jpg)
    compteur = 0
    n = len(img_arr)
    m = len(img_arr[0])
    taille_img = n*m
    for i in range(n) :
        for j in range(m) :
            pixel = img_arr[i,j,:]
            ij_is_white = is_white(pixel,threshold,dist) #booléen
            if ij_is_white == 1 :
                compteur +=1
    return compteur/taille_img*100




def white_to_grey(img_jpg,threshold=245, dist=5):
    """Transforme tous les pixel considérés comme blancs (selon une certaine notion de distance et un certain threshold) en pixels gris.
    
    Paramètres
    ----------
    img_jpg : Image
        Image d'entrée au format RGB.
    threshold : int
        Threshold pour la limite du blanc.
    dist : int
        Distance pour la limite du blanc.
        
    Retours
    ----------
    Image
        Renvoie l'image d'entrée dont le blanc est converti en gris.
    """
    img_arr= img_to_array(img_jpg)
    n = len(img_arr)
    m = len(img_arr[0])
    img_corrigee_arr = np.zeros([n,m,3])
    for i in range(n) :
        for j in range(m) :
            pixel= img_arr[i,j,:]
            if is_white(pixel, threshold, dist) ==1 :
                pixel = [125.,125.,125.]
            img_corrigee_arr[i,j,:]= pixel
        img_corrigee = array_to_img(img_corrigee_arr)
    return img_corrigee




def is_white_background(img_jpg,threshold=245, dist=5, percentage=30) :
    """Détermine si le fond d'une image est blanc ou non.
    
    Paramètres
    ----------
    img_jpg : Image
        Image d'entrée au format RGB.
    threshold : int
        Threshold pour la limite du blanc.
    dist : int
        Distance pour la limite du blanc.
    percentage : int
        Pourcentage de blanc de l'image à partir duquel on considère que l'image est effectivement sur fond blanc.
        
    Retours
    ----------
    bool
        Renvoie un booléen : 1 si le fond est blanc, 0 sinon.
    """
    return white_percentage(img_jpg,threshold=245, dist=5) > percentage




def is_white_background_feedback(img_jpg,threshold=245, dist=5, percentage=30) :
    """Fonction is_white_background enrichie d'un retour à l'utilisateur. Dans le cours de la fonction, imprime l'image d'entrée, l'image d'entrée dont les pixels blancs ont été grisés.
    Détermine si le fond d'une image est blanc ou non.
    
    Paramètres
    ----------
    img_jpg : Image
        Image d'entrée au format RGB.
    threshold : int
        Threshold pour la limite du blanc.
    dist : int
        Distance pour la limite du blanc.
    percentage : int
        Pourcentage de blanc de l'image à partir duquel on considère que l'image est effectivement sur fond blanc.
        
    Retours
    ----------
    bool
        Renvoie un booléen : 1 si le fond est blanc, 0 sinon.
    float
        Pourcentage de pixels blancs de la photo.
    """
    plt.imshow(img_jpg)
    plt.show()
    plt.imshow(white_to_grey(img_jpg))
    plt.show()
    white_percent = white_percentage(img_jpg,threshold=245, dist=5)
    if white_percent > percentage :
        print("FOND BLANC. Pourcentage de pixels blancs : ", white_percent)
        return (1, white_percent )
    else :
        print("PAS DE FOND BLANC. Pourcentage de pixels blancs : ",white_percent)
        return (0, white_percent )
    


    
def is_human_model(path, limit_percent=95) :
    """Détermine si un vêtement est porté par un humain ou non.
    
    Paramètres
    ----------
    path : str
        Le chemin d'une photo.
    limit_percentage : int
        Pourcentage minimal à partir duquel on considère que le sujet de la photo est humain.
    
    Retours
    ----------
    list
        Retourne une liste dont le premier argument est un booléen : True si le vêtement est porté par un modèle humain, False sinon ; le second argument est le pourcentage de certitude de l'algorithme.
    """
    detectedImage, detections = detector.detectObjectsFromImage(output_type="array",input_image=path,minimum_percentage_probability =-1)
    convertedImage = cv2.cvtColor(detectedImage, cv2.COLOR_RGB2BGR)
    
    if detections ==[] :
        return (False)
    max_percent = max([detections[i]['percentage_probability'] for i in range(len(detections))]) #plusieurs objets peuvent être détectés 
    if max_percent > limit_percent :
        return(True)
    else :
        return(False)

    
    
    
def is_human_model_feedback(path, limit_percent=95) :
    """Fonction is_human_model enrichie d'un retour à l'utilisateur. Imprime l'image analysée par l'algorithme d'opencv.        
    Détermine si un vêtement est porté par un humain ou non.
    
    Paramètres
    ----------
    path : str
        Le chemin d'une photo.
    limit_percentage : int
        Pourcentage minimal à partir duquel on considère que le sujet de la photo est humain.
    
    Retours
    ----------
    list
        Retourne une liste dont le premier argument est un booléen : True si le vêtement est porté par un modèle humain, False sinon ; le second argument est le pourcentage de certitude de l'algorithme.
    float
        Pourcentage de certitude avec lequel l'algorithme estime que l'image en question contient un humain.
    """
   
    detectedImage, detections = detector.detectObjectsFromImage(output_type="array",input_image=path,minimum_percentage_probability =-1)
    convertedImage = cv2.cvtColor(detectedImage, cv2.COLOR_RGB2BGR)

    img2 = convertedImage[:,:,::-1]
    plt.imshow(img2)
    plt.show()
    if detections ==[] :
        print("NON-HUMAIN. Pourcentage obtenu par l'algorithme :   < 50%")
        return (False, "< 50 %")    
    max_percent = max([detections[i]['percentage_probability'] for i in range(len(detections))]) #plusieurs objets peuvent être détectés 
    if max_percent > limit_percent :
        print("HUMAIN. Pourcentage obtenu par l'algorithme : ", max_percent)
        return(True, max_percent)
    else :
        print("NON-HUMAIN. Pourcentage obtenu par l'algorithme : ", max_percent)
        return(False, max_percent)
    
    
    
def percentage_true(data_img, bool_function) :
    """Applique une fonction booléenne (agissant sur une image) sur une liste d'images et renvoie le pourcentage d'image renvoyant la valeur True.
    
    Paramètres
    ----------
    data_img : list
        Liste d'images, au format RGB.
    bool_function : function
        Fonction booléenne, prenant en entrée une image et renvoyant True ou False.
    
    Retours
    ----------
    float
        Pourcentage d'image renvoyant la valeur True lorsqu'on leur applique la fonction booléenne.
    """
    n = len(data_img)
    compteur = 0
    compteur_progression=0 #Permet un suivi utilisateur pour l'avancement de l'algorithme.
    compteur_progression2=0
    for i in range(n) :
        img_jpg = data_img[i]
        compteur += bool_function(img_jpg)
        compteur_progression+=1
        compteur_progression2+=1
        if  compteur_progression2 ==200 :  
            print("{} images. Nous en sommes à : {} %".format(compteur_progression,round(compteur_progression/n * 100,2)), "d'avancement.") # permet de garder une trace sur le nombre d'images qui ont été traitées pendant l'exécution de l'algorithme, qui peut être très longue...
            compteur_progression2=0 
    return compteur/n * 100




def percentage_true_feedback(data_img, bool_function_feedback) :
    """Fonction percentage_true_feedback enrichie d'un retour à l'utilisateur. Imprime un feedback à chaque étape.        
    Applique une fonction booléenne (agissant sur une image) sur une liste d'images et renvoie le pourcentage d'image renvoyant la valeur True.
    
    Paramètres
    ----------
    data_img : list
        Liste d'images, au format RGB.
    bool_function_feedback : function
        Fonction qui prend en entrée une image et renvoie une liste d'un booléen et d'un score, et qui dans son exécution imprime un feedback pour l'utilisateur.
    
    Retours
    ----------
    float
        Pourcentage d'image renvoyant la valeur True lorsqu'on leur applique la fonction booléenne.
    """
    n = len(data_img)
    compteur = 0
    compteur_progression=0
    compteur_progression2=0
    for i in range(n) :
        img_jpg = data_img[i]
        bool_and_feedback = bool_function_feedback(img_jpg)
        compteur += bool_and_feedback[0]
        compteur_progression+=1
        compteur_progression2+=1
        if  compteur_progression2 ==200 :  
            print("{} images. Nous en sommes à : {} %".format(compteur_progression,round(compteur_progression/n * 100,2)), "d'avancement.") # permet de garder une trace sur le nombre d'images qui ont été traitées pendant l'exécution de l'algorithme, qui peut être très longue...
            compteur_progression2=0            
    return compteur/n * 100
