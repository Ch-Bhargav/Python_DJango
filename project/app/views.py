from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'home.html')

def my_form_view(request):
    if request.method == 'POST':
        # Retrieve the data from the form
        textbox_data = request.POST.get('my_textbox')

        Model.objects.create(name=textbox_data)

        return render(request, 'home.html')