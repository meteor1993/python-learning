import pandas as pd

# 数据导入
data_train = pd.read_csv("train.csv")

# 数据查看
print(data_train.info())

pd.set_option('display.max_columns', None)
print(data_train.describe())

print(data_train)

print(data_train['SibSp'] + data_train['Parch'])

print(data_train['SibSp'] + data_train['Parch'] + 1 - data_train['Survived'])

print(data_train['Survived'] > (data_train['SibSp'] + data_train['Parch']))

# 按列统计
print(data_train.count())
# 按行统计
print(data_train.count(axis=1))
# 某一列单独统计
print(data_train['Age'].count())

# 按列求和
print(data_train.sum())
# 按行求和
print(data_train.sum(axis=1))

print(data_train.mean())

print(data_train.max())
print('-----------------------------------------')
print(data_train.min())

print(data_train.median())

print(data_train.mode())
# 单独获取某列众数
print(data_train['Sex'].mode())

print(data_train.var())

print(data_train.std())

print(data_train.quantile(0.25))
print('-----------------------------------------')
print(data_train.quantile(0.5))

print(data_train.corr(method='pearson'))