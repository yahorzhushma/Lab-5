import numpy as np

X1 = np.ones((1, 12))
X2 = np.random.randint(7, 19, (1, 12))
X3 = np.random.randint(60, 82, (1, 12))
X_ = np.vstack((X1, X2, X3))

X = X_.transpose()
Y = np.random.randint(13.5, 18.6, 12)

XT = np.transpose(X)
a = np.linalg.inv(XT.dot(X)).dot(XT).dot(Y)

print("Оценки уравнения регрессии:\n", a)
CH = X.dot(a)
print("\nПолученные значения:")
print(CH)
print("\nИсходные значения Y:")
print(Y)
