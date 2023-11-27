str_var="cat"
nm=""
cnt=len(str_var)-1
print(cnt)
while cnt>=0:
    nm = nm+str_var[cnt]
    cnt -=1

print(str(nm))




ip_add = "2.2.2.2"

print(ip_add.replace('.',"[.]"))
