from pandas import Series, DataFrame
import pandas as pd
# obj_list=[1,2,3]
# a= pd.Series(obj_list)
# print( a)
asciiSer =Series([97,98,99,100],index=['a','b','c','d'])
# asciiSer =[97,98,99,100]
print(asciiSer)
print("--------")
print('a'in asciiSer)
print("--------")

print(pd.Series(asciiSer))
popDict=Series({'HRB':800,'PK':5100,'SH':6000,'SZ':2200})

print(popDict)

data ={'apple':['color','size','wight'],
       'banana':['long','wangdu','time'],
       'potato':['weight','size','color']}
d = DataFrame(data,index=['one','two','three'])
print(d)
print("----------")
print(d['apple'])
print("----------")
print(d.banana)#这两个是一样的功能
print("----------")

# 获取一横的数据
print(d.ix['two'])

popDict = {'SZ':2200, 'PK':5100, 'SH':6000, 'HRB':800}
allCity = ['SZ', 'GZ', 'PK', 'HK', 'SH', 'HRB']

doc = DataFrame(popDict,index=allCity)
print("=================")
print(doc)
print("=================")
print(doc.SZ)
print("=======________==========")
stuDict = {'grade':[1, 2, 3, 4, 5, 6], 'year':[2010, 2011, 2012, 2013, 2014, 2015],
'teacher':['Lucy', 'Lily', 'Tom', 'Jerry', 'Poly', 'Han']}
p =DataFrame(stuDict)
print(p)
print("=======_____+++___==========")

stuFrame =DataFrame(stuDict,columns={'total','grade','year','teacher'})
print(stuFrame)
val =Series([12,23,24,116])
stuFrame['total']=val
print(stuFrame)
print("dddd")
#这个就是将dataframe转换为series
series = Series(stuFrame.teacher)
print(series)

dist={'decimal':[65,66,67,68,69],
      'Octal':[101,102,103,104,105]}
di = DataFrame(dist,index=['a','b','c','d','e'])
print(di)
print("+++++++++++++")
dict1= {'decimal':{2003:'people',2004:'human',2005:'superman'},
        'service':{'2003':'apple','2004':'bread','2005':'catch'}}
do = DataFrame(dict1,index=[2003,2004,2005])
do.index.name='年份'
do.columns.name='任命'
print(do)