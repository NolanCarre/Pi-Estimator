# Pi-Estimator
Ce projet consiste à estimer Pi par le biais de Spark et Numpy et comparer leur temps d'exécution et leur écart à Pi (valeur machine).

# Estimation de Pi 
## Avec 100 000 points
<img src="Output/tab_100000.png" 
  style="float: center; margin-right: 10px; margin-top: 10px; margin-bottom: 10px;" />

## Avec 1 000 000 points
<img src="Output/tab_1000000.png" 
  style="float: center; margin-right: 10px; margin-top: 10px; margin-bottom: 10px;" />
  
## Performances Spark vs. Numpy
Avec n = 100 000 points la méthode utilisant Numpy est à privilégier car plus précise.
En revanche, avec n = 1 000 000 la méthode utilisant Spark sera plus précise.

Dans les deux cas, Numpy permet d'obtenir une vitesse d'exécution plus élevée.

#Remarques
Le choix entre Numpy et Spark doit se faire en fonction des besoins. En particulier, si le nombre de données est élevé il est préférable d'utiliser Spark afin d'accroître la précision. Mais le temps d'exécution sera plus élevé.

