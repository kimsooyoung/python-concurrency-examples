# Code from InfLearn
# https://www.inflearn.com/course/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A4%91%EA%B8%89-%EC%9D%B8%ED%94%84%EB%9F%B0-%EC%98%A4%EB%A6%AC%EC%A7%80%EB%84%90/dashboard

# Generator 패턴
# 1.지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 후 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2.단위 실행 가능한 코루틴(Coroutine) 구현과 연동
# 3.작은 메모리 조각 사용


class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(" ")

    def __iter__(self):
        # print('Called __iter__')
        for word in self._text:
            yield word  # 제네레이터 사용, 예외처리를 해준다.

    def __repr__(self):
        return "WordSplit(%s)" % (self._text)


wg = WordSplitGenerator("Do today what you could do tomorrow")

wt = iter(wg)

# print(wt)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt))
# print(next(wt))
# print(next(wt))
# print(next(wt))

print()

for val in wt:
    print(val)


#### Result ####
#
# Do
# today
# what
# you

# could
# do
# tomorrow
