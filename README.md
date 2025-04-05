# Project Idea
## Fake NEWS classification using Machine Learning

The surge of fake news, propelled by the rapid evolution of social media and digital communication channels, presents a pressing challenge. Detecting fake news is increasingly vital but hindered by resource limitations and evolving methodologies. This project addresses this challenge by proposing a fake news detection system leveraging machine learning techniques. It implements logistic regression as the classification model, integrating feature extraction methods like Counter Vectorizer (From Scikit Library). Furthermore, a dataset is constructed comprising both fake and genuine news to train the system comprehensively. Through rigorous experimentation, the efficacy of the approach is validated accurately in identifying fake news. This project mainly concentrates on how to spot fake news in internet news sources. We are dedicated in two ways. In order to determine the percentage of correct news that is phony, we will use multiple datasets of actual and fake news. We provide a thorough description of the selection, justification, and approval process as well as a few exploratory analyses on the observable evidence of etymological differences in false and legitimate news material. In order to create precise false news identifiers, we focus a lot of learning studies. Additionally, we provide close examinations of the automatic and manual evidence of bogus news. Python can be used to spot fake news posted on social media.

# Training
To ``train`` the model use the training folder. 
+ Use the Train.ipynb File to train, obtain the model and rename the model and vectorizer as follows, \
- ``Model --> model1.joblib``  
``Vectorizer --> vectorizer1.joblib ``
+ Then copy the ``renamed model1.joblib`` and ``vectorizer1.joblib`` to app folder.

# Flask Implementation of trained model
+ Simply run the main.py and it will give an ``IP_ADDRESS:PORT`` to access the website usually ``http://127.0.0.1:5000/``. 
+ Copy the Web ip and paste it any local machine's browser , then access the webpage.
* The user has to give the input article (i.e. the article which is going to be found out whether real or fake) to the webpage interface created through the use of flask framework of python and hit the submit button.
* The website through the help of flask framework will classify thr NEWS with trained model will display the result to the website.

# Contact
+ [Github](https://github.com/log-esh-bug)