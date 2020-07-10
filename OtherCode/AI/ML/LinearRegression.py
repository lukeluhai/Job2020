

# Code source: Jaques Grobler
# License: BSD 3 clause


import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset 载入糖尿病数据
diabetes = datasets.load_diabetes()

# 对于不同类型的数据集，有三种不同类型的数据集接口。最简单的是样品图像的界面，下面在 样本图片 部分中进行了描述。
# 数据集生成函数和 svmlight 加载器分享了一个较为简化的接口，返回一个由 n_samples * n_features 组成的
#  tuple (X, y) 其中的 X 是 numpy 数组 y 是包含目标值的长度为 n_samples 的数组
# 玩具数据集以及 ‘real world’ 数据集和从 mldata.org 获取的数据集具有更复杂的结构。
# 这些函数返回一个类似于字典的对象包含至少两项：一个具有 data 键（key）的 n_samples * n_features
# 形状的数组（除了20个新组之外except for 20newsgroups）和一个具有 target 键（key）的包含 target
# values （目标值）的 n_samples 长度的 numpy 数组。
# 数据集还包含一些对``DESCR`` 描述，同时一部分也包含 feature_names 和 ``target_names``的特征。
print('数据结构' + str(diabetes.keys()))
print('data维度' + str(diabetes.data.shape))
print('target维度' + str(diabetes.target.shape))
# print(np.stack((diabetes.data,diabetes.target),axis=0))
# Use only one feature
diabetes_X = diabetes.data[:, 2, np.newaxis]
print(diabetes_X)
# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
print(diabetes_X_train)
print(diabetes_X_test)
# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test, color='black',label='x')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3,label='y')

plt.xticks(())
plt.yticks(())
plt.legend()
plt.show()
