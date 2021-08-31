# Code from InfLearn
# https://www.inflearn.com/course/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A4%91%EA%B8%89-%EC%9D%B8%ED%94%84%EB%9F%B0-%EC%98%A4%EB%A6%AC%EC%A7%80%EB%84%90/dashboard
#
# Chapter06-05
# Futures 동시성
#
# 2가지 패턴 실습
# concurrent.futures map
# concurrent.futures wait, as_completed

# GIL : 두 개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스 하는 경우 -> 문제점을 방지하기 위해
#       GIL 실행 , 리소스 전체에 락이 걸린다. -> Context Switch(문맥 교환)

# GIL : 멀티프로세싱 사용, CPython

# map은 모든 작업들이 종료되고 나서야 반환을 함
# wait은 시간이 오래 걸리는 것
# 실패하는 것

import os
import time

# from concurrent import futures, wait, as_completed
from concurrent.futures import (
    ProcessPoolExecutor,
    ThreadPoolExecutor,
    wait,
    as_completed,
)

WORK_LIST = [100000, 1000000, 10000000, 1000000000]

# 동시성 합계 계산 메인함수
# 누적 합계 함수(제네레이터)
def sum_generator(n):
    return sum(n for n in range(1, n + 1))


def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    # 시작 시간
    start_tm = time.time()
    futures_list = []

    # 결과 건수
    # ProcessPoolExecutor
    # with ProcessPoolExecutor() as executor:
    with ThreadPoolExecutor() as excutor:
        for work in WORK_LIST:
            # future 반환
            future = excutor.submit(sum_generator, work)
            # 스케쥴링
            futures_list.append(future)
            # 스케쥴링 확인
            print("Scheduled for {} : {}".format(work, future))
            # print()

        result = wait(futures_list, timeout=3)
        # 성공
        print(f"completed task : {result.done}")
        # 실패
        print(f"pending tasks : {result.not_done}")
        # 성공한 것들 결과값 출력
        print([done_future.result() for done_future in result.done])

    # 종료 시간
    end_tm = time.time() - start_tm
    # 출력 포멧
    msg = "\n Result -> {} Time : {:.2f}s"
    # 최종 결과 출력
    print(msg.format(list(result), end_tm))


# 실행
if __name__ == "__main__":
    main()
