# Proyecto de Inteligencia Artificial

Reconocimiento facial usando el detector de caras MTCNN y [Facenet](https://github.com/davidsandberg/facenet) (pre entrenado por David Sandberg) 


# Instalación

StackEdit stores your files in your browser, which means all your files are automatically saved locally and are accessible **offline!**

 1. Crear un ambiente virtual de Python 3 
 2. Ir a la ubicación del código     `/project-ai` 
 3.  Ejecutar `pip install -r requirements.txt` 
 4.  Bajar el  modelo preentrenado    [aquí](https://drive.google.com/file/d/1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55-/view)     y ponerlo en el directorio `project-ai/facenet/src/`

# Ejecución
En la carpeta `project-ai/facenet/dataset/raw` se tienen que crear los directorios con las caras de las personas a identificar. Lo ideal es tener 10 fotos por persona y cada una de estas personas debe tener su propia carpeta. 
## Identificación de caras
Las caras detectadas serán guardadas en `project-ai/facenet/dataset/aligned`

En nuestro caso, el comando sería

    python facenet/src/align/align_dataset_mtcnn.py   facenet/dataset/raw facenet/dataset/aligned  --image_size 160 --margin 32


## Entrenamiento de caras

    python facenet/src/classifier.py TRAIN     facenet/dataset/aligned facenet/src/20180402-114759/     facenet/src/20180402-114759/my_classifier.pkl     --batch_size 50 --min_nrof_images_per_class 6     --nrof_train_images_per_class 6 --use_split_dataset

En la carpeta `project-ai/output` estará la lista de caras que va a reconocer. No necesariamente todos los modelos en `project-ai/raw` serán usados en el modelo. Esto depende de cuantas caras correctamente identificadas tenga por persona. En nuestro caso, se necesitan al menos 6 fotos por cada individuo.

## Reconocimiento facial


Las imágenes de pruebas pueden estar en una carpeta como `project-ai/facenet/dataset/test-images/`

Para ejecutar una sola foto en el directorio:

    python facenet/src/face_recognition_image.py facenet/dataset/test_images/velasco_mite.jpeg

Para ejecutar todas las fotos de una carpeta:

    python facenet/src/face_recognition_image_batch.py facenet/dataset/FOTOS_A_RECONOCER/

Para ejecutar desde la cámara:

    python facenet/src/camera-example.py

Los resultados estarán en la carpeta `project-ai/output`. Las caras serán marcadas con un cuadro verde y si reconoce una cara con una probabilidad mayor a 0.15, se colocará el nombre debajo.


