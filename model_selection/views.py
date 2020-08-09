from django.shortcuts import render

# Create your views here.
# model_selection  根据请求的参数进行模型选择

def get_datesets_list(request):
    return render(request, "../templates/dist/index.html")

