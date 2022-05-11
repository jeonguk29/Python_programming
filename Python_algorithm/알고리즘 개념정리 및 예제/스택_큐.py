# 스택 구현시 그냥 리스트 사용하면 됨
from collections import deque
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()       # append, pop 함수는 시간복잡도 상수시간이라 o(1) 스택 자료구조로 활용하기 적합함

print(stack)  # 최하단 원소부터 출력
print(stack[::-1])  # 최상단 원소부터 출력


# 큐(Queue) 구현을 위해 deque 라이브러리 사용  from collections import deque   관행임
queue = deque()  # 리스트로도 가능하지만 시간 복잡도가 더 높아서 비효율 적이라 deque 라이브 러리 씀

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)   # 리스트 append 함수와 동일함 상수시간
queue.append(7)
queue.popleft()  # 가장 왼쪽에 있는수 빼는거임 상수시간 소요
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)  # 먼저 들어온 순서대로 출력
queue.reverse()  # 다음 출력을 위해 역순으로 바꾸기
print(queue)  # 나중에 들어온 원소부터 출력
