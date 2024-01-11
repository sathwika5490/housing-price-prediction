================
Custom Transformer
================


The CustomScaler custom transformer utilizes scikit-learn's StandardScaler to scale numerical data, 
a common preprocessing step in machine learning to ensure consistent scales among numerical features. 
Scaling prevents features with larger magnitudes from overpowering those with smaller magnitudes during model 
training.

Methods 
========

Fit: Adapts the scaler to the input data.
Transform: Applies the fitted scaler to the input data. 
InverseTransform: Reverts the scaled data back to the original scale.



    


    