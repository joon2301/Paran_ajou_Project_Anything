import codecs
from konlpy.tag import Okt
from gensim.models import Word2Vec

okt=Okt()
fread = codecs.open("furniture_data.txt", 'r', 'utf-8')
result = []

while True:
    line = fread.readline()
    if not line: break
    tokenlist = okt.pos(line, stem=True, norm=True)
    temp=[]
    for word in tokenlist:
        if word[1] in ["Noun"]:
            temp.append((word[0]))
        elif word[1] in ["Verb"]:
            temp.append((word[0]))
        elif word[1] in ["Adjective"]:
            temp.append((word[0]))
    if temp:
      result.append(temp)

fread.close()

model = Word2Vec(result, size=100, window=5, min_count=5, workers=4, sg=0)
model.save('word2vec.model')

# 형태소 분석기로 input.txt 어떻게 잘렸는지
"""
fwrite = codecs.open("token.txt", 'w', 'utf-8')

for i in range(len(result)):
    for ii in range(len(result[i])):
        fwrite.write(result[i][ii])
        fwrite.write("\n")

fwrite.close()
"""