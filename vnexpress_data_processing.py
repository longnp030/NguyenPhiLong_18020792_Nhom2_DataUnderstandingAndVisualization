import pandas as pd
import os
import re
from underthesea import word_tokenize as wt
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

folder = "vnexpress/"

viet_apb = re.compile("[^aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiI"
                      "ìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuU"
                      "ùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ ]")

df = pd.DataFrame(columns=['categories', 'content'])

for file in os.listdir(folder):
    with open(folder + file, 'r') as txt:
        article = {}
        txt = txt.read()[1:len(txt.read()) - 1]
        neccessary_info = [re.sub("['\[\]]", '', info.strip()) for info in
                           txt.split(',\n')[1:3]]  # Lay 2 cot danh muc va noi dung
        for info in neccessary_info:
            article[info.split(': ')[0]] = ''.join(info.split(': ')[1:])
        article['categories'] = article['categories'].split(', ')
        article['content'] = re.sub(viet_apb, '', article['content']).strip()
        while '  ' in article['content']:
            article['content'] = article['content'].replace('  ', ' ')
        article['content'] = [wt(article['content'])]  # Tach tu
        # article['content'] = [article['content'].split(' ')]
        df = df.append(pd.DataFrame.from_dict(article, orient='index').T, ignore_index=True)

# categories = df.groupby('categories').nunique()  // Lay thang nao nhieu nhat lam vi du de danh gia

df = df[df['categories'] == 'Giáo dục']
df = df.reset_index(drop=True)
words = [df.loc[i, 'content'] for i in range(df['categories'].size)][0]

fdist = FreqDist(words)
count_frame = pd.DataFrame(fdist, index=[0]).T
count_frame.columns = ["Count"]
counts = count_frame.sort_values("Count", ascending=False)

fig = plt.figure(figsize=(12, 6))
ax = fig.gca()
counts["Count"][:30].plot(kind="bar", ax=ax)
ax.set_title("Tần suất các từ phổ biến nhất xuất hiện trong danh mục 'Giáo dục'")
ax.set_ylabel("Tần suất")
ax.set_xlabel("Từ")
plt.show()
