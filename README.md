# BookApp – an app for generating emotional trajectories of stories
Simple app that enables you to upload your text file and generate an image of its emotional trajectory using sentiment analysis. It lets you then add the book to the database and find 5 most similar emotional trajectories within existing 580 images.
<br><br>For every sentence of given text, sentiment score is calculated. The data is then smoothed with PAA algorithm and visualized. 
## Technologies
Project is created with:
* Python 3.9.1
* Django 4.1.5
* TensorFlow 2.11.0
* Transformers 4.25.1
* DeepImageSearch
* Pandas 1.4.4
* NumPy 1.23.5
* NLTK 3.5
* Matplotlib 3.6.2
* Scipy 1.9.1
