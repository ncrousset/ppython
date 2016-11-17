import time

print('The time is  : ', time.ctime())
later = time.time() + 15
print('15 secs from now : ', time.ctime(later))

# struct_time

print('gmtime: ', time.gmtime())
print('localtime: ', time.localtime())
print('mktime: ', time.mktime(time.localtime()))

t = time.localtime() 
print(t)
print('Day of month:', t.tm_mday)
print('Day of week:', t.tm_wday)
print('Day of year:', t.tm_yday)