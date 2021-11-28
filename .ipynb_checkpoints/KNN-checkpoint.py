import numpy as np

def distancia_euclideana(ponto_a, ponto_b):
    """devolve a distancia entre os pontos A e B"""
    return np.sqrt(np.sum(np.square(ponto_a-ponto_b)))

class KNN_example:
    
    def __init__(self,K=3, max_iterations = 1000):
        self.K = K
        self.max_iterations=max_iterations



    def fit(self, X):
        """Utiliza os pontos X para encontrar os K centroides que melhor se
        adaptam aos dados
        Input:
            X-Matriz de dados
        Output:
        centroides-Os K centros para a matriz X"""
        
        self.X = X
        self.numero_exemplos, self.numero_atributos= X.shape
        #iniciar os centroides
        self.centroides = self._iniciar_centroides()
        
        
        #otimizar 
            for _ in range(self.max_iterations):
                
                #criar clusters
                self.clusters = self._criar_clusters(self)
                #atualizar centroides
                centroides_antigos = self.centroides
                self.centroides = self._atualizar_centroides(self)
                
            
        
                #confirmar paragem
                should_stop = self._confirmar_paragem(self.centroides, centroides_antigos)
        
   
    
    def _iniciar_centroides(self, noise=0.1):
        centroides=[]
        for _ in range(self.K):
            centroide_array=[]
            for atributo in range(self.numero_atributos):
                media_atributo=np.mean(self.X[:,atributo])
                centroide_valor_atributo=(media_atributo
                                          + noise
                                          * ((np.random.rand()*2)-1)
                                          * media_atributo)
                centroide_array.append(centroide_valor_atributo)
            centroides.append(np.array(centroide_array))
        return centroides
        
    def _criar_clusters(self, centroides):
        
        clusters= [() for _ in range(self.K)]
        
        for i in range(self.numero_exemplos):
            ponto = X[i,:]
            centroide_mais_perto=self.centroide_mais_perto(ponto)
            cluster[centroide_mais_perto.append].append(i)
        return clusters
    
    def _centroide_mais_perto(self, ponto):
        distancia_aos_centroides = [distancia_euclideana(ponto_a,centroide) 
                                    for centroide in self.centroides]
        centroide_mais_perto = np.minarg(distancia_aos_centroides)
        return centroide_mais_perto
       
    def _atualizar_centroides(self):
        centroides = _iniciar_centroides(noise=0.1)
        
        count=0
        for cluster in self.clusters:
            centro_de_gravidade = np.mean(X[cluster],axis=0)
            centroide[count] = centro_de_gravidade
            count +=1
        return centroides
    def _confirmar_paragem(self.centroides, centroides_antigos):
        distancia_entre_centroides = [distancia_euclideana(centroides[i], centroides_antigos[i]) 
                                      for i in range(len(centroides))] 
        should_stop = True if np.sum(distancia_entre_centroides
    
    def predict(self):
        pass
