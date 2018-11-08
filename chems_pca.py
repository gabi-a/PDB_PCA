import numpy as np
import pickle

from sklearn import decomposition

chem_names = pickle.load(open("chem_names.pkl","rb"))
chems = pickle.load(open("../blasting_preconceptions/db/chems_dict.pkl","rb"))

num_wells = len(chems.keys())
num_chems = len(chem_names)

X = np.zeros((num_wells,num_chems), float)

for i,well in enumerate(chems.values()):
    for cond in well:
        X[i, chem_names.index(cond['chem'])] = 1

pca = decomposition.PCA(n_components=num_chems)
pca.fit(X)

np.save("pca_matrix", X)
pickle.dump(pca, open("pca_result.pkl","wb"))