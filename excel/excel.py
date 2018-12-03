# encoding=utf-8
import xlrd
import os
import xlwt

# 获取通讯录
def getAll():
    data = xlrd.open_workbook('通讯录.xls')
    table = data.sheets()[0]   
    return table 

# 获取值班表
def getOnDuty(all_table,worksheet,title):
    
    data = xlrd.open_workbook('靖边值班表.xls')
    table = data.sheets()[0]   
    nrows = table.nrows 
    all_nrows = all_table.nrows
    name_index = date_index = leader_index = row_index = 0
    for i in range(3):
        row = table.row_values(i)
        if '值班人员' in row:
            name_index = row.index('值班人员')
            row_index = i+1
        if '值班时间' in row:
            date_index = row.index('值班时间')
        if '带班领导干部' in row:
            leader_index = row.index('带班领导干部')
    if name_index>0 and date_index>0 and leader_index>0:
        for i in range(row_index,nrows):
            row = table.row_values(i)
            name = row[name_index]
            date = row[date_index]
            leader = row[leader_index]
            name_contact = leader_contact = ''
            if name and len(name)>1 and len(name)<5 and '审核' not in name:
                flag = l_flag = False
                for j in range(all_nrows):
                    all_row = all_table.row_values(j)
                    if  name in all_row:
                        name_contact =  handle(all_row)
                        flag = True
                    if  leader and leader in all_row:
                        leader_contact =  handle(all_row)
                        l_flag = True
                if not flag:
                    print('未找到 %s的联系方式'%name)
                if leader and not l_flag:
                    print('未找到 %s的联系方式'%leader)

                value = [date,leader,leader_contact,name,name_contact,'','']

    else:
        print('没找到表头信息，请检查excel里值班人员，值班时间，带班领导干部 这3个是否存在')
    

# 处理每行数据
def handle(row):
    new_row = str(row[3]).rstrip('0').rstrip('.')+' '+str(row[4]).rstrip('0').rstrip('.')+' '+str(row[5]).rstrip('0').rstrip('.')
    return new_row

if __name__ == '__main__':
    print('开始值班表处理……')
    rootdir = os.getcwd()
    list = os.listdir(rootdir) 
    for i in range(0,len(list)):
           path = os.path.join(rootdir,list[i])
           if os.path.isfile(path):
                print(path)
    # workbook = xlwt.Workbook(encoding = 'ascii')
    # worksheet = workbook.add_sheet('Sheet1')
    # title = ['日    期','带班领导干部','联系方式','靖边值班人员','联系方式','银川值班人员','联系方式']
    # for i in range(len(title)):
    #     worksheet.write(0, i, label = title[i])
    # table = getAll()
    # result = getOnDuty(table)   
    # for i in range(len(result)):
    #     for j in range(len(result[i])):
    #         worksheet.write(i, j, label = result[i][j])
    # workbook.save('生成汇总表.xls')
    # print('over')