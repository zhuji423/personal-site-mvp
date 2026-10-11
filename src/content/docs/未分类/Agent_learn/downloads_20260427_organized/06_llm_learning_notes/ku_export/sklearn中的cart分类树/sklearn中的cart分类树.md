---
title: "sklearn中的cart分类树"
description: "三、sklearn cart树 简单应用1. 测试集、训练集划分from sklearn import modelselection 数据划分trainx, testx, trainy, testy = modelselection.tra"
date: "2026-04-28"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\sklearn中的cart分类树\\sklearn中的cart分类树.md"
---
# sklearn中的cart分类树
本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间一、树的定义node_count : 节点总数目。包括：internal nodes + leavescapacity：<=node_countmax_depth: 最大深度children_left：children_left[i]表示node i的左节点.children_right: children_right[i]表示node i的右节点.feature: feature[i]表示internal node i进行分割的feature.threshold:threshold[i]表示internal node i的threshold.value:包含了每个节点的预测值impurity：impurity[i]表示node i的不纯度impurity.n_node_samples：n_node_samples[i]表示node i下所有的训练样本数.weighted_n_node_samples: weighted_n_node_samples[i]表示node i的样本权重。二、训练时(fit)的参数

| 参数 | 说明 |
| --- | --- |
| criterion | 用来权衡划分的质量。缺省‘gini’： 即 Gini impurity。 或者‘entropy’： 信息增益. 其实现可参考： _creterion.pyx, 包含了分类和回归.缺省为：gini. |
| splitter | 划分方式有三种：best, presort-best, random. 它的实现在： _splitter.pyx，它会根据criterion对每个节点进行划分. best是最优划分，random: 随机划分. 缺省为：best |
| max_features | 当进行best划分时，会考虑max_features. 缺省: None |
| max_depth | 树的最大深度。缺省为：None |
| min_samples_split | 对于一个中间节点（internal node），必须有min个samples才对它进行分割。缺省为：2 |
| min_samples_leaf | 对一个叶子节点（left node），必须有min个samples认为它是叶子节点。缺省为：1 |
| min_weight_fraction_leaf | 在一个叶子节点上，输入样本必须有min个最小权重块。缺省为：0 |
| max_leaf_nodes | 以最好优先（best-first）的方式使用该值生成树。如果为None:不限制叶子节点的数目。如果不为None，则忽略max_depth。缺省为：None |
| class_weight | 分类和权重以这种形式关联在一起：{class_label: weight}。如果示给定，那么所有的分类都认为具有权重1. 对于多分类总题，可以给出一个list of dicts，顺序与y列一致。“balanced”模式：自动调整权重。n_samples / (n_classes * np.bincount(y))详见文档。 |
| random_state | 随机种子 |
| presort | bool, 是否对数据进行预先排序，以便在fitting时加快最优划分。对于大数据集，使用False，对于小数据集，使用True. |

三、sklearn cart树 简单应用1. 测试集、训练集划分from sklearn import model_selection# 数据划分train_x, test_x, train_y, test_y = model_selection.train_test_split(dataSet, target, test_size=0.1, random_state=0)# train_data：所要划分的样本特征集

# train_target：所要划分的样本结果

# test_size：样本占比，如果是整数的话就是样本的数量。若为整数时，表示训练样本的样本数。若为None时，train_size自动被设置成0.75。

# random_state：是随机数的种子。 随机数种子：其实就是该组随机数的编号，在需要重复试验的时候，保证得到一组一样的随机数。比如你每次都填1，其他参数一样的情况下你得到的随机数组是一样的。但填0或不填，每次都会不一样。

# stratify：是为了保持split前类的分布。比如有100个数据，80个属于A类，20个属于B类。如果train_test_split(... test_size=0.25, stratify = y_all), 那么split之后数据如下：  training: 75个数据，其中60个属于A类，15个属于B类。  testing: 25个数据，其中20个属于A类，5个属于B类。 

