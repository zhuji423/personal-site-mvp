---
title: "简单分类模型训练demo"
date: "2026-04-27"
category: "深度学习与机器学习"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\简单分类模型训练demo\\简单分类模型训练demo.md"
---
# 简单分类模型训练demo
import numpy as npimport pandas as pdfrom sklearn import metricsfrom sklearn.model_selection import train_test_splitfrom sklearn.neighbors import KNeighborsClassifierfrom sklearn.linear_model import LogisticRegressionfrom sklearn.tree import DecisionTreeClassifierfrom sklearn.svm import SVCdef main():    """    主函数 简单模型训练    """    # 导入数据集    iris_local = pd.read_csv("./data/dataset/iris.csv", usecols=[0, 1, 2, 3, 4])  # 选择特征列、标签列    iris_local = iris_local.dropna()  # 丢弃含空值的行、列    print(iris_local.head())  # 查看前几行    # 载入特征和标签集    X = iris_local[['fea_a', 'fea_b', 'fea_c', 'fea_d']]    y = iris_local['res_real']    # 划分训练集(70%)、测试集(30%)    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)    print("X_train shape: {}, y_train shape: {}, X_test shape: {}, y_test shape: {}" \          .format(X_train.shape, y_train.shape, X_test.shape, y_test.shape))    # 看下特征数据分布    print(iris_local.describe())    # 在训练集训练模型  常见分类模型：https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/3PtAlLBfxz6cN0    model = SVC()  # svm模型    # model = LogisticRegression()  # lr模型    # model = KNeighborsClassifier(n_neighbors=3)  # knn模型    # model = DecisionTreeClassifier()  # 决策树模型    model.fit(X_train, y_train)    # 在测试集验证模型效果    prediction = model.predict(X_test)    print('accuracy: {:.3f}'.format(metrics.accuracy_score(prediction, y_test)))    # 预测单条数据    X_new = np.array([[5, 2.9, 1, 0.2]])    prediction = model.predict(X_new)    print('data: {}, res: {}'.format(X_new[0], prediction[0]))if __name__ == '__main__':    main()特征分析 

