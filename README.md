# Animal Classification using Deep Learning

## Overview

This document outlines the analysis and classification models for an animal image dataset using deep learning techniques. The primary objective is to classify animals based on images, employing various preprocessing and augmentation steps along with a pre-trained neural network model.

## Dataset

The dataset consists of animal images collected from diverse sources. The dataset is collected from Kaggle.

https://www.kaggle.com/datasets/alessiocorrado99/animals10/data

## Data Preprocessing

The following steps were performed to prepare the data for model training:

1. Loaded and preprocessed data using the specified file paths.
2. Checked for corrupted images within the dataset.
3. Displayed the distribution of labels in the image dataset.
4. Displayed a subset of images from the dataset with their corresponding labels.
5. Split the data into training and testing sets.

## Model Development

The deep learning model is built using TensorFlow and Keras, incorporating transfer learning with a pre-trained EfficientNetB7 model. The model includes data augmentation layers to improve generalization.

1. Loaded the pre-trained EfficientNetB7 model.
2. Built and compiled the classification model with additional layers for fine-tuning.
3. Implemented data augmentation using TensorFlow's ImageDataGenerator.
4. Trained the model on the training dataset with five epochs.

## Model Evaluation

The model was evaluated on the test dataset, and predictions were generated. The evaluation includes:

1. Displaying the first 5 predictions.
2. Displaying 25 random pictures from the dataset with true and predicted labels.
3. Displaying confusion matrix and classification report.

## Dependencies

Ensure the following Python libraries are installed:

```bash
pip install numpy pandas tensorflow opencv-python PIL matplotlib seaborn
