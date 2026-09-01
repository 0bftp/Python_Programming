# 반복문 : while문, for문


# while문
# 1~10까지 반복 출력
i = 1
while i<=10:
    print(i)
    i+=1
else:
    print("End")
    
nums = [1,3,5,7,9]
target = 2
a=0
while a<5:
    print("found" if target in nums else "not found")
    a+=1