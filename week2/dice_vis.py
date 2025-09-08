import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm

font_path = '/Users/soyee/Library/Fonts/NanumGothic-Regular.ttf'
fontprop = fm.FontProperties(fname=font_path)

mpl.rc('font', family=fontprop.get_name())
mpl.rc('axes', unicode_minus=False)

n = 10_000
dice = np.random.randint(1, 7, size=n)
unique, counts = np.unique(dice, return_counts=True)
probs = counts / n

print('주사위 던지기 결과 빈도')
print(dict(zip(unique, counts)))

print('\n주사위 확률(추정)')
print(dict(zip(unique, probs)))

plt.figure()
plt.bar(unique, counts)
plt.title('주사위 10,000회 결과(빈도)', fontproperties=fontprop)
plt.xlabel('눈', fontproperties=fontprop)
plt.ylabel('빈도', fontproperties=fontprop)
plt.show()
