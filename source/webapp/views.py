from django.shortcuts import render


def calculate(request):
    if request.method == "GET":
        return render(request, "form_view.html")
