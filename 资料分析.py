data=[]
count = 0

with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0:
			print(len(data))
print('there are ',len(data),'data')

sum_len = 0
for d in data:
	sum_len = sum_len +len(d)
print('留言平均长度为',sum_len/len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new),'比数小于100')