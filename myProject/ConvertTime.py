import time

now = time.time()
print(now)

min = now // 60
sec = now - min * 60

hour = min // 60
min -= hour*60

day = hour //24
hour -= day*24

print(str(day)+' : '+str(hour)+' : '+str(min)+' : '+str(sec))