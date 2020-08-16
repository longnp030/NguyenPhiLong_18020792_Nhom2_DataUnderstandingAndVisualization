from nltk.corpus import stopwords

txt = "Để tôi cho mọi người xem con đường tình yêu huyền thoại gắn liền với năm tháng cấp 3 của tôi. Không thể nhớ " \
       "được là tôi đã đi qua đây bao nhiêu lần, nhưng lần nào cũng vậy, cái tâm trí lãng đãng của tôi chả bao giờ để " \
       "ý đến con đường này đẹp thế nào, cũng chả bao giờ mảy may lấy điện thoại ra chụp bao giờ cả. Cho đến khi tôi " \
       "bắt gặp những bức ảnh này, tự thấy bồi hồi và xúc động vô cùng, có gì đó tự hào nữa. Có lẽ là đôi khi chúng " \
       "ta vô tình lãng quên những thứ đẹp đẽ quanh mình, những thứ mà vô hình chung tưởng chừng như rất đỗi thân " \
       "quen để rồi một ngày nhìn lại như tôi đây, thấy bối rối và có một phần trách mình sao không để ý đến nó nhiều " \
       "hơn nữa"
txt = ' '.join([word for word in txt.split() if word not in (stopwords.words("vietnamese"))])
print(txt)
