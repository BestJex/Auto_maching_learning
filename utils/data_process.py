'''
数据操作
上传数据文件
选择数据数据
删除数据文件
'''

import pymongo
import pandas as pd
from model_selection.models import UserModel
import os
class data_process():
    def __init__(self,url="localhost",port=27017,database="AML",collection="user_model",username="admin"):
        self.client = pymongo.MongoClient(url, port)
        self.collection=self.client[database][collection]
        self.username=username
        self.user = self.collection.find_one({"username": self.username})
        self.columns=[]
    def upload(self,file_path):
        '''

        :param file_path: 用户上传的文件路径
        :return:是否成功上传的bool值
        '''
        #文件后缀检查
        postfix=os.path.split(file_path)[-1].split(".")
        if postfix[1]=='xls' or postfix[1]=='xlsx':
            df=pd.read_excel(file_path)
        else:
            try:
                df = pd.read_csv(file_path)
            except Exception as e:
                print("上传文件失败:",e.__traceback__)
                return False
        #将dataframe转换为字典形式
        data = {i: df[i].tolist() for i in df.columns}
        #获取传入文件去掉后缀的名称
        file_name=postfix[0]
        self.collection.update_many({'username':self.username},{"$push":{"dataset":{file_name:data,"name":file_name}}})
        return True
    def get_dataset(self,dataset_name):
        '''

        :param dataset_name:
        :return: 获取数据集转换为DataFrame
        '''
        my_dataset=self.user['dataset'][dataset_name]
        self.columns=my_dataset.keys()
        return pd.DataFrame(my_dataset)

    def delete(self,dataset_name):

        self.collection.update({"username":self.username},{"$pull":{"dataset":{"name":dataset_name}}})


#if __name__=="__main__":

    # path="../Datasets/day.csv"
    # dp=data_process()
    # dp.delete("hour")#删除admin用户下的hour文件
    # dp.upload(path)#将day.csv上传
    # a=dp.get_dataset("hour")
    # print(pd.DataFrame(a))

