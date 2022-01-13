# linked list
# 떨어진 곳에 위치하는 리스트를 화살표로 연결해서 관리하는 데이터 구조
# C언어에서는 주요한 데이터 구조, 파이선은 리스트에서 링크드리스트 기능 지원

# 예
# node

# class Node:
#   def __init__(self, data) :
#       self.data = data
#       self.next = None
# 위의 것을 좀더 객체지향으로!

class Node:
  def __init__(self, data, next=None) :
      self.data = data
      self.next = next

# 노드와 노드 연결
node1 = Node(1)
node2 = Node(2)
node1.next = node2
#node1 의 주소 설정
head = node1

#링크드 리스트로 데이터 추가하기
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(data):
    node = head
    #맨끝의 노드를 찾기!
    while node.next:
        node = node.next
    #현재 none인 노드의 맨끝부분에 노드를 넣어준다
    node.next = Node(data)

node1 = Node(1)
head = node1
for index in range(2, 10):
  add(index)

#링크드 리스트로 데이터 출력
node = head
while node.next:
  print(node.data)
  node = node.next
print(node.data)