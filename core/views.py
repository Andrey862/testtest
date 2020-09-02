from django.shortcuts import render
from .models import Counter
# Create your views here.

def home(request):
    c = Counter.objects.get(pk=1)
    t=c.value
    c.value += 1
    c.save()
    return render(request, 'core/index.html', {'title': 'home page', 'counter': t})
    