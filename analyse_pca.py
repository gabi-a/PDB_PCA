from sklearn import decomposition
import numpy as np
import pickle

import matplotlib.pyplot as plt

pca = pickle.load(open("pca_result.pkl","rb"))
chem_names = pickle.load(open("chem_names.pkl","rb"))

variance_ratios = pca.explained_variance_ratio_

chems_by_importance = []

for component in pca.components_:
    chems_by_importance.append(chem_names[np.argmax(component)])

for c in chems_by_importance[:10]:
    print(c)

plt.bar(range(0,len(variance_ratios)), variance_ratios)
plt.show()
