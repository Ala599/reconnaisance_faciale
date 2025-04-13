Pipeline pour Améliorer une Image avec Reconnaissance Faciale
Objectif
Le but de ce projet est de traiter une image floue afin de l'améliorer, détecter les visages présents et effectuer une reconnaissance faciale en comparant les visages détectés avec une image de référence.

Description des Étapes
1️⃣ Amélioration de l'Image
Fonction utilisée : enhance_image(image_path, output_path)

But : Appliquer une série de traitements sur l'image pour l'améliorer en utilisant la Transformée en Cosinus Discrète (DCT), l'égalisation d'histogramme et un seuillage adaptatif.


Image seuillée (image_seuillage.jpg).

2️⃣ Détection de Visages
Fonction utilisée : detect_faces(image_path)

But : Localiser les visages dans une image en utilisant un classificateur en cascade Haar fourni par OpenCV.


3️⃣ Reconnaissance Faciale
Fonction utilisée : recognize_faces(image_path, reference_image_path)

But : Comparer les visages détectés avec une image de référence pour identifier une correspondance en utilisant DeepFace.


Pipeline Global
Amélioration de l'image :

Charger l'image floue.

Améliorer la qualité de l'image.

Détection des visages :

Identifier et encadrer les visages détectés.

Reconnaissance faciale :

Vérifier si le visage détecté correspond à l'image de référence.

Dépendances
Bibliothèques Python nécessaires :

cv2 : Manipulation et traitement des images.

numpy : Calculs mathématiques et manipulation de matrices.

DeepFace : Vérification et reconnaissance faciales.

os : Gestion des chemins de fichiers.

Données :

Image d'entrée floue.

Image de référence claire.

Pré-requis

Installer les bibliothèques avec pip install opencv-python numpy deepface.

Placer les images dans les chemins spécifiés dans le code.

Configurer l'environnement Python pour exécuter le script.