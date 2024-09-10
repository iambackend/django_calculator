from django.shortcuts import render
import traceback

# Create your views here.

def home(request):
    formula = request.GET.get('formula')
    if formula is None:
        return render(request, 'home.html', {})

    # run formula
    trace = None
    try:
        ans = eval(formula)
    except Exception as e:
        ans = 'Error'
        trace = traceback.format_exc()

    return render(request, 'home.html', {'ans': ans, 'formula': formula, 'trace': trace or None})
