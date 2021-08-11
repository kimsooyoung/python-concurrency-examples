# Code from InfLearn
# https://www.inflearn.com/course/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A4%91%EA%B8%89-%EC%9D%B8%ED%94%84%EB%9F%B0-%EC%98%A4%EB%A6%AC%EC%A7%80%EB%84%90/dashboard

# Chapter06-01
# Concurrency)
# Iterator, Generator

# Python Iterable types
# for, collections, text file, List, Dict, Set, Tuple, unpacking, *args

# 반복 가능한 이유? 내부적으로 iter(x) 함수 호출
t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# for 반복
for c in t:
    print(c)

print()

# while 반복
w = iter(t)

# print(next(w))
# print(next(w))
# print(next(w))
# print(next(w))
# print(next(w))

while True:
    try:
        print(next(w))
    except StopIteration:
        break

# 위와 같이 쓰는 것은 귀찮음, (예외처리 해야 함)

# 반복 형인지 확인하는 방법
from collections import abc

t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(hasattr(t, "__iter__"))
print(isinstance(t, abc.Iterable))
