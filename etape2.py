#author : Louis Bonamy - start : 7/11/2024 - end : 
#coding utf-8

"""
Une fonction qui place la fusée dans le plot en fonction de 3 coordonnées d'espace et 3 d'angles (à adapter avec les données du capteur)
"""

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