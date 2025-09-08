import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = '/Users/soyee/Library/Fonts/NanumGothic-Regular.ttf'
fontprop = fm.FontProperties(fname=font_path)

n = 50_000

x_norm = np.random.normal(loc=0, scale=1, size=n)
x_unif = np.random.uniform(low=-3, high=3, size=n)
x_exp  = np.random.exponential(scale=1.0, size=n)

for name, arr in [('정규', x_norm), ('균등', x_unif), ('지수', x_exp)]:
    print(f'[{name}] mean={arr.mean():.4f}, std={arr.std():.4f}, '
          f'min={arr.min():.4f}, max={arr.max():.4f}')


# plt.figure()
# plt.hist(x_norm, bins=60)
# plt.title('정규분포 샘플 히스토그램', fontproperties=fontprop)
# plt.xlabel('값', fontproperties=fontprop)
# plt.ylabel('도수', fontproperties=fontprop)
# plt.show()

# plt.figure()
# plt.hist(x_unif, bins=60)
# plt.title('균등분포 샘플 히스토그램', fontproperties=fontprop)
# plt.xlabel('값', fontproperties=fontprop)
# plt.ylabel('도수', fontproperties=fontprop)
# plt.show()

plt.figure()
plt.hist(x_exp, bins=60)
plt.title('지수분포 샘플 히스토그램', fontproperties=fontprop)
plt.xlabel('값', fontproperties=fontprop)
plt.ylabel('도수', fontproperties=fontprop)
plt.show()
