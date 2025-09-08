import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = '/Users/soyee/Library/Fonts/NanumGothic-Regular.ttf'
fontprop = fm.FontProperties(fname=font_path)
plt.rc('font', family=fontprop.get_name())
plt.rc('axes', unicode_minus=False)

date_index = pd.date_range(start='2025-09-08', periods=200, freq='D')
ts = pd.DataFrame({
    'date': date_index,
    'value': (np.linspace(0, 10, len(date_index)) + np.random.normal(0, 1, len(date_index))).cumsum()
})
ts = ts.set_index('date')

weekly = ts.resample('W').mean()

rolling7 = ts.rolling(window=7, min_periods=1).mean()

plt.figure()
plt.plot(ts.index, ts['value'], label='일간 값')
plt.title('일간 시계열 값', fontproperties=fontprop)
plt.xlabel('날짜', fontproperties=fontprop)
plt.ylabel('값', fontproperties=fontprop)
plt.legend()
plt.show()

plt.figure()
plt.plot(rolling7.index, rolling7['value'], color='orange', label='7일 평균')
plt.title('7일 롤링 평균 (시계열)', fontproperties=fontprop)
plt.xlabel('날짜', fontproperties=fontprop)
plt.ylabel('값', fontproperties=fontprop)
plt.legend()
plt.show()
