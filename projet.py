import cv2
import numpy as np
from deepface import DeepFace
import os

### AMÉLIORATION DE L'IMAGE ###
def enhance_image(image_path, output_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f" Impossible de charger l'image : {image_path}")
        return None

    img_f32 = np.float32(image) / 255.0
    dct = cv2.dct(img_f32)
    dct[:30, :30] *= 2
    enhanced_img = cv2.idct(dct)
    enhanced_img = np.uint8(np.clip(enhanced_img * 255, 0, 255))

    enhanced_img = cv2.equalizeHist(enhanced_img)

    thresholded = cv2.adaptiveThreshold(
        enhanced_img, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11, 2
    )

    cv2.imshow("Image Améliorée", enhanced_img)
    cv2.imshow("Image Seuillée", thresholded)

    cv2.imwrite(output_path, enhanced_img)
    cv2.imwrite("image_seuillage.jpg", thresholded)
    return output_path


### DÉTECTION DE VISAGE ###
def detect_faces(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f" Image non trouvée : {image_path}")
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Visages détectés", image)
    cv2.imwrite("detected_faces.jpg", image)
    return "detected_faces.jpg", faces


### RECONNAISSANCE FACIALE ###
def recognize_faces(image_path, reference_image_path):
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f" img2_path introuvable : {image_path}")
        if not os.path.exists(reference_image_path):
            raise FileNotFoundError(f" img1_path introuvable : {reference_image_path}")

        result = DeepFace.verify(
            img1_path=reference_image_path,
            img2_path=image_path,
            enforce_detection=False
        )

        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f" Image non trouvée : {image_path}")

        name = "Inconnu"
        if result["verified"]:
            name = " Personne connue"

        cv2.putText(image, name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0),1)
        cv2.imshow("Reconnaissance Faciale", image)
        cv2.imwrite("recognized_faces.jpg", image)
        return "recognized_faces.jpg"

    except Exception as e:
        print(f" Erreur pendant la reconnaissance faciale : {e}")
        return None


###  EXÉCUTION DU PIPELINE ###
input_image = r"C:\Users\33758\python\dossierprojet\image_floue1.jpg"
reference_image = r"C:\Users\33758\python\dossierprojet\image_claire.jpg"
output_image = "image_amelioree.jpg"

print("[1] Amélioration de l'image...")
enhanced_image = enhance_image(input_image, output_image)

if enhanced_image:
    print("[2] Détection des visages...")
    detected_faces, faces = detect_faces(enhanced_image)

    if len(faces) > 0:
        print("[3] Reconnaissance faciale en cours...")
        recognized_image = recognize_faces(enhanced_image, reference_image)
        if recognized_image:
            print(" Processus terminé. Voir 'recognized_faces.jpg'.")
    else:
        print(" Aucun visage détecté, reconnaissance annulée.")
else:
    print(" Échec de l'amélioration, traitement interrompu.")

cv2.waitKey(0)
cv2.destroyAllWindows()
