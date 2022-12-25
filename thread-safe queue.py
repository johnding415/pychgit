from queue import Queue, Empty
import time
from threading import Thread


def producer(queue):
    for i in range(1, 6):
        print(f'Inserting Item {i} into the queue')
        time.sleep(1)
        queue.put(1)


def consumer(queue):
    while True:
        try:
            item = queue.get()
        except Empty:
            continue
        else:
            print(f'Processing item,{item}')
            time.sleep(2)
            queue.task_down()


def main():
    queue = Queue()
    producer_thread = Thread(target=producer, args=(queue,))
    producer_thread.start()
    consumer_thread = Thread(target=consumer, args=(queue,), daemon=True)
    consumer_thread.start()

    producer_thread.join()
    queue.join()


if __name__ == '__main__':
    main()
