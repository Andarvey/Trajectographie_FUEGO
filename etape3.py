#author : Louis Bonamy - start : 21/11/2024 - end : ??/??/???? 
#coding utf-8

"""
Utilise la fonction de placement modifiée et ses copines pour afficher une animation du déplacement de la fusée. Dans l'idéal,
récupérer les données de vol de l'année dernière et l'animer. Il faut que la trajectoire s'affiche derrière le passage de la fusée.

PROBLEMES : - il faut encore récupérer les données
            - il faut vérifier que le tracé soit juste, c'est possible que ce soit le modèle 3D qui soit pété
"""
import trimesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.animation import FuncAnimation

def translate_mesh(mesh, translation_vector):
    """Applique une translation à tous les sommets du modèle."""
    mesh.vertices += translation_vector
    return mesh

def rotate_mesh(mesh, angles):
    """Applique des rotations (roll, pitch, yaw) au modèle."""
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

def placement(ax, mesh, x, y, z, r, l, t, trajectory_x, trajectory_y, trajectory_z):
    """Place et oriente un modèle 3D en appliquant une translation et des rotations."""
    # Appliquer la translation
    translation_vector = np.array([x, y, z])
    mesh = translate_mesh(mesh, translation_vector)

    # Appliquer les rotations
    mesh = rotate_mesh(mesh, (r, t, l))  # (roll, pitch, yaw)

    # Mettre à jour les sommets et les faces
    vertices = mesh.vertices
    faces = mesh.faces

    ax.clear()  # Efface le graphique précédent

    # Tracer les faces du modèle 3D
    ax.plot_trisurf(
        vertices[:, 0], vertices[:, 1], vertices[:, 2], triangles=faces,
        color=(0.5, 0.5, 1), edgecolor='k', alpha=0.7
    )

    # Relier les points successifs avec une ligne
    ax.plot(trajectory_x, trajectory_y, trajectory_z, color="r", marker="", markersize=5, linestyle='-', alpha=0.7)

    # Configurer la vue
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Calculer les limites basées sur les dimensions du modèle
    x_limits = (-100, 100)  # Plage fixe pour X (ajustez selon vos besoins)
    y_limits = (-100, 100)  # Plage fixe pour Y (ajustez selon vos besoins)
    z_limits = (-100, 100)  # Plage fixe pour Z (ajustez selon vos besoins)

    ax.set_xlim(x_limits)
    ax.set_ylim(y_limits)
    ax.set_zlim(z_limits)

    #ax.axis('equal')
    ax.set_box_aspect([1, 1, 1])  # Aspect ratio 1:1:1

def update(frame, mesh, ax, positions, rotations, trajectory_x, trajectory_y, trajectory_z):
    """Fonction d'update pour l'animation."""
    # Récupérer la position et les angles pour cette frame
    x, y, z = positions[frame]
    r, l, t = rotations[frame]

    # Ajouter la position actuelle à la trajectoire
    trajectory_x.append(x)
    trajectory_y.append(y)
    trajectory_z.append(z)

    # Appeler la fonction placement pour chaque frame
    placement(ax, mesh, x, y, z, r, l, t, trajectory_x, trajectory_y, trajectory_z)

def animate():
    """Lancer l'animation avec une séquence de positions et rotations."""
    # Charger le modèle .obj
    mesh = trimesh.load('fusée_3d.obj', file_type='obj')

    # Initialiser le graphique 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Séquence de positions (x, y, z)
    positions = [
        (0, 0, 0), (1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)
    ]

    # Séquence d'angles (roll, pitch, yaw)
    rotations = [
        (0, 0, 0), (30, 45, 60), (60, 90, 120), (90, 135, 150), (120, 180, 210)
    ]

    # Initialiser les listes pour la trajectoire
    trajectory_x = []
    trajectory_y = []
    trajectory_z = []

    # Créer l'animation
    ani = FuncAnimation(
        fig, update, frames=len(positions), fargs=(mesh, ax, positions, rotations, trajectory_x, trajectory_y, trajectory_z),
        interval=10, repeat=True
    )

    # Afficher l'animation
    plt.show()

animate()
