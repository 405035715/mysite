import datetime
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

def report(request):
    patientid   = request.GET.get('patientid')
    examinedate = request.GET.get('time')
    swhere      = 'and patientid = \'\'\'\'%s\'\'\'\'  and examinedate =  \'\'\'\'%s\'\'\'\' ' % (patientid,examinedate)
    patientsql  = 'SET NOCOUNT ON; EXEC  tj_P_RUN_PROCDURE_WITH_SELECTRETURN  \'sp_sel_PatientCheckin\' ,\'@sWhere_=\'\' %s \'\' \' ' % swhere
    patientlist = selSql(patientsql)

    if 1 == len(patientlist):
        patient   = patientlist[0]
        print(patient)
        reportDic = {}
        reportDic['patientid']   = patient[41]       # patientid
        reportDic['name']        = patient[8]
        reportDic['sex']         = patient[9]
        reportDic['age']         = patient[10]
        reportDic['bodypart']    = patient[27]
        reportDic['time']        = datetime.datetime.strftime(patient[25],"%Y-%m-%d %H:%M:%S")
        reportDic['diagfind']    = patient[30]     # diagfind 所见
        reportDic['conclusion']  = patient[32]     #conclusion 印象
        reportDic['doctor']      = patient[19]     #检查医生
        #print(reportlist)
        context = {
            'reportDic': reportDic,
        }
        return render(request, 'report/report.html', context)

def patientlist(request):
    # 查询病人
    # 查询条件
    name = '陈丽珍'
    if 'GET' == request.method:
        if request.GET.get('name'):
            name = request.GET.get('name')
    swhere = 'and name = \'\'\'\'%s\'\'\'\''%name
    reportsql = 'SET NOCOUNT ON; EXEC  tj_P_RUN_PROCDURE_WITH_SELECTRETURN  \'sp_sel_PatientCheckin\' ,\'@sWhere_=\'\' %s \'\' \' '%swhere
    reportlist = selSql(reportsql)
    # print(len(report))
    patintlist = []
    for a in reportlist:
        reportDic = {}
        reportDic['patientid'] = a[41]  # patientid
        reportDic['name']      = a[8]
        reportDic['sex']       = a[9]
        reportDic['age']       = a[10]
        reportDic['bodypart']  = a[27]
        reportDic['time']      = datetime.datetime.strftime(a[25],"%Y-%m-%d %H:%M:%S")
        patintlist.append(reportDic)
    print(reportlist)
    context = {
         'patintlist': patintlist,
         'name'      : name
    }
    return render(request, 'report/patiantlist.html', context)