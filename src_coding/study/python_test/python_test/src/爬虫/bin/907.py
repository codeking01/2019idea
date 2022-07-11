# a=0  求奇数
# while a<100 :
#     a+=1
#     if a%2!=0 :
#         print(a)


k=0
a=99
while a <999 :
    a+=1
    unit=a%10 #个位
    decade=a%100//10 #十位
    hundred=a//100 #百位
    if unit**3+decade**3+hundred**3==a :
        k+=1
        print(a)
print(k)
