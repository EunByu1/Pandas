# pandas 불러오기
import pandas as pd

# 딕셔너리 만들고, 변수 dict_data에 저장 
dict_data = {'a':1, 'b':2, 'c':3}

# 판다스 Series()함수로 dictionary를 Series로 변환 후 변수 sr에 저장 
sr = pd.Series(dict_data)

# sr의 자료형 출력
print("type(sr) : ",type(sr))

# 변수 sr에 저장되어 있는 시리즈 객체 출력
print(sr)
