# spam_detector_app/views.py
import pickle
from django.shortcuts import render
from django.http import HttpResponse

# Load the Multinomial Naive Bayes model and CountVectorizer object from disk
filename = '/home/sivakavi/Desktop/dj/spam.pkl'
with open(filename, 'rb') as file:
    classifier = pickle.load(file)

cv = pickle.load(open('/home/sivakavi/Desktop/dj/spam_filter/utils/cv.pkl', 'rb'))

def home(request):
    return render(request, 'index.html')

def prediction(request):
    return render(request, 'spam.html')

def about(request):
    return render(request, 'about.html')

def predict(request):
    if request.method == 'POST':
        message = request.POST['mess']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction = classifier.predict(vect)
        return render(request, 'result.html', {'prediction': my_prediction})