用了stratify参数，training集和testing集的类的比例是 A：B= 4：1，等同于split前的比例（80：20）。通常在这种类分布不平衡的情况下会用到stratify。

将stratify=X就是按照X中的比例分配， 将stratify=y就是按照y中的比例分配 。若为None时，划分出来的测试集或训练集中，其类标签的比例也是随机的。

2. cart树 模型训练from sklearn import tree

# 定义决策树分类器
clf = tree.DecisionTreeClassifier()
# 训练分类器
clf.fit(train_x, train_y)

3. 模型可视化import graphviz

# 可视化为pdf
graph = graphviz.Source(dot_data)
graph.render("./data/graph/zjtest")



import pydotplus

# 可视化为pdf 方法二
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf("./data/graph/zjtest2.pdf")

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=c3c2cb3ad13c8dde808ff4623ffe8bf8)

4. 模型保存与加载# 保存训练的模型
joblib.dump(clf, "./data/model/zjtest.m" )

# 加载保存的模型
clf = joblib.load("zjtest.m") 

5. 测试完整代码

#!/usr/bin/python# -*- coding: utf-8 -*-from sklearn import datasetsfrom sklearn import model_selectionfrom sklearn import treeimport pydotplusimport graphvizfrom sklearn.externals import joblibdef main():    # 使用iris数据集 iris = datasets.load_iris() dataSet, target = iris.data, iris.target    # 数据划分 train_x, test_x, train_y, test_y = model_selection.train_test_split(dataSet, target, test_size=0.1, random_state=0)    # 定义决策树分类器 clf = tree.DecisionTreeClassifier()    # 训练分类器 clf.fit(train_x, train_y)    # 预测测试样本 pre_y = clf.predict(test_x) print('预测结果：\n{}'.format(pre_y)) print('实际结果：\n{}'.format(test_y)) dot_data = tree.export_graphviz(clf, out_file=None, feature_names='iris', filled=True, rounded=True, special_characters=True)    # 可视化为pdf graph = graphviz.Source(dot_data) graph.render("./data/graph/zjtest")    # 可视化为pdf 方法二 graph = pydotplus.graph_from_dot_data(dot_data) graph.write_pdf("./data/graph/zjtest2.pdf")    # 保存训练的模型 joblib.dump(clf, "./data/model/zjtest.m" ) # clf = joblib.load("zjtest.m") # 加载保存的模型if __name__ == '__main__':    main()四、应用中碰到的具体问题1. 数据不均衡问题 偏斜类遇到正负样本数量差距较大的情况，设置fit() 参数 'class_weight': 'balanced'

基本思路是让正负样本在训练过程中拥有相同的话语权，比如利用采样与加权等方法。

1.1 采样采样分为上采样（Oversampling）和下采样（Undersampling），上采样是把小众类复制多份，下采样是从大众类中剔除一些样本，或者说只从大众类中选取部分样本。

随机采样最大的优点是简单，但缺点也很明显。上采样后的数据集中会反复出现一些样本，训练出来的模型会有一定的过拟合；而下采样的缺点显而易见，那就是最终的训练集丢失了数据，模型只学到了总体模式的一部分。

1.2 数据合成数据合成方法是利用已有样本生成更多样本，这类方法在小数据场景下有很多成功案例，比如医学图像分析等。

最常用的SMOTE为每个小众样本合成相同数量的新样本，这带来一些潜在的问题：一方面是增加了类之间重叠的可能性，另一方面是生成一些没有提供有益信息的样本。

1.3 加权 对不同分类分错的代价不同，这种方法的难点在于设置合理的权重，实际应用中一般让各个分类间的加权损失值近似相等。

2. 参数优化及选择 GridSearchCV列出要测试的参数，然后Grid Search使用穷举搜索，GridSearchCV用于系统地遍历多种参数组合，通过交叉验证确定最佳效果参数。

