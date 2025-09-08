import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = '/Users/soyee/Library/Fonts/NanumGothic-Regular.ttf'
fontprop = fm.FontProperties(fname=font_path)
plt.rc('font', family=fontprop.get_name())
plt.rc('axes', unicode_minus=False)

n = 300
df = pd.DataFrame({
    'student_id': np.arange(1, n+1),
    'grade': np.random.choice(['A','B','C','D'], size=n, p=[0.2,0.4,0.3,0.1]),
    'math': np.random.normal(70, 10, size=n).clip(0, 100),
    'eng':  np.random.normal(72, 12, size=n).clip(0, 100),
    'kor':  np.random.normal(75, 8, size=n).clip(0, 100),
})
df.loc[np.random.choice(df.index, size=20, replace=False), 'eng'] = np.nan

print()
print(df.info())
print()

mask = (df['math'] > df['eng'].fillna(-1)) & (df['kor'] >= 80)

grouped = df.groupby('grade').agg(
    math_mean=('math','mean'),
    eng_mean=('eng','mean'),
    kor_mean=('kor','mean'),
    count=('student_id','count')
).reset_index()

grade_counts = df['grade'].value_counts().sort_index()

plt.figure()
plt.bar(grade_counts.index, grade_counts.values)
plt.title('등급별 학생 수 (이산 카테고리)', fontproperties=fontprop)
plt.xlabel('등급', fontproperties=fontprop)
plt.ylabel('명', fontproperties=fontprop)
plt.show()
