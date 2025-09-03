from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406453606',
        'name': 'Shelia Vellicita',
        'class': 'PBP KI'
    }

    return render(request, "main.html", context)
