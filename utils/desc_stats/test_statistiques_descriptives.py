class Stats_Des_Test(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'Statistiques_Descriptives'."""

    def setUp(self):
        """Initialisation des tests."""
        self.path = 'D:\Downloads\python_project_dataset\python_project_dataset'
        self.pull = os.listdir(path=path+'\pull')
        self.tshirt = os.listdir(path=path+'\\tshirt')
        self.short = os.listdir(path=path+'\short')
        self.pantalon = os.listdir(path=path+'\pantalon')
        self.image = Image.open(path+'\pull/' + pull[0])
        self.colour_dict = {'#FFFFFF' : 'Blanc',
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


    def test_closest_colour(self):
        """Test le fonctionnement de la fonction 'closest_colour'."""

        self.assertIn(closest_colour(np.array(image)[0,0,:]), colour_dict.values())

    def test_crop(self):
        """Test le fonctionnement de la fonction 'test_crop'."""

        self.assertIs(crop(image),PIL.Image.Image)

    def test_major_colour(self):
        """Test le fonctionnement de la fonction 'major_colour'."""

        self.assertIs(major_colour(np.array(image)),colour_dict.values())

    def test_colour_repartition_mean(self):
        """Test le fonctionnement de la fonction 'colour_repartition_mean'."""

        self.assertIs(major_colour_mean('pull', 0.01), dict)
        self.assertIs(major_colour_mean('pull', 0.01).values(), int)
        self.assertEqual(major_colour_mean('pull', 0.01).keys(),colour_dict.values())

    def test_colour_repartition_cluster(self):
        """Test le fonctionnement de la fonction 'colour_repartition_cluster'."""

        self.assertIs(major_colour_cluster('pull', 0.01), dict)
        self.assertIs(major_colour_cluster('pull', 0.01).values(), int)
        self.assertEqual(major_colour_cluster('pull', 0.01).keys(),colour_dict.values())

    def test_colour_repartition_major(self):
        """Test le fonctionnement de la fonction 'colour_repartition_major'."""
        self.assertIs(major_colour_major('pull', 0.01), dict)
        self.assertIs(major_colour_major('pull', 0.01).values(), int)
        self.assertEqual(major_colour_major('pull', 0.01).keys(),colour_dict.values())

    def test_colour_mean(self):
        """Test le fonctionnement de la fonction 'colour_mean'."""

        self.assertIs(colour_mean(image),PIL.Image.Image)
        
    def test_colour_var(self):
        """Test le fonctionnement de la fonction 'colour_var'."""

        self.assertIs(colour_var(image),PIL.Image.Image)


    def test_is_logo(self):
        """Test le fonctionnement de la fonction 'is_logo'."""

        self.assertIs(is_logo(image),bool)

    def test_is_logo_feedback(self): 
        """Test le fonctionnement de la fonction 'is_logo_feedback'."""

        self.assertIs(is_logo_feedback(image)[0],bool)
        self.assertIs(is_logo_feedback(image)[1],float)
        
    def test_is_white(self):
        """Test le fonctionnement de la fonction 'is_white'."""

        self.assertIs(is_white(image[0,0,:]),bool)
        
    def test_white_percentage(self):
        """Test le fonctionnement de la fonction 'white_percentage'."""

        self.assertIs(is_white(image),float)
        
    def test_white_to_grey(self):
        """Test le fonctionnement de la fonction 'white_to_grey'."""

        self.assertIs(white_to_grey(image),PIL.Image.Image)

    def test_is_white_background(self):
        """Test le fonctionnement de la fonction 'is_white_background'."""

        self.assertIs(is_white_background(image),bool)
        
    def test_is_white_background_feedback(self):
        """Test le fonctionnement de la fonction 'is_white_background_feedback'."""

        self.assertIs(is_white_background_feedback(image)[0],bool)
        self.assertIs(is_white_background_feedback(image)[1],float)
        
    def test_is_human_model(self):
        """Test le fonctionnement de la fonction 'is_human_model'."""

        self.assertIs(is_human_model(path+'\pull/' + pull[0]),bool)
        
    def test_is_human_model_feedback(self): 
        """Test le fonctionnement de la fonction 'is_human_model_feedback'."""

        self.assertIs(is_human_model_feedback(path+'\pull/' + pull[0])[0],bool)
        
    def test_percentage_true (self): 
        """Test le fonctionnement de la fonction 'percentage_true'."""

        self.assertIs(percentage_true(image),float)
        
    def test_percentage_true (self): 
        """Test le fonctionnement de la fonction 'percentage_true'."""

        self.assertIs(percentage_true([image],is_white_background),float)
        
    def test_percentage_true_feedback (self): 
        """Test le fonctionnement de la fonction 'percentage_true_feedback'."""

        self.assertIs(percentage_true_feedback([image],is_white_background_feedback),float)   
        
