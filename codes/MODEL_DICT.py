
MODEL_DICT={
    '分类':{
        '朴素贝叶斯':'from sklearn.naive_bayes import GaussianNB',
        '决策树':'from sklearn.tree import DecisionTreeClassifier',
        '支持向量机':'from sklearn.svm import SVC',
        '神经网络':'from sklearn.neural_network import MLPClassifier'
    },
    '回归':{
        '线性回归':'from sklearn.linear_model import LinearRegression',
        '逻辑回归':'from sklearn.linear_model import LogisticRegression',
        '决策树':'from sklearn.tree import DecisionTreeRegressor',
        '支持向量机':'from sklearn.svm import SVR',
        '神经网络':'from sklearn.neural_network import MLPRegressor'
    },
    '聚类':{
        'K-means':'from sklearn.cluster import KMeans'
    },
    'ROC曲线':'plot_ROC_curve.py',
    '混淆矩阵':'plot_confusion_matrix.py'
}
if __name__=='__main__':
    pass

