#author : Louis Bonamy - start : 7/11/2024 - end : 21/11/2024 
#coding utf-8

"""
Une fonction qui place la fusée dans le plot en fonction de 3 coordonnées d'espace et 3 d'angles (à adapter avec les données du capteur)

Problèmes : - le point 0 du repère n'est pas strictement au milieu, ce n'est pas un problème de code mais de construction du modèle
"""
import trimesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def translate_mesh(mesh, translation_vector):
    """
    Applique une translation à tous les sommets du modèle.
    """
    # Appliquer la translation à chaque sommet
    mesh.vertices += translation_vector
    return mesh

def rotate_mesh(mesh, angles):
    """
    Applique des rotations (roll, pitch, yaw) au modèle.
    
    Args:
        mesh (trimesh.Trimesh): Le modèle 3D à transformer.
        angles (tuple): Angles de roulis, tangage et lacet en degrés (r, l, t).
    """
    # Convertir les angles en radians
    roll, pitch, yaw = np.radians(angles)

    # Matrices de rotation
    R_x = np.array([
        [1, 0, 0],
        [0, np.cos(roll), -np.sin(roll)],
        [0, np.sin(roll), np.cos(roll)]
    ])
    
    R_y = np.array([
        [np.cos(pitch), 0, np.sin(pitch)],
        [0, 1, 0],
        [-np.sin(pitch), 0, np.cos(pitch)]
    ])
    
    R_z = np.array([
        [np.cos(yaw), -np.sin(yaw), 0],
        [np.sin(yaw), np.cos(yaw), 0],
        [0, 0, 1]
    ])

    # Appliquer la rotation : ordre Z (yaw), Y (pitch), X (roll)
    rotation_matrix = R_z @ R_y @ R_x
    mesh.vertices = np.dot(mesh.vertices, rotation_matrix.T)
    return mesh

def placement(x,y,z,r,l,t):
    """La fonction en question.

    Args:
        x (float): coordonnée x du centre de masse en mètre
        y (float): coordonnée y du centre de masse en mètre
        z (float): coordonnée z du centre de masse en mètre
        r (float): angle de roulis en degré
        l (float): angle de lacet en degré
        t (float): angle de tangage en degré
    """
    # Charger le modèle .obj
    mesh = trimesh.load('fusée_3d.obj', file_type='obj')

    # Spécifier les coordonnées de translation (x, y, z)
    translation_vector = np.array([x, y, z])  # Exemple : déplacer de 10 unités en x, 5 en y, et 15 en z

    # Appliquer la translation
    mesh = translate_mesh(mesh, translation_vector)
    
    # Appliquer les rotations
    mesh = rotate_mesh(mesh, (r, t, l))  # Note : ordre (roll, pitch, yaw)

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

    # Calculer les limites basées sur les dimensions du modèle
    x_limits = (vertices[:, 0].min(), vertices[:, 0].max())
    y_limits = (vertices[:, 1].min(), vertices[:, 1].max())
    z_limits = (vertices[:, 2].min(), vertices[:, 2].max())

    ax.set_xlim(*x_limits)
    ax.set_ylim(*y_limits)
    ax.set_zlim(*z_limits)

    ax.axis('equal')
    ax.set_box_aspect([1,1,1])  # Aspect ratio 1:1:1

    plt.show()

placement(0,0,0,0,0,0)