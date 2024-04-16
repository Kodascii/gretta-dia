<link rel="stylesheet" href="../../stylesheet.css">

# Story_11 — Réseaux de Neuronnes Convolutifs (CNN)

## Contexte
> Apprendre les techniques de comuter vision avec les réseaux de neurones convolutifs pour classifier les images.

## Mots clefs
- <def-of>CNN (Réseau de Neurones Convolutifs)</def-of> : *Type de réseau neuronal artificiel, particulièrement adapté au traitement d'images.*
- <def-of>[YOLO (You Only Look Once)](#yolo)</def-of> : *Algorithme de détection d'objets en vision par ordinateur qui offre un bon équilibre entre vitesse et précision.*
- <def-of>Pooling</def-of> : *Opération de sous-échantillonnage, réduisant ainsi le coût de calcul et empêchant le surajustement.. Les types de pooling les plus populaires sont le max et l'average pooling.*
- <def-of>[Padding](#padding)</def-of> : *Technique qui ajoute des pixels de zéro autour des frontières des données d'entrée et garantit que toutes les parties contribuent au processus d'extraction de fonctionnalités.*
- <def-of>Conv2D</def-of> : *Couche de convolution 2D, *
- <def-of>Stride</def-of> : *Paramètre qui dénote le nombre de pixels par lesquels la fenêtre se déplace après chaque opération.*
- <def-of>Fully connected</def-of> : *Les couches entièrement connectées sont généralement utilisées à la fin du CNN pour effectuer des tâches de classification.*
- <def-of>Flattened</def-of> : *Convertis un tensor (ou matrice) en un vecteur.*
- <def-of>[Dropout](#dropout)</def-of> : *Des neurones sont supprimés de manière aléatoire, de sorte que le réseau est obligé d'apprendre à partir de différents sous-ensembles de fonctionnalités dans les données d'entraînement. Cela permet d'éviter que le réseau ne s'appuie trop sur des fonctionnalités spécifiques ou ne devienne trop sensible à de petites variations dans les données.*
- <def-of>[Unet](#unet)</def-of> : *Type d'architecture de réseau neuronal conçue pour les tâches de segmentation d'images (diviser une image en ses différentes parties)*
- <def-of>[Transfer learning](#transfer-learning)</def-of> : *Exploite les enseignements d’un modèle précédemment formé comme point de départ pour un nouveau modèle, au lieu de former un nouveau modèle à partir de zéro.*
- <def-of>[Data augmentation](#data-augmentation)</def-of> : *Technique pour étendre artificiellement l’ensemble de données d’entraînement. Il fonctionne en créant de nouvelles versions légèrement modifiées des points de données existants.*
- <def-of>[Fine tuning](#fine-tuning)</def-of> : *Réglage de CNN utilisé pour améliorer les performances d'un modèle pré-entraîné sur une nouvelle tâche connexe.* 
- <def-of>Matrice de style (Matrice de Gram)</def-of> : *Technique qui permet de transférer le style artistique d'une image au contenu d'une autre image*
- <def-of>[Feature map](#feature-map)</def-of> : *Détecte un type spécifique de fonctionnalité dans l’image d’entrée. Ces fonctionnalités peuvent aller de fonctionnalités de bas niveau telles que les bords et les coins à des fonctionnalités de niveau supérieur telles que les formes et les textures.*

## Problématiques
1. Comment créer un réseaux de neuronnes convolutifs ?
1. Comment évaluer et améliorer un modèle CNN ?
1. Comment utiliser le transfer learning ?
1. Comment faire le fine tunning ?

## Hypothèses
- <u>Le padding permet de normaliser la dimension des entrées.</u> <h-f/> : *!;*
- <u>Ce que défini un CNN, est la présence d'au moins une couche de neurones convolutifs.</u> <h-t/> : *!;*²
- <u>On utilise le transfert leaning quand on veut utiliser les cnn et on as peut de données pour l'entraînement.</u> <h-t/> : *!;*
- <u>Le pooling est inutile sur des images présentant peu de détails.</u> <h-t/> : *!;*
- <u>Les CNN sont capables de détecter automatiquement les caractéristiques importantes dans une image sans intervention humaine</u> <h-t/> : *!;*
- <u>Les cnn nécessitent toujours une grande quantité de données d'entraînement pour obtenir de bonnes performances.</u> <h-t/> : *!;*
- <u>?</u> <h-t/> : *!;*
- <u>?</u> <h-t/> : *!;*
- <u>?</u> <h-t/> : *!;*

## Plan d'action
1. Investigation des ressources
6. Définitions des mots clefs;
7. Vérifier les hypothèses;
8. Répondre aux questions.

# RER

### YOLO
YOLO, which stands for "You Only Look Once", is a state-of-the-art algorithm used for real-time object detection in computer vision. Here's a breakdown of its key characteristics:

- **Single-Shot Detection:** Unlike some object detection methods that involve multiple stages to propose candidate regions and then classify them, YOLO is a single-shot detector. It processes the entire image once and directly predicts bounding boxes and class probabilities for objects in the image. This makes it computationally efficient and suitable for real-time applications.
- **Convolutional Neural Networks (CNNs):**  YOLO relies on CNNs for image processing and feature extraction. The specific architecture of YOLO utilizes a series of convolutional layers followed by fully connected layers to make predictions.
- **Bounding Boxes and Class Probabilities:** YOLO predicts bounding boxes around the detected objects in the image. These bounding boxes indicate the location and size of the objects. Additionally, YOLO assigns a class probability to each bounding box, indicating the likelihood that the enclosed region contains a specific object class (e.g., car, person, cat).
- **Speed and Accuracy:**  A major advantage of YOLO is its ability to achieve real-time object detection with good accuracy. This is particularly valuable for applications where fast processing is crucial, such as autonomous vehicles, video surveillance, or augmented reality.
- **Multiple Versions:**  Since its introduction in 2015, YOLO has undergone several iterations, each improving upon the previous version. Popular versions include YOLOv2, YOLOv3, and YOLOv5, each offering advancements in speed, accuracy, or model size.

**Applications of YOLO:**

YOLO's speed and efficiency make it suitable for various real-world applications:

- **Self-driving cars:** YOLO can be used to detect pedestrians, vehicles, and traffic signs in real-time, enabling autonomous vehicles to navigate their surroundings safely.
- **Video surveillance:** YOLO can be used to detect suspicious activity or objects in video feeds, improving security monitoring systems.
- **Drone object detection:** YOLO can be used on drones to identify objects of interest during aerial surveys or inspections.
- **Image and video analysis:** YOLO can be used to automate tasks like object counting, scene understanding, and content moderation in images and videos.

**Overall, YOLO is a powerful and versatile object detection algorithm that offers a good balance between speed and accuracy. Its ability to perform real-time object detection makes it a valuable tool for various applications in computer vision.**

### Padding
In the context of neural networks, particularly convolutional neural networks (CNNs) used for image processing tasks, padding refers to a technique that adds extra elements (usually zeros) around the borders of the input data (images). Here's a breakdown of its purpose and effects:

**Preserving Spatial Information:**

- A core function of CNNs is to extract features from images through convolutional layers. However, these convolutions can potentially shrink the size of the image as they move across the data. This is because the filter (kernel) used for convolution only overlaps with a portion of the input at a time.
- Padding addresses this issue by adding extra elements around the borders of the image. This ensures the filter considers all areas of the image during convolution and prevents the spatial dimensions (height and width) from getting progressively smaller after each convolutional layer.

**Types of Padding:**

There are two main types of padding used in CNNs:

- **Same Padding:** This type of padding aims to maintain the same output size (height and width) as the input after the convolution operation. The number of padding elements added on each side (top, bottom, left, right) is calculated based on the filter size and a specific padding strategy (often referred to as padding mode) like reflecting or repeating the edge values of the original image.
- **Valid Padding:** In contrast, valid padding prioritizes preserving all valid convolutions without necessarily maintaining the original dimensions.  Any convolutions that would cause the filter to go off the edges of the image are discarded, potentially resulting in a smaller output size compared to the input.

**Benefits of Padding:**

- **Preserves Information:** Padding helps retain valuable information from the edges of the image that might otherwise be lost due to filter size and stride (movement of the filter). This can be crucial for capturing important features present near the borders.
- **Controls Output Size:** Same padding allows for predictable output sizes, which can be helpful when designing the overall architecture of the CNN, especially when stacking multiple convolutional layers.

**Choosing Padding:**

The choice between same padding and valid padding depends on your specific needs and the desired outcome of the CNN. Here are some general considerations:

- If preserving all spatial information and maintaining output size is crucial, same padding is preferred.
- If discarding some peripheral information is acceptable in exchange for a potentially simpler network structure or avoiding overly large outputs, valid padding can be used.

Overall, padding is a vital concept in CNNs, allowing you to control the output size and ensure all parts of the input data contribute to the feature extraction process.

### Dropout
Dropout is a technique used in neural networks to address a common problem called **overfitting**. Here's how it works:

**Combating Overfitting:**

- Overfitting occurs when a neural network memorizes the training data too well, hindering its ability to generalize and perform well on unseen data. Imagine training a model to recognize handwritten digits using only images with very thick lines. The model might perfectly classify those specific images but struggle with digits written in a thinner style.

**Randomly Disabling Neurons:**

- Dropout works by randomly deactivating a certain percentage of neurons (units) in a layer during training. This means these neurons are temporarily ignored, and their connections are not used in the forward pass (where data flows through the network) or the backpropagation step (where the network learns and adjusts weights).

**Benefits of Dropout:**

- **Prevents Overfitting:** By randomly dropping out neurons, the network is forced to learn from different subsets of features in the training data during each training iteration. This helps prevent the network from relying too heavily on any specific features or becoming overly sensitive to small variations in the data.
- **Promotes Robustness:** Dropout essentially trains multiple variations of the network structure at the same time. This encourages the network to learn more robust feature representations that are less dependent on specific neurons or connections.

**Dropout Implementation:**

- Dropout is typically applied after each fully-connected or convolutional layer in a neural network (except the output layer). It's not applied during testing or prediction when you want the network to use all its learned knowledge.
- A dropout rate (percentage of neurons to drop) is chosen, often between 20% and 50%. This rate controls the level of randomness introduced during training.

**Analogy:**

- Imagine training a group of students for a competition. Dropout is like randomly dividing the students into smaller groups for practice sessions. Each group learns from a slightly different subset of the material, making them less likely to overfocus on specific details and more likely to develop a broader understanding.

**Overall, dropout is a simple yet powerful technique that helps neural networks avoid overfitting and learn more robust and generalizable representations from the training data.**

### Unet
U-Net is a specific type of artificial neural network architecture designed for **image segmentation** tasks in artificial intelligence. Here's a breakdown:

- **Field:**  U-Net falls under the field of **computer vision**, which is an AI subfield concerned with enabling computers to understand and process visual information.
- **Purpose:**  Its primary function is to segment images. In simpler terms, image segmentation involves dividing an image into its different parts or objects. For instance, segmenting a medical scan could separate the bones, muscles, and organs.
- **Strength:** U-Net is particularly adept at handling tasks with limited training data. This is crucial because acquiring large, labelled datasets for image segmentation can be expensive and time-consuming.
- **Architecture:** The architecture of U-Net is what makes it efficient. It has a U-shaped structure with two key parts:
    - **Contracting Path:** This part analyzes the image, capturing its overall context and extracting important features.
    - **Expanding Path:** This path uses the information from the contracting path to precisely localize and segment the objects in the image.

- **Applications:** U-Net's success in biomedical image segmentation led to its adoption in various fields. Here are some examples:
    - **Self-driving cars:** Segmenting objects like lanes, pedestrians, and vehicles is essential for safe navigation.
    - **Satellite imagery:** Segmentation helps identify different land cover types (forests, buildings, etc.).
    - **Material science:** Analyzing microscopic images can benefit from accurate segmentation.

Overall, U-Net is a powerful tool in AI's computer vision toolbox, especially for tasks requiring precise image segmentation with limited training data.

### Data Augmentation
Data augmentation is a technique used in machine learning, particularly in areas like computer vision, to artificially expand the training dataset. It works by creating new, slightly modified versions of existing data points in your dataset. This helps address challenges that arise due to limited data availability.

Here's a breakdown of how data augmentation works:

- **Goal:** Increase the diversity of your training data. Imagine training a model to recognize cats using only a few pictures. The model might struggle to recognize cats in different poses or lighting conditions. Data augmentation helps address this by creating variations of the existing data.
- **Process:** It involves applying various transformations to your existing data samples. These transformations are typically random and aim to mimic real-world variations but remain realistic.
- **Common Techniques:**
    - **Image Augmentation (for computer vision tasks):**
        * Flipping images (horizontally or vertically)
        * Rotating or cropping images
        * Adjusting brightness, contrast, or saturation
        * Adding noise or blurring effects
    - **Text Augmentation:**
        * Introducing typos or grammatical errors (controlled)
        * Synonyms replacement
        * Shuffling word order slightly

- **Benefits:**
    * **Reduces Overfitting:** By training the model on a wider variety of data, it reduces the risk of the model memorizing the training data instead of learning generalizable patterns.
    * **Improves Model Generalizability:** The model becomes more robust to variations in real-world data, leading to better performance on unseen data.
    * **Addresses Class Imbalance:** If your dataset has some classes with significantly fewer examples, data augmentation can help balance the representation.

- **Limitations:**
    * There's a balance to be struck. Too much augmentation can create unrealistic data that confuses the model. 
    * Not all types of data augmentation are effective for all tasks. Choosing the right techniques depends on your specific data and problem.

Overall, data augmentation is a valuable tool for enhancing the performance of machine learning models, especially when dealing with limited training data.

### Transfer learning

Transfer learning is a powerful technique in machine learning where knowledge gained while solving one task is reused on a related task. It's essentially leveraging the learnings from a previously trained model as a starting point for a new model, instead of training a new model from scratch.

Here's a breakdown of how transfer learning works:

- **Core Idea:** Imagine training a massive image recognition model on millions of general images (source task). This model learns low-level features like edges, shapes, and color combinations. Now, you want to train a new model to identify specific dog breeds (target task). Transfer learning allows you to reuse the pre-trained model (source model) and only fine-tune the final layers for dog breed classification.
- **Benefits:**
    * **Faster Training:** Since you're leveraging pre-trained weights, training the new model becomes significantly faster, especially for complex tasks requiring vast amounts of data.
    * **Improved Performance:** The pre-trained model already has valuable knowledge from the source task, which can benefit the target task, especially when dealing with limited data.
    * **Reduced Resources:** Training large models from scratch can be computationally expensive. Transfer learning allows you to achieve good results with less computational power.

- **Applications:** Transfer learning is widely used in various machine learning domains, including:

    * **Computer Vision:** Pre-trained models on massive image datasets can be fine-tuned for specific object detection, image segmentation, or image classification tasks.
    * **Natural Language Processing (NLP):** Pre-trained models on large text corpora can be fine-tuned for sentiment analysis, text summarization, or machine translation tasks.
    * **Speech Recognition:** Models trained on large audio datasets can be adapted for speaker identification or specific command recognition.

- **Types of Transfer Learning:**
    * **Full Transfer:** When the source and target tasks are very similar, the entire pre-trained model can be directly used for the target task with minimal adjustments.
    * **Fine-tuning:** This is the most common approach. The initial layers of the pre-trained model are frozen (weights don't change), and only the final layers are trained on the target task data.
    * **Feature Extraction:** Here, the pre-trained model is used as a feature extractor. Its final layers are removed, and the activations from the earlier layers are used as features for a new model trained on the target task.

Overall, transfer learning is a cornerstone technique in accelerating and improving the performance of machine learning models, especially in deep learning with complex tasks and limited data.

### Fine tuning
Fine-tuning, in the context of machine learning, is a specific technique that falls under the umbrella of transfer learning. It's a process used to improve the performance of a pre-trained model on a new, related task. Here's how it works:

**Leveraging Pre-Trained Knowledge:**

Imagine you have a large model trained on a massive dataset of general images (like ImageNet) to recognize various objects and concepts. This model has learned valuable generic features like edges, shapes, and basic visual patterns. Now, you want to use this knowledge to build a model that identifies specific dog breeds.

**Fine-tuning for a Specific Task:**

Fine-tuning takes this pre-trained model and adjusts it for your new task. Instead of training the entire model from scratch, you focus on modifying only the final layers. These final layers are responsible for making the final decisions or predictions specific to your new task (dog breed classification in this case).

**Why Fine-tuning?**

Here are some key benefits of fine-tuning:

- **Faster Training:** Since most of the model's weights are already learned from the pre-training stage, fine-tuning requires significantly less training data and time compared to training a new model from scratch.
- **Improved Performance:** The pre-trained model brings valuable knowledge to the table, even for the new task. This can be particularly helpful when dealing with limited data for the target task (dog breeds). The model can leverage its understanding of generic visual features to perform better. 
- **Reduced Resources:** Training large models from scratch can be computationally expensive. Fine-tuning allows you to achieve good results with a pre-trained model, reducing the computational resources required.

**Fine-tuning vs Full Training:**

- Fine-tuning is more efficient than training a whole new model from scratch, especially when there's a good amount of pre-trained knowledge relevant to the target task.
- In contrast, if the source and target tasks are entirely different, fine-tuning might not be as effective. In such cases, training a new model specifically designed for the target task might be necessary. 

**Overall, fine-tuning is a powerful technique within transfer learning that allows you to leverage pre-trained models and significantly improve the performance on related tasks with less time, data, and computational resources.**

### Feature map
In the context of convolutional neural networks (CNNs) used for image recognition and computer vision tasks, a feature map is a fundamental concept. Here's a breakdown of what a feature map is and its role in CNNs:

**Extracting Visual Information:**

- CNNs are adept at recognizing patterns and objects in images. They achieve this through a series of layers, and the core functionality lies in the convolutional layers.
- These convolutional layers process the input image using filters (also called kernels). These filters slide across the image, computing element-wise multiplications with small regions of the image.

**Feature Maps as Outputs:**

- The output of a convolutional layer is not a single number or value. Instead, it's a two-dimensional array called a feature map. There can be multiple feature maps generated by a single convolutional layer, depending on the number of filters used.

**Capturing Specific Features:**

- Each feature map focuses on detecting a specific type of feature in the input image. These features can range from low-level features like edges and corners to higher-level features like shapes and textures.
- The specific features a map captures depend on the design of the filter and its learned weights during the training process.

**Stacked for Hierarchy:**

- CNNs typically have multiple convolutional layers stacked together. The output feature maps from one layer become the input for the next convolutional layer.
- As you progress through the layers, the features become increasingly complex. Lower layers focus on basic features, while higher layers learn more intricate combinations of features, ultimately leading to object recognition.

**Visualizing Feature Maps (Optional):**

- Techniques exist to visualize feature maps, which can be helpful for understanding what a specific filter in a CNN is learning. These visualizations often appear as heatmaps where brighter areas represent stronger activations for a particular feature in that region of the image.

**Key Points:**

- Feature maps are the outputs of convolutional layers in CNNs.
- Each map captures specific visual features from the input image.
- Multiple feature maps are generated based on the number of filters used.
- Feature maps become progressively more complex through stacked convolutional layers.

**In essence, feature maps are the building blocks for CNNs to understand the visual content of images. They act as a bridge between the raw pixel data and the high-level understanding of objects and scenes that CNNs achieve.**