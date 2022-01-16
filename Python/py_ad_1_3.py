'''
    Section 1
    Multithreading - Thread(1) - Basic
    Keyword - Threading basic
'''

from concurrent.futures import thread
import logging
import threading
import time

# 스레드 실행 함수
def thread_func(name):
    logging.info("Sub-Threa %s: starting", name)
    time.sleep(3)
    logging.info("Sub-Threa %s: finishing", name)

# 스레드는 디버깅이 어렵기 때문에 중간중간에 로그를 찍어줄수 있는 logging을 사용하자!
# 메인영역
if __name__ == "__main__":
    # Logging Format 설정
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")

    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=('First',))
    logging.info("Main-Thread: before running thread")

    # 서브 스레드 실행
    x.start()

    logging.info("Main-Thread: wait for the thread to finish")

    logging.info("Main-Thread: All done")
   