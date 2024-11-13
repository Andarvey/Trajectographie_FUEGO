#author : Louis Bonamy - start : 7/11/2024 - end : 7/11/2024
#coding utf-8

"""
Place à l'origine d'un plot 3D un fichier au format .obj.
Problèmes : - les proportions ne sont toujours pas bonnes malgré les corrextion, je ne comprends pas.
            - localisation du fichier objet, ici il s'agit d'un chemin local et non à partir du git
"""

import trimesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Charger le modèle .obj
mesh = trimesh.load('C:/Users/Louis/Documents/Trajectographie_FUEGO') #valable sur mon pc en local à ADAPTER

# Obtenir les sommets et les faces
vertices = mesh.vertices
faces = mesh.faces

# Initialiser le graphique 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.axis('equal')
ax.set_box_aspect([1, 1, 1])

# Tracer les faces du modèle 3D
ax.plot_trisurf(
    vertices[:, 0], vertices[:, 1], vertices[:, 2], triangles=faces,
    color=(0.5, 0.5, 1), edgecolor='k', alpha=0.7
)

# Configurer la vue
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Calculer les limites basées sur les dimensions du modèle
x_limits = (vertices[:, 0].min(), vertices[:, 0].max())
y_limits = (vertices[:, 1].min(), vertices[:, 1].max())
z_limits = (vertices[:, 2].min(), vertices[:, 2].max())

ax.set_xlim(*x_limits)
ax.set_ylim(*y_limits)
ax.set_zlim(*z_limits)

#ax.set_box_aspect([1,1,1])  # Aspect ratio 1:1:1

plt.show()