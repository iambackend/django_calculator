from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):
    formula = request.GET.get('formula')

    # run formula
    ans = eval(formula)

    return render(request, 'result.html', {'ans': ans})
