from django.shortcuts import render

# Create your views here.
# Para que Django funcione correctamente se debe registrar la app en el archivo settings
def my_view(request):
  car_list = [
    {"title":"BMW",
    "title":"Mazda"}
  ]
# El contexto permite la comunicacion hacia el template
  context = {
    "car_list": car_list
  }
  return render(request, "my_first_app/car_list.html",context=context)