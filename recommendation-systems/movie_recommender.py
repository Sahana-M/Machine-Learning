#install numpy using ->  pip install numpy
#install lightfm using -> pip install lightfm


import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#store data
data = fetch_movielens(min_rating = 4.0)

#choose a model, wrap - weighted apporoximate rank pairwise, uses gardient decent, both content based and collaborative -> hybrid system
model = LightFM(loss = 'warp')
model.fit(data['train'], epochs = 30, num_threads = 2)

def sample_recommendation(model, data, user_ids):
  
  n_users, n_items = data['train'].shape
  
  for user_id in user_ids:
  
    #csr -> compressed sparsed row format, movues they already like
    known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

    #movies our model predicts they like
    scores = model.predict(user_id, np.arange(n_items))
 
    #ranking them in order of most likes to least
    top_items = data['item_labels'][np.argsort(-scores)]
    
    print("User %s" % user_id)
    print("     Best liked:")    
    for x in known_positives[:3]:
      print("        %s" % x)

    print("     Recommended:")
    
    for x in top_items[:3]:
      print("        %s" % x)
      
      
sample_recommendation(model, data, [3,25,450])


 
 

       
      
