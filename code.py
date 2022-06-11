import csv
with open('SOCR-HeightWeight.csv', newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
from collections import Counter
# data='This is a strin for the code'
# x=Counter(data)
# print(x)
# newList=x.items()
# print(newList)
file_data.pop(0)
newData=[]
for i in range(len(file_data)):
    num=file_data[i][1]
    newData.append(float(num))
n=len(newData)
# mean
total=0
for x in newData:
    total+=x
mean=total/n
print(mean)
# median
newData.sort()
if n%2==0 :
    median_1=float(newData[n//2])
    median_2=float(newData[n//2-1])
    median=(median_1+median_2)/2
else :
    median=newData[n//2]
print(median)
data=Counter(newData)
modeDataForRange={
    '50-60':0,
    '60-70':0,
    '70-80':0
}
for height,occurence in data.items():
    if 50 < height < 60 :
        modeDataForRange['50-60']+=occurence
    elif 60 < height < 70 :
        modeDataForRange['60-70']+=occurence
    elif 70 < height < 80 :
        modeDataForRange['70-80']+=occurence
modeRange, modeOccurence=0, 0
for range, occurence in modeDataForRange.items():
    if occurence > modeOccurence :
        modeRange, modeOccurence=[int(range.split('-')[0]), int(range.split('-')[1])], occurence
        mode=float((modeRange[0]+modeRange[1])/2)
print(mode)