# STACK
# LIFO(Last In, Fisrt Out) 또는 FILO(First In, Last Out) 데이터 관리 방식을 따름
# 후입선출
# 컴퓨터 내부의 프로세스 구조의 함수 동작 방식
# push(): 데이터를 스택에 넣기
# pop(): 데이터를 꺼내기

#재귀 함수
def recursive(data):
  if data < 0:
    print("ended")
  else:
    print(data)
    recursive(data - 1)
    print("returned", data)


# 파이선 리스트 기능에서 제공하는 메서드로 스택 사용해보기
data_stack = list()
data_stack.append(1)
data_stack.append(2)

print(data_stack)
print(data_stack.pop())

# 연습문제
# push와 pop를 쓰지 않고 기능 구현하기

stack_list = list()

def stackPush(data) :
  stack_list.append(data)

def stackPop():
  targetData = stack_list[-1]
  print(targetData)
  del stack_list[-1]
  return targetData

for index in range(10):
  stackPush(index)

print(stack_list)

stackPop()

# 스택의 장단점
# 장점
#   구조가 단순 >> 구현이 쉽다
#   데이터 저장/읽기 속도가 빠름
# 단점
#   데이터 최대 갯수를 미리 정해야 한다.
#   저장 공간의 낭비가 발생할 수 있음