import collections as col

dias_semana = col.deque(["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"])
print(dias_semana)

dias_semana.popleft()
print(dias_semana)

dias_semana.appendleft("Dom")
print(dias_semana)

dias_semana.pop()
print(dias_semana)