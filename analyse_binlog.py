import linecache
readfile = open('/Users/weixinping/Downloads/find.sql','r')
writefile = open('/Users/weixinping/Downloads/table.sql','w')
start = {}
i = 1
lines = readfile.readlines()
start_index = 0
stop_index = 0
for i in range(0,len(lines)):
    if lines[i].find('#181212')==0 and  lines[i].find('Write_rows') >0 :
        start_index = i
    elif  lines[i].find('# at ') ==0:
        if start_index != 0:
            stop_index = i
            text = ''.join(lines[start_index:stop_index])
            if text.find('t_user_data_supply_status') > 0:
                writefile.write(text)
            start_index = 0
            stop_index = 0
readfile.close()
writefile.close()