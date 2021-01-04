import datetime
from datetime import datetime as dt

# tstr = '2012-12-29'
# tstr2 = '13:49'
# adatetime = dt.strptime(tstr, '%Y-%m-%d')
# bdatetime = dt.strptime(tstr2, '%H:%M')

# print(tstr)
# print(adatetime)
# print(bdatetime)


date = '2017/10/19 10:54:29'
new_date = datetime.datetime.strptime(
    date, '%Y/%m/%d %H:%M:%S').strftime('%Y/%m/%d')
print(new_date)
new_time = datetime.datetime.strptime(
    date, '%Y/%m/%d %H:%M:%S').strftime('%H:%M')
print(new_time)

# date = '2017/10/19 10:54:29'
# new_date, new_time = date.split()
# new_date  # => '2017/10/19'
# print(new_date)
# print(new_time.strftime)
