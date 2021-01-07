#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 10:05:19 2021

@author: carrenolan
"""

install_requires=[
    'pyspark=={site.SPARK_VERSION}'
    ]

#On importe les packages utiles
from pyspark import SparkContext,SparkConf
from random import random
from time import time
import numpy as np
import math

#Instantiation l'API de Spark pour les RDD (spark context).
conf =SparkConf().setAppName("piestimator").setMaster("local")
sc = SparkContext(conf=conf)
n=100000


#La fonction suivante permet de simuler un point p avec 
#deux coordonnées x et y pour déterminer si le point simulé 
#est à l’intérieur ou à l'extérieur du cercle.

def is_point_inside_unit_circle(n):
    x, y = random(), random()   # simuler deux points  x et y
    return 1 if x*x + y*y < 1 else 0 # vérifier si ces deux points sont dans la cercle

#La fonction suivante permet d'estimer Pi par le biais de Spark
#Et retourne le nombre de point dans le cercle unité et une valeur estimée de Pi

def pi_estimator_spark(n):
    
    count = sc.parallelize(range(n)).map(is_point_inside_unit_circle).reduce(lambda a,b : a+b)
    pi_est = 4*count/n
        
    return count, pi_est

#La fonction suivante permet d'estimer Pi par le biais de Numpy
#Et retourne le nombre de point dans le cercle unité et une valeur estimée de Pi

def pi_estimator_numpy(n):
    
    count = np.arange(n)
    
    for i in range(n) :
        count[i] = is_point_inside_unit_circle(0) #0 n'importe pas, c'esst une valeur quelconque.
        
    tot = np.sum(count)
        
    pi_est = 4*tot/n
        
    return tot, pi_est

#Calcul avec Spark
t_init_S = time() #Initialisation du temps à 0 avant exécution de la fonction d'estimation.
(nb_pts_S, pi_est_S) = pi_estimator_spark(n) 
tmp_S = np.round(time()-t_init_S,6) #Donne le temps de calcul de la fonction d'estimation.
Ec_perc_S = np.abs(round(100-(pi_est_S/math.pi)*100,4)) #Donne l'écart à Pi en pourcents.

#Affichage des resultats
print("")
print("Spark")
print("Parmis les",n,"points,",nb_pts_S, "sont dans le cercle.")
print("")
print("Une approximation de Pi est de", pi_est_S, ".")
print("")
print("Le temps d'execution de l'algorithme avec Spark est de",tmp_S,"secondes.")
print("")
print("L'erreur est de", Ec_perc_S, "%")
print("")

#Calcul avec Numpy
t_init_N = time() #Initialisation du temps à 0 avant exécution de la fonction d'estimation.
(nb_pts_N, pi_est_N) = pi_estimator_numpy(n)
tmp_N = np.round(time()-t_init_N,6) #Donne le temps de calcul de la fonction d'estimation.
Ec_perc_N = np.abs(round(100-(pi_est_N/math.pi)*100,4)) #Donne l'écart à Pi en pourcents.

#Affichage des resultats
print("Numpy")
print("Parmis les",n,"points,",nb_pts_N, "sont dans le cercle.")
print("")
print("Une approximation de Pi est de", pi_est_N, ".")
print("")
print("Le temps d'execution de l'algorithme avec Numpy est de",tmp_N,"secondes.")
print("")
print("L'erreur est de", Ec_perc_N, "%")

sc.stop() #Ferme le SparkContext