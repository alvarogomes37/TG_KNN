import numpy as np
import pandas as pd
import collections

def calc_dist(ponto_a,ponto_b):
    """ Calculo da Distância Euclidiana entre os Pontos A e B"""
    return np.sqrt(np.sum(np.square(ponto_a-ponto_b)))

#importação do data set
dataset = pd.read_csv(r'C:\Users\Asus\Desktop\TG\TG_KNN\iris_csv.csv')

#Trocar os nomes das classes na coluna class por numeros
dataset.loc[dataset['class'] == "Iris-setosa",'class'] = 0
dataset.loc[dataset['class'] == "Iris-versicolor",'class'] = 1
dataset.loc[dataset['class'] == "Iris-virginica",'class'] = 2

#De seguida dividimos o dataset nos seu atributos e labels:
#A variavel X contém  as primeiras 4 colunas do dataser (i.e. atributos) e y comtém as labels.

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values


class KNN_example:
    def __init__(self,K=3):
        self.K=K
        
    def predict(self,v,X=X,y=y,K=3):
        
        """"definição da função de predição de dados"""
        distancias=[calc_dist(v,X[i,:]) for i in range(len(X))]
        
        """"ordernar os vetores mais proximos do ponto que queremos descobrir"""
    
        k_vetor_mais_proximo=np.argsort(distancias)[:K]
        
        """descobrir a label dos pontos mais proximos"""
        
        k_label_mais_proximo=[y[i] for i in k_vetor_mais_proximo]
        
        """"tendo em conta as labels dos pontos mais proximos vamos descobrir a label do vetor em teste"""
        
        
        label_output=collections.Counter(k_label_mais_proximo).most_common(1)[0][0]
       
    
        return label_output