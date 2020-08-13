from django.shortcuts import render
from django.http import JsonResponse
from utils.data_process import  data_process
# Create your views here.
# model_selection  根据请求的参数进行模型选择

def get_datesets_list(request):
    return render(request, "../templates/dist/index.html")

def get_data_list(request):
    dp=data_process()
    lists=[list(i.keys())[0] for i in dp.user['dataset']]
    return JsonResponse({"data_list":lists}, safe=False)
