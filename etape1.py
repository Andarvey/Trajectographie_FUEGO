import trimesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Charger le modèle .obj
mesh = trimesh.load('C:/Users/Louis/Documents/2024-25/ASTRE/fusée_3d.obj')

# Obtenir les sommets et les faces
vertices = mesh.vertices
faces = mesh.faces

# Initialiser le graphique 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tracer les faces du modèle 3D
ax.plot_trisurf(
    vertices[:, 0], vertices[:, 1], vertices[:, 2], triangles=faces,
    color=(0.5, 0.5, 1), edgecolor='k', alpha=0.7
)

# Configurer la vue
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_box_aspect([1,1,10])  # Aspect ratio 1:1:1

plt.show()