# Bank Note Authentication end to end implementation with Docker, Building UI with Flasgger, Deployed with Streamlit on Heroku, Flask

![image from Kaggle](https://www.neuraldesigner.com/images/banknote-authentication.jpeg)

[Download the data from Kaggle](https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data)

### About the data
Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.
The problem statement is quiet simple:
#### Problem statement

as it is described in about the data section, There is a gray scale pictures of notes with a resolution of about 660 dpi.
Wavelet Transform tool were used to extract features from images.we have four features`['Variance', 'skewness', 'curtosis', 'entropy']` and we have to predict wheather Bank Note is authentic or not.

I Have used RandomForestClassifier to predict wheather the note is authetic or not as problem is not that complex, We have Cleaned data with 0 Null values.just fitted the data and predict  with 98% accuracy on test data.
and created pcikle file .
The pickle module implements a fundamental, but powerful algorithm for serializing and de-serializing a Python object structure.and additonally pickle is a binary file format
I have used flask to create a Web API
