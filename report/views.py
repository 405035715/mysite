from django.shortcuts import render, get_object_or_404
from django.template.context_processors import request
import pyodbc

#查询数据库
def selSql(selStr):
    sqlresult =[]
    connectStr = 'DRIVER={SQL Server};SERVER=192.168.1.4;PORT=1433;DATABASE=videocapture;UID=sa;PWD=easy'
    cnxn = pyodbc.connect(connectStr)
    cursor = cnxn.cursor()
    try:
        cursor.execute(selStr)
    except Exception as e:
        print(e)
    sum = 0
    while 1:
        row = cursor.fetchone()
        #sum = sum + 1
        if not row:
            break
        sqlresult.append(list(row))
        #print(row)
    #print(sum)
    cnxn.close
    return sqlresult

def index(request):
    # 查询报告
    # 查询条件
    name = "陈丽珍"
    swhere = 'and name = \'\'\'\'%s\'\'\'\''%name
    reportsql = 'SET NOCOUNT ON; EXEC  tj_P_RUN_PROCDURE_WITH_SELECTRETURN  \'sp_sel_PatientCheckin\' ,\'@sWhere_=\'\' %s \'\' \' '%swhere
    report= selSql(reportsql)
    # print(len(report))
    for a in report:
        print(a[8])
        print(a[9])
        print(a[10])
        print('\n')
        print(a[30])  # diagfind 所见
        print(a[32]) #conclusion 印象
        print(a[41]) #patientid




    if request.method == 'GET':
        print(request.GET.get('patientid'))
    print(report)
    context = {
        # 'latest_question_list': latest_question_list,
    }
    return render(request, 'report/reportlist.html', context)