class sklearn.model_selection.GridSearchCV(estimator, param_grid, scoring=None, fit_params=None, n_jobs=1, iid=True, refit=True, cv=None, verbose=0, pre_dispatch=‘2*n_jobs’, error_score=’raise’, return_train_score=’warn’)

参数：

estimator 选择使用的分类器

param_grid 需要最优化的参数的取值，值为字典或者列表

scoring=None 模型评价标准，默认None,这时需要使用score函数；或者如scoring='roc_auc'，根据所选模型不同，评价准则不同

fit_params=None

n_jobs=1 n_jobs: 并行数，int：个数,-1：跟CPU核数一致, 1:默认值

iid=True iid:默认True,为True时，默认为各个样本fold概率分布一致，误差估计为所有样本之和，而非各个fold的平均

refit=True 默认为True,程序将会以交叉验证训练集得到的最佳参数，重新对所有可用的训练集与开发集进行，作为最终用于性能评估的最佳模型参数。即在搜索参数结束后，用最佳参数结果再次fit一遍全部数据集

cv=None 交叉验证参数，默认None，使用三折交叉验证。指定fold数量，默认为3

verbose=0 日志冗长度，int：冗长度，0：不输出训练过程，1：偶尔输出，>1：对每个子模型都输出

pre_dispatch=‘2*n_jobs’ 指定总共分发的并行任务数。当n_jobs大于1时，数据将在每个运行点进行复制，这可能导致OOM，而设置pre_dispatch参数，则可以预先划分总共的job数量，使数据最多被复制pre_dispatch次

error_score=’raise’

return_train_score=’warn’ 如果“False”，cv_results_属性将不包括训练分数



GridSearchCV属性：

（1）cv_results_ : dict of numpy (masked) ndarrays 具有键作为列标题和值作为列的dict，可以导入到DataFrame中。注意，“params”键用于存储所有参数候选项的参数设置列表。

（2）best_estimator_ : estimator 通过搜索选择的估计器，即在左侧数据上给出最高分数（或指定的最小损失）的估计器。 如果refit = False，则不可用。

（3）best_score_ : float best_estimator的分数

（4）best_params_ : dict 在保存数据上给出最佳结果的参数设

（5）best_index_ : int 对应于最佳候选参数设置的索引（cv_results_数组）。

search.cv_results _ ['params'] [search.best_index_]中的dict给出了最佳模型的参数设置，给出了最高的平均分数（search.best_score_）。

（6）scorer_ : function Scorer function used on the held out data to choose the best parameters for the model.

（7）n_splits_ : int The number of cross-validation splits (folds/iterations).

（8）grid_scores_：给出不同参数情况下的评价结果



应用：

model = XGBClassifier()               learning_rate = [0.0001,0.001,0.01,0.1,0.2,0.3] #学习率gamma = [1, 0.1, 0.01, 0.001] param_grid = dict(learning_rate = learning_rate,gamma = gamma)#转化为字典格式，网络搜索要求 kflod = StratifiedKFold(n_splits=10, shuffle = True,random_state=7)#将训练/测试数据集划分10个互斥子集 grid_search = GridSearchCV(model,param_grid,scoring = 'neg_log_loss',n_jobs = -1,cv = kflod)#scoring指定损失函数类型，n_jobs指定全部cpu跑，cv指定交叉验证grid_result = grid_search.fit(X_train, Y_train) #运行网格搜索print("Best: %f using %s" % (grid_result.best_score_,grid_search.best_params_))#grid_scores_：给出不同参数情况下的评价结果。best_params_：描述了已取得最佳结果的参数的组合#best_score_：成员提供优化过程期间观察到的最好的评分#具有键作为列标题和值作为列的dict，可以导入到DataFrame中。#注意，“params”键用于存储所有参数候选项的参数设置列表。means = grid_result.cv_results_['mean_test_score']params = grid_result.cv_results_['params']for mean,param in zip(means,params):    print("%f  with:   %r" % (mean,param))3. 分支过多 控制叶结点的样本数设置min_samples_split

