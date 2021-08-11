# Code from InfLearn
# https://www.inflearn.com/course/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A4%91%EA%B8%89-%EC%9D%B8%ED%94%84%EB%9F%B0-%EC%98%A4%EB%A6%AC%EC%A7%80%EB%84%90/dashboard
#
# Generator Ex3(중요 함수)
# filterfalse, accumulate, chain, product, product, groupby
import itertools

gen1 = itertools.count(1, 2.5)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# ... 무한

#### Result ####
#
# 1
# 3.5
# 6.0
# 8.5

# 조건
gen2 = itertools.takewhile(lambda n: n < 20, itertools.count(1, 2.5))

for v in gen2:
    print(v)

#### Result ####
#
# 1
# 3.5
# 6.0
# 8.5
# 11.0
# 13.5
# 16.0
# 18.5

# 필터 반대
gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])

for v in gen3:
    print(v)

#### Result ####
#
# 3
# 4
# 5

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 11)])

for v in gen4:
    print(v)

#### Result ####
#
# 1
# 3
# 6
# 10
# 15
# 21
# 28
# 36
# 45
# 55

gen5 = itertools.chain("ABCDE", range(1, 11, 2))
print(list(gen5))

gen6 = itertools.chain(enumerate("ABCDE"))
print(list(gen6))

# 개별
gen7 = itertools.product("ABCDE")
print(list(gen7))

# 연산(경우의 수)
gen8 = itertools.product("ABCDE", repeat=2)
print(list(gen8))

# 그룹화
gen9 = itertools.groupby(sorted("EEXAAABBCCCCDDEEEX"))
# print(list(gen9))

for chr, group in gen9:
    print(chr, " : ", list(group))

print()
