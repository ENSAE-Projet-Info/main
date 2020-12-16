from vars_ext import *
from PIL import Image
import pandas as pd
import seaborn as sns
import numpy as np
import scipy
import matplotlib.pyplot as plt
import os
import webcolors
import random
from keras.preprocessing.image import  img_to_array, load_img, ImageDataGenerator, array_to_img
from copy import copy
import glob
import cv2
from math import log
from imageai.Detection import ObjectDetection as od
import requests as req
from statistiques_descriptives_ext import *

image = Image.open(path+'/pull/' + pull[0])
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

import unittest 

class Stats_Des_Test(unittest.TestCase):
    """Test case utilisé pour tester les fonctions du module 'Statistiques_Descriptives'."""

    def test_closest_colour(self):
        """Test le fonctionnement de la fonction 'closest_colour'."""

        self.assertIn(closest_colour(np.array(image)[0,0,:]), colour_dict.values())

    def test_crop(self):
        """Test le fonctionnement de la fonction 'test_crop'."""

        self.assertIs(type(crop(image)),PIL.Image.Image)

    def test_major_colour(self):
        """Test le fonctionnement de la fonction 'major_colour'."""

        self.assertIn(major_colour(np.array(image)),colour_dict.values())

    def test_colour_repartition_mean(self):
        """Test le fonctionnement de la fonction 'colour_repartition_mean'."""

        self.assertIs(type(colour_repartition_mean('pull', 0.01)), dict)

    def test_colour_repartition_cluster(self):
        """Test le fonctionnement de la fonction 'colour_repartition_cluster'."""

        self.assertIs(type(colour_repartition_cluster('pull', 0.01)), dict)

    def test_colour_repartition_major(self):
        """Test le fonctionnement de la fonction 'colour_repartition_major'."""
        self.assertIs(type(colour_repartition_major('pull', 0.01)), dict)

    def test_colour_mean(self):
        """Test le fonctionnement de la fonction 'colour_mean'."""

        self.assertIs(type(colour_mean(image)),PIL.Image.Image)
        
    def test_colour_var(self):
        """Test le fonctionnement de la fonction 'colour_var'."""

        self.assertIs(type(colour_var(image)),PIL.Image.Image)


    def test_is_logo(self):
        """Test le fonctionnement de la fonction 'is_logo'."""

        self.assertIn(is_logo(image),(True,False))

    def test_is_logo_feedback(self): 
        """Test le fonctionnement de la fonction 'is_logo_feedback'."""

        self.assertIn(is_logo_feedback(image)[0],(True,False))
        self.assertIs(type(is_logo_feedback(image)[1]),float)
        
    def test_is_white(self):
        """Test le fonctionnement de la fonction 'is_white'."""

        self.assertIn(is_white(np.array(image)[0,0,:]),(True,False))
        
    def test_white_percentage(self):
        """Test le fonctionnement de la fonction 'white_percentage'."""

        self.assertIs(type(white_percentage(image)),float)
        
    def test_white_to_grey(self):
        """Test le fonctionnement de la fonction 'white_to_grey'."""

        self.assertIs(type(white_to_grey(image)),PIL.Image.Image)

    def test_is_white_background(self):
        """Test le fonctionnement de la fonction 'is_white_background'."""

        self.assertIn(is_white_background(image),(True,False))
        
    def test_is_white_background_feedback(self):
        """Test le fonctionnement de la fonction 'is_white_background_feedback'."""

        self.assertIn(is_white_background_feedback(image)[0],(True,False))
        self.assertIs(type(is_white_background_feedback(image)[1]),float)
        
    def test_percentage_true (self): 
        """Test le fonctionnement de la fonction 'percentage_true'."""

        self.assertIs(type(percentage_true([image],is_white_background)),float)
        
        
    def test_percentage_true_feedback (self): 
        """Test le fonctionnement de la fonction 'percentage_true_feedback'."""

        self.assertIs(type(percentage_true_feedback([image],is_white_background_feedback)),float) 

if __name__ == '__main__' :
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
