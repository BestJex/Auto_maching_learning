from sklearn.model_selection import train_test_split
from codes.evaluation import *
import pandas as pd
import numpy as np

{}

FILE_PATH={}#dataset_name
if FILE_PATH.split('.')[-1]=='xls' or FILE_PATH.split('.')[-1]=='xlsx':
    DF=pd.read_excel(FILE_PATH)
else:
    DF=pd.read_csv(FILE_PATH)
MODEL={}
y =DF[{}]
X = DF[{}]
# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
X.apply()

# 模型训练
model = MODEL.fit(X_train, y_train)
#预测
y_pred = model.predict(X_test)
#模型评估
# 绘制混淆矩阵
cnf_matrix = confusion_matrix(y_test, y_pred)
np.set_printoptions(precision=len(y.unique))  # 设置打印数量的阈值
class_names = y.unique()
test_report = classification_report(y_test, y_pred)
print(test_report)
plot_confusion_matrix(cnf_matrix, classes=class_names, title='Confusion matrix')
plot_ROC_curve(y_test, y_pred)
