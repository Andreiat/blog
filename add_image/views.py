from django.shortcuts import render
from .forms import AddImgForm

def add_image(request):
    if request.method == "POST":
        form = AddImgForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if 'img' in request.FILES:
                post.img = request.FILES['img']
                post.save()
    else:
        form = AddImgForm()

    return render(request, 'add_image/add.html', {'form': form})
