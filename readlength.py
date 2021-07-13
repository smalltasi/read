data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
print('每一筆留言的平均長度是', sum_len/len(data))

new = []
for n in data:
	if len(n) < 100:
		new.append(n)
print('總共有', len(new), '筆留言字數小於100')
print(new[0])

word = []
for w in data:
	if 'good' in w:
		word.append(w)
print('總共有', len(word), '筆含有good這個詞')

#快寫法
wor = [w for w in data if 'good' in w]
print(len(wor))

count = 0
for review in wor[:3]:   #叫出前三段，並且顯示第幾段
	count += 1
	print(count)
	print(review)
