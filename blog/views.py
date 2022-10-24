from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("""<html>
    <title>Шарипов Роман</title>
    <h1>Шарипов Роман</h1>
</html>""")
