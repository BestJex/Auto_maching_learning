import os
import pandas as pd
import numpy as np
from utils import MODEL_DICT
'''
流程：   
` 1、从monodb读取用户上传的数据集（已完成）`       
`2、传入需要处理的列(特征列)，以及处理过程函数。  
   * 内置填充缺失值、删除缺失值以及one-hot编码
    - 标准化数据（MinMax），可选参数 `    
` 3、模型构建，传入模型名称、目标列进行构建`
    - 允许用户进行参数搜索，前端用户输入的搜索参数格式为json格式

主函数生成：
- 自动生成代码的代码模块存放于同一个文件夹：
       仅包含功能函数
       
- 主函数预先定义一个代码文件，相关参数通过占位符填充，填充的参数来源于前段输入，包括：主要包括特征列、目标列，文件名
'''


class Models():
    '''

    用于与前端界面交互，获取特征列，以及数据处理步骤。
    根据用户选择的步骤，读取预定义的代码。
    前端返回参数
    {
        target:[],
        features:[],

    }
    '''

    def __init__(self, code_files):
        '''
        参数与前端的用户输入一致
        '''
        self.code_files = code_files
        self.target = None
        self.features =None

    def clean_data(self,df,cols,op,standard=''):
        '''
           自动数据清洗
           df:
           cols:
           op:数据清洗的操作
           '''
        if op == 'fillna':
            df.loc[:, cols].fillna()
        elif op == 'dropna':
            df.loc[:,cols].dropna()
        else:
            df.loc[:,cols].apply(op)
        return df

    def get_code(self,model_type, model_name):
        filename = MODEL_DICT[model_name]
        if model_type == '分类':
            filename = model_name + 'Classifiy'
        elif model_type == '回归':
            filename = model_name + 'Regression'
        filename += '\.py'
        f = open(os.path.join(self.code_files, filename), 'r')
        code = f.read()
        return code
