import numpy as np
import pandas as pd
import collections
import matplotlib.pyplot as plt

def distancia_euclideana(ponto_a, ponto_b):
    """devolve a distancia entre os pontos A e B"""
    return np.sqrt(np.sum(np.square(ponto_a-ponto_b)))

v = [[1.4, 3.6, 3.4, 1.2]]

class KNN_example:
    
    dataset = pd.read_csv(r'C:\Users\Asus\Desktop\prog_knn\iris_csv.csv')



    #Trocar os nomes das classes na coluna class por numeros
    dataset.loc[dataset['class'] == "Iris-setosa",'class'] = 0
    dataset.loc[dataset['class'] == "Iris-versicolor",'class'] = 1
    dataset.loc[dataset['class'] == "Iris-virginica",'class'] = 2
    
    #The next step is to split our dataset into its attributes and labels. To do so, use the following code:

    #The X variable contains the first four columns of the dataset (i.e. attributes) while y contains the labels.

    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 4].values
    
    def predict(v,X=X,y=y,K=3):
        distancias=[calc_dist(v,X[i,:]) for i in range(len(X))]
    
        k_vetor_mais_proximo=np.argsort(distancias)[:K] 
    
        k_label_mais_proximo=[y[i] for i in k_vetor_mais_proximo]
    
        label_output=collections.Counter(k_label_mais_proximo).most_common(1)[0][0]
        print(k_vetor_mais_proximo)
        print(k_label_mais_proximo)
        print(label_output)
    
        return label_output