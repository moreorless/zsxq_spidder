import datetime

timeStr = "2019-12-27T18:54:11.011+0800"
t1 = datetime.datetime.strptime(timeStr, "%Y-%m-%dT%H:%M:%S.%f+0800").strftime("%Y-%m-%d %H:%M:%S")
print(t1)

