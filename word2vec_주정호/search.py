from konlpy.tag import Okt
from gensim.models import Word2Vec

model = Word2Vec.load('word2vec.model')
okt=Okt()
furniture_category = []


search = "다리가 긴 의자"
"""
if search in furniture_category:
    print("검색어와 가장 유사한 가구는 " + search)
    print("검색어와 유사도는 1")
    quit()
"""
search_tokenlist = okt.pos(search, stem=True, norm=True)
search_token=[]
for word in search_tokenlist:
    if word[1] in ["Noun"]:
        search_token.append((word[0]))
    elif word[1] in ["Verb"]:
        search_token.append((word[0]))
    elif word[1] in ["Adjective"]:
        search_token.append((word[0]))

"""
print(search_tokenlist) # search 형태소 분석
print(search_token) # 실제 검색에 사용한 search
"""

how_many_result = 20
search_result=model.wv.most_similar(positive=search_token,topn=how_many_result)

"""
for i in range(0,how_many_result):
    if search_result[i] in furniture_category:
        print("검색어와 가장 유사한 가구는 " + search_result[i][0])
        print("검색어와 유사도는 " + search_result[i][1])
        break
"""

print(search_result)