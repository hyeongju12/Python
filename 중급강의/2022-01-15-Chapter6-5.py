# Chapter6-4
# Futures(동시성)
# 비동기 작업 실행
# 지연시간(block) CPU 및 리소스 낭비 방지 -> (FILE) Network I/O 관련 작업 할때 동시성 작업 권장
# 비ㅣ동기 작업과 적합한 프로그램일 경우 압도적 성능 향상 

from asyncio import as_completed
import threading
import multiprocessing

# concurrent.futures
# 1. 멀티스레딩/멀티프로세싱 api 통일 -> 사용하기 쉬움
# 2. 실행중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백 추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념

# 2가지 패턴 
# concurrent.futures 사용법1
# concorrent.futures 사용법2

# GIL : 두개 이상의 스레드가 동시에 실행 될때 하나의 자원을 액세스 하는 경우 -> 문제점을 방지
#       GIL 실행(GLOBLA INTERFACE LOCK), 리소스 전체에 락이 걸린다. -> Context Switch(문맥 교환)

# GIL : 멀티프로세싱 사용, Cpython

import os
import time
from concurrent.futures import wait, as_completed, ThreadPoolExecutor, ProcessPoolExecutor

WORK_LIST = [100000, 1000000, 10000000, 100000000]

# 동시성 합계 계산 메인 함수
# 누적 합계 함수(제너레이터)

def sum_generator(n):
    return sum(n for n in range(1, n+1))

def main():
    worker = min(10, len(WORK_LIST))

    # 시작시간
    start_tm = time.time()
    futures_list = []

    # 결과 건수
    # ProcessPoolExcutor
    with ThreadPoolExecutor() as excutor:
        for work in WORK_LIST:
            # future 반환
            future = excutor.submit(sum_generator, work)
            # 스케쥴링
            futures_list.append(future)
            print('Scheduled for {} : {}'.format(work, future))
            print()

        # result = wait(futures_list, timeout=7)
        # # 성공
        # print('Completed Tasks : ' + str(result.done))

        # # 실패
        # print('Pending ones after wating for 7seconds : ' + str(result.not_done))

        # # 결과 값 출력
        # print([future.result() for future in result.done])

        # as_completed 결과 출력
        for future in as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled

            # future 결과 확인
            print('Future Result: {}, Done : {}'.format(result, done))
            print('Future Cancelled: {}'.format(cancelled))

    # # 종료시간
    # end_tm = time.time() - start_tm
    # # 출력 포맷
    # msg = '\n time : {:.2f}s'
    # # 최종 결과 줄력
    # print(msg.format(list(result), end_tm))

# 실행
if __name__ == '__main__':
    main()
