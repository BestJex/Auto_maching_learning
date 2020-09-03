import matplotlib.pyplot as plt
import numpy as np
import itertools
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score, confusion_matrix
from sklearn.metrics import roc_curve, auc,recall_score  #

# 绘制混淆矩阵函数

# 模型性能评估
def model_performance_evaluation(model_name, test, pred, spend_time):
    acc = accuracy_score(test, pred)
    print(model_name, '| 准确率: %.4f' % acc)
    pred = pred.astype('float64')
    false_positive_rate, true_positive_rate, thresholds = roc_curve(test, pred)
    roc_auc = auc(false_positive_rate, true_positive_rate)
    print(model_name, '| AUC: %.4f' % roc_auc)
    cm = confusion_matrix(test, pred)
    miss_report = cm[0][1] / (1.0 * cm[0][1] + cm[1][1])
    false_report = cm[1][0] / (1.0 * cm[0][0] + cm[1][0])
    print(model_name, "| 漏报率为：%.4f" % miss_report)
    print(model_name, "| 误报率为：%.4f" % false_report)
    print(model_name, "| 训练时长（秒）：%.4f" % spend_time)
    return acc, roc_auc, miss_report, false_report, spend_time


