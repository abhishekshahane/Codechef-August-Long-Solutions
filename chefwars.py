# cook your dish here
for i in range(int(input())):
   darth_health,attack = map(int, input().split())
   darth_health= darth_health - attack
   while (attack > 0):
       attack/=2
       darth_health-=attack
   if (attack <= 0 and darth_health > 0):
       print(0)
   else:
       print(1)
