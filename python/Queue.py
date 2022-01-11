# Queue에 대하여,
# Queue는 선입선출을 기본으로 하는 자료 구조
# 부가적인 데이터 정책으로
# FIFO(First-In, First-Out) 또는 LILO(Last-In, Last-Out) 방식이 있다
# Enqueue: 큐에 데이터를 넣는 기능
# Dequeue: 큐에서 데이터를 빼는 기능

# 파이선 자체적으로 큐 임포트를 제공하고 있음
import queue

# 기본적인 큐 클래스를 만든다
testQueue = queue.Queue()

# 큐에 데이터를 넣는 메소드 : put(인자)
testQueue.put('test')
testQueue.put(1)

# 큐의 사이즈를 재는 메소드 : qsize
print(testQueue.qsize())

# 큐의 데이터를 빼는 메소 드 : get()
# (데이터를 특정하여 뺄 수 없고 정책에 따라서 빼야한다)
print(testQueue.get())


# LifoQueue만들기
test2Queue = queue.LifoQueue()

test2Queue.put('test')
test2Queue.put(1)
print(test2Queue.qsize())

# 이 때, LifoQueue이기 때문에 1이 먼저 출력된다.
print(test2Queue.get())


# priorityQueue
# 우선순위를 설정하여 데이터를 넣는다
test3Queue = queue.PriorityQueue()

test3Queue.put((1, 12))
test3Queue.put((11, 'test'))
test3Queue.put((7, 'seven'))

print(test3Queue.qsize())

print('priority') 
print(test3Queue.get())
print(test3Queue.get())
