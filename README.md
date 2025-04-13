# reconnaisance_faciale
 "Projet de reconnaissance faciale des images flous avec OpenCV"
 
 Amélioration, Détection et Reconnaissance Faciale

Ce projet utilise les bibliothèques Python OpenCV, NumPy et DeepFace pour améliorer la qualité d'une image, détecter les visages présents, et effectuer une reconnaissance faciale par comparaison avec une image de référence.


Bibliothèques nécessaires :

OpenCV (opencv-python)

NumPy (numpy)

DeepFace (deepface)

Fonctionnalités disponibles

📌 Amélioration d'image

Description : Utilise des techniques de traitement d'image telles que la transformée en cosinus discrète (DCT), l'égalisation d'histogramme et un seuillage adaptatif pour améliorer la qualité visuelle d'une image floue.

Résultats :

Image améliorée (image_amelioree.jpg)

Image seuillée (image_seuillage.jpg)

📌 Détection de visages

Description : Utilise un classificateur Haar pour détecter les visages dans une image et encadre automatiquement les visages trouvés.

Résultats :

Image avec les visages détectés (detected_faces.jpg)

Coordonnées des visages détectés.

📌 Reconnaissance faciale

Description : Compare les visages détectés avec une image de référence pour déterminer si un visage est connu ou inconnu.

Résultats :

Image annotée indiquant si le visage est reconnu (recognized_faces.jpg).

Comment exécuter le programme :
Placez les fichiers image nécessaires dans votre répertoire de travail :

Image floue : image_floue1.jpg

Image de référence : image_claire.jpg

Exécutez le script Python:

python projet.py

Suivez les étapes affichées dans le terminal :

Amélioration de l'image

Détection des visages

Reconnaissance faciale

Instructions pour les résultats:

Les résultats (images améliorées, visages détectés, reconnaissance faciale) seront sauvegardés dans votre répertoire de travail.

Auteurs :
Le code a été développé par Raja Bouabidi et Ala Bendaoued .



