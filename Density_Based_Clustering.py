import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn. neighbors import NearestNeighbors
from sklearn. preprocessing import StandardScaler
from sklearn. preprocessing import normalize
import seaborn as sns

data = pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Assignments\Data Mining\AirQualityUCI_2.xlsx")
df = pd.DataFrame(data)
df_data = df.iloc[0:5000,[2,5,8,9]]
print(df_data)

scaler = StandardScaler()
df_data = scaler.fit_transform(df_data)

df_data = normalize(df_data)

df_data = pd.DataFrame(df_data)
print(df_data)
x = df_data[0]
y = df_data[2]

nbrs = NearestNeighbors(n_neighbors=5).fit(df_data)
neigh_dist, neigh_ind = nbrs.kneighbors(df_data)


sort_neigh_dist = np.sort(neigh_dist, axis=0)


k_dist = sort_neigh_dist[:, 4]
plt.figure()
plt.plot(k_dist)

MinPts = 2*len(df_data.axes[1])
db = DBSCAN(eps=0.15, min_samples=MinPts).fit(df_data)

set(db.labels_)

plt.figure()
p = sns.scatterplot(data=df_data, x=x, y=y, hue=db.labels_, legend= "full", palette="deep")
sns.move_legend(p,"upper right", bbox_to_anchor=(1.20, 1.03), title="CLUSTERS")
plt.show()


