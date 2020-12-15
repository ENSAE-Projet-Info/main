path = "utils/data/python_project_dataset"

pull = os.listdir(path=path+'/pull')
tshirt = os.listdir(path=path+'/tshirt')
short = os.listdir(path=path+'/short')
pantalon = os.listdir(path=path+'/pantalon')

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
