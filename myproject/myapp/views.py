from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

# Create your views here.
def index(request):
    return render(request, 'index.html')


def counter(request):
    text = request.POST['text']

    amount_of_words = len(text.split())

    total_length = sum(len(word) for word in text.split())

    uppercase_count = sum(1 for char in text if char.isupper())

    lowercase_count = sum(1 for char in text if char.islower())

    greeting = "Hello! Welcome to the Text Analyzer."

    description = "This app can count words, total letters, uppercase, and lowercase letters in your text."

    return render(request, 'counter.html', {
        'amount': amount_of_words, 
        'total_length': total_length,  
        'uppercase_count': uppercase_count,
        'lowercase_count': lowercase_count,
        'greeting': greeting,
        'description': description
    })