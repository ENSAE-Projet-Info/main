# Reproduction notre travail 

**Les fichiers correspondant aux différentes étapes de notre travail seront à déplacer à la racine du projet afin de pouvoir accéder à la librairie *utils* que nous avons écrite pour l'occasion**

## Partie Web App Scraping :
Aller directement au niveau de utils/scraping.data_scraping.py, specifier les chemins d'acces au niveau du module et executer le module avec le terminal. Possibilité de le faire directement sur le Report Notebook

## Partie Statistique Descriptive :
Ci-après la démarche à suivre:
* Placer le fichier Notebook_AiDress_Statistiques_Descriptives.ipynb à la racine du projet
* Installer les modules nécéssaires qui ne sont probablement pas installés sur votre machine :

```
# import sys
!{sys.executable} -m pip install keras==2.0.8
!{sys.executable} -m pip install opencv-python
!{sys.executable} -m pip install imageai
!{sys.executable} -m pip install requests
!{sys.executable} -m pip install tensorflow==1.14.0
!{sys.executable} -m pip install webcolors

```
Les autres modules sont specifiés dans le fichier module à la racine de ce dossier.

* Il ne reste plus qu'à exécuter les cellules du  notebook une par une. Attention, certaines fonctions peuvent prendre jusqu'à plusieurs heures, cela est indiqué quand c'est le cas et des alternatives sont proposées.


## Partie Modélisation : 
Le code de cette partie à été exécuter au sein d'un environnement Google Colab afin de pouvoir acceder aux ressourses GPU misent à disposition.

Le reproduction des resultats qui y sont exposés nécessitera donc l'utilisation de ce service.
Ci-après la démarche à suivre:
* Upload du fichier Notebook_AiDress_Modelisation.ipynb au sein de votre environnement Colab
* Upload des dossiers python_project_dataset et python_project_dataset_final présent dans le repertoire                 *utils/data* du projet dans votre google drive, au meme endroit où pointera le repertoire de travail de votre         notebook sur Colab
* Vous n'aurez plus qu'a executer les celulles, une fonction permet d'installer et d'importer tous les modules nécessaire au bon fonctionnement du notebook
    
## Partie Web App :
L'application est accessible live à l'adresse : https://aidress.onrender.com/ .

Si vous le souhaitez, vous pouvez, après avoir installer Docker, lancer la commande suivante à la racine du projet:

*docker build -t dressai*

*docker run -d dressai*


```python

```
