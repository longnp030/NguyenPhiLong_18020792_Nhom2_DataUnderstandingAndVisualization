import os
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


folder = "raovat/"

pd.set_option('max_rows', None)
df = pd.DataFrame(columns=['price', 'tags'])

for file in os.listdir(folder):
    with open(folder + file, 'r') as txt:
        product = {}
        txt = re.sub("[{}'\[\]\n]", ' ', txt.read()).strip()
        while '  ' in txt:
            txt = txt.replace('  ', ' ')
        price = txt[txt.find('price'):txt.find('seller')].replace(' , ', '').strip().split(' : ')[1]
        tags = txt[txt.find('tags'):].strip().split(' : ')[1].split(' , ')
        if price != 'Thương lượng':
            product['price'] = int(price.replace('.', ''))
        else:
            product['price'] = -1
        product['tags'] = tags

        df = df.append(pd.DataFrame.from_dict(product, orient='index').T, ignore_index=True).explode('tags')

df = df.groupby('tags')['price'].apply(set).reset_index(name='price range')
price_range = df['price range'].sort_values().apply(lambda x: sorted(x)).reset_index()
del df['price range']
df['price range'] = price_range['price range'].to_numpy()

to_compare = df.loc[np.array(list(map(len, df['price range'].values))) > 15]  # Lay nhung thang nao co khoang gia dao dong pho bien nhat de so sanh
pd.set_option('max_colwidth', None)
print(to_compare)

#ax = to_compare[['price range']].applymap(lambda x: x[0]).plot.bar(rot=0, color=list('br'))
ax = to_compare[['price range']].unstack().apply(pd.Series).\
    plot.bar(rot=0, fontsize=8, cmap=plt.cm.plasma, width=1, figsize=(17, 10))

ax.set_xticklabels(to_compare['tags'], rotation=10)
ax.set_ylabel("Giá (chục triệu đồng)")
ax.set_xlabel("Loại")
ax.set_title("So sánh khoảng giá của các loại hàng phổ biến nhất")
plt.show()
