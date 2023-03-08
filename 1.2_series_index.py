# pandas 불러오기
import pandas as pd

# 리스트 만들고, 변수 list_data에 저장
list_data = ['2019-01-02', 3.14, 'ABC', 100, True]

# 판다스 Series()함수로 list를 Series로 변환 후 변수 sr에 저장
sr = pd.Series(list_data)

# 변수 sr에 저장되어 있는 시리즈 객체 출력
print(sr)

# 변수 idx에 인덱스 배열 저장
idx = sr.index
print("idx : ", idx)

# 변수 val에 데이터 값 배열 저장 
val = sr.values
print("val : ", val)
