# Chapter06-03
# 흐름제어, 병행성(Concurrency)
# 코루틴(Coroutine)

# yield : 메인 <-> 서브
# 코루틴 제어, 상태, 양방향 전송
# yield from

# 서브루틴 : 메인루틴에서 호출 -> 서브루틴에서 수행(흐름제어)
# 코루틴 : 루틴 실행 중 중지 ->  동시성 프로그래밍
# 코루틴 : 쓰레드에 비해 오버헤드 감소
# 쓰레드 : 싱글쓰레드 -> 멀티쓰레드 -> 복잡 -> 공유되는 자원 -> 교착 상태 발생 가능성, 컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가

# 코루틴 Ex1
def coroutine1():
    print(">>> coroutine started.")
    i = yield
    print(">>> coroutine received : {}".format(i))


# 제네레이터 선언
cr1 = coroutine1()

print(cr1, type(cr1))

# yield 지점 까지 서브루틴 수행
next(cr1)
# >>> coroutine started.

# 기본 전달 값 None
# next(cr1)
# >>> coroutine received : None

# 값 전송
cr1.send(100)
# send = value sending + next

# 잘못된 사용
# next 없이 바로 send

# cr2 = coroutine1()
# cr2.send(100) # 예외 발생
