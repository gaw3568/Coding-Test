money, life = map(int, input().split())

per_money = money // life
left_money = money % life
print(per_money)
print(left_money)