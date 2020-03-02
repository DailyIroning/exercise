# for, while
# break, continue 배우기
for i in range(100):
    print(i)
    print("철수")
    print("영희")
    if i > 2:
        break

j = 0
while j < 3:
    print(j)
    print("철후후후후")
    print("영희희희")
    j = j + 1

k = 0
while True:  #무한루프
    print(k)
    print("케케케")
    print("훼훼훼")
    k = k + 1
    if k > 2:
        break

for i in range(3):
    print(i)
    print("철수")
    print("영희")
    if 1 == 1:
        continue

    print("헤헤헤")
