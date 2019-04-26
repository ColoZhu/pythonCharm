# 加载线性模型算法库
from sklearn import linear_model

# 创建线性回归模型的对象
clf = linear_model.LinearRegression()
# 利用训练集训练线性模型
X = [[0, 0], [1, 1], [2, 2]]
y = [0, 1, 2]
clf.fit(X, y)
print(clf.coef_)
print(clf.intercept_)
