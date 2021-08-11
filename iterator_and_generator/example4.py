# Code from InfLearn
# https://www.inflearn.com/course/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A4%91%EA%B8%89-%EC%9D%B8%ED%94%84%EB%9F%B0-%EC%98%A4%EB%A6%AC%EC%A7%80%EB%84%90/dashboard
#
# Chapter06-02
# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 => 단일 프로그램 안에서 여러 일을 쉽게 해결
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 => 속도
# 이터레이터, 제네레이터
# Iterator, Generator

# 파이썬 반복 가능한 타입
# for, collections, text file, List, Dict, Set, Tuple, unpacking, *args

# Generator Ex1
def generator_ex1():
    print("Start")
    yield "A Point "
    print("continue")
    yield "B Point "
    print("End")


temp = iter(generator_ex1())

try:
    print(next(temp))
    # Start
    # A Point.
    print(next(temp))
    # continue
    # B Point.
    print(next(temp))
    # End
except StopIteration:
    pass
finally:
    print()


print()

# Generator Ex2
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())

#### Result ####
#
# ['A Point A Point A Point ', 'B Point B Point B Point ']
# <generator object <genexpr> at 0x7fd8dbf05ba0>

print(temp2)
print(temp3)

for i in temp2:
    print(i)

#### Result ####
#
# A Point A Point A Point
# B Point B Point B Point

for i in temp3:
    print(i)

#### Result ####
#
# Start
# A Point A Point A Point
# continue
# B Point B Point B Point
# End