# 调用cart模型module_name = "server_offline_cart_qiantai"parameters = {'min_samples_leaf': [0.08, 0.1], 'max_depth': range(5, 15, 1), 'class_weight': ['balanced']}# parameters = {'min_samples_leaf': [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4],# 'max_depth': range(5, 15, 1)}scoring = "roc_auc"# scoring = "precision"cv = 10clf = tree.DecisionTreeClassifier()grid_search = GridSearchCV(clf, parameters, cv=cv, scoring=scoring)grid_search.fit(X, y)logging.info("best_params: %s, best_score: %s" % (grid_search.best_params_, grid_search.best_score_))return grid_search.best_estimator_4. 评价指标 ROC与AUC用分类器预测完后，得到一个二分类的混淆矩阵：

| 真实情况 | 预测结果 |  |
| --- | --- | --- |
|  | 正例 | 反例 |
| 正例 | TP(真正例) | FN(假反例) |
| 反例 | FP(假正例) | TN(真反例) |

准确率(accuracy)所有预测正确的样本占所有样本的比例，但这个指标在类别比例不平衡时不太恰当。

sklearn.metrics.accuracy_score(y_true, y_pred, normalize=True, sample_weight=None)

#normalize：默认值为True，返回正确分类的比例；如果为False，返回正确分类的样本数

查准率(Precision)直观理解为： 在所有预测为正例中，真正正例的比例。（有点绕，多读几遍就好） 

precision(查准率)=TP/(TP+FP)

precision_score(y_true, y_pred, labels=None, pos_label=1, average=‘binary’,sample_weight=None)

查全率(Recall)直观理解为： 在所有真实的正例中，预测为正例的比例。 

recall(查全率)=TP/(TP+FN)

recall_score(y_true, y_pred, labels=None, pos_label=1,average='binary', sample_weight=None)

# average : string, [None, ‘micro’, ‘macro’(default), ‘samples’, ‘weighted’]

F1-score由于Precision和Recall是一对不可调和的矛盾，很难同时提高二者，也很难综合评价。故提出F1来试图综合二者，F1是P和R的调和平均（harmonic mean）： 

F1 = 2 * (precision * recall) / (precision + recall)

f1_score(y_true, y_pred, labels=None, pos_label=1, average=‘binary’, sample_weight=None)

ROC曲线真正例（True Positive Rate，TPR），表示所有正例中，预测为正例的比例： TPR=TP/(TP+FN)

假正例（False Positive Rate，FPR），表示所有负例中，预测为正例的比例： FPR=FP/(TN+FP)



以FPR为横坐标，TPR为纵坐标，那么ROC曲线就是改变各种阈值后得到的所有坐标点 (FPR,TPR) 的连线，画出来如下。红线是随机乱猜情况下的ROC，曲线越靠左上角，分类器越佳。

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=ceeb73a1977ae0ba8a896dc354c51c1f)

AUCAUC（Area Under Curve）就是ROC曲线下的面积。

AUC值越大的分类器，正确率越高。

ROC曲线有个很好的特性：当测试集中的正负样本的分布变化的时候，ROC曲线能够保持不变。  在实际的数据集中经常会出现类不平衡（class imbalance）现象，即负样本比正样本多很多（或者相反），而且测试数据中的正负样本的分布也可能随着时间变化。

应用：sklearn绘制ROC曲线+求AUC

a.分别求ROC和AUC

from sklearn.metrics import roc_curve, aucfpr, tpr, thresholds = roc_curve(y, y_proba, pos_label=2)auc = auc(fpr, tpr)将 fpr 和 tpr 的值用matplotlib绘制即得ROC曲线。

b. 直接求AUC

from sklearn.metrics import roc_auc_scoreroc_auc_score(y_true, y_scores)

