from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.http import require_http_methods
from utils.dataset_process import  dataset_process
# Create your views here.
# model_selection  根据请求的参数进行模型选择

def get_datesets_list(request):
    return render(request, "../templates/dist/index.html")

@require_http_methods(['GET'])
def get_data_list(request):
    '''
    获取用户上传的所有数据集名称
    '''
    dp=dataset_process()
    lists=[list(i.keys())[0] for i in dp.user['dataset']]
    return JsonResponse({"data_list":lists}, safe=False)

@require_http_methods(['GET'])
def show_dataset(request):
    '''
    根据用户选择的数据集，展示所有数据
    '''
    dp=dataset_process()
    df=dp.get_dataset('day')
    df_json=df.to_json()
    return HttpResponse(df_json)
