from django.db import models

# Create your models here.
import mongoengine


class UserModel(mongoengine.Document):
    username = mongoengine.StringField(max_length=16)
    password= mongoengine.StringField(max_length=16)
    phone= mongoengine.StringField(max_length=16)
    email= mongoengine.StringField(max_length=16)
    authority=mongoengine.BooleanField(default=False)#会员权限
    dataset=mongoengine.ListField()
#
# import pandas as pd
# import os
#
# print(os.path)
# df = pd.read_csv("Datasets/hour.csv")
# data = {i: df[i].tolist() for i in df.columns}
# UserModel.objects.create(
#     username='admin',
#     password='admin',
#     phone='123456',
#     email='123456',
#     authority=True,
#     dataset=[{"hour": data,"name":"hour"}]
# )
#
#
#

