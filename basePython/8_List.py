list=[1,2,3,4,5]
print(list)
list1=['hello']*3
print(list1)
print(len(list1))
print(list[3])
print(list[-1])

#生成式#
data =[1,2,3,4,5]
new_data=[num*3 for num in data if num<4]
print(new_data)

#队列转字符串
chars=['a','b','c']
str=''.join(chars)
print(str)

#普通迭代
data=[1,2,3,4,5]
for index in range(len(data)):
    print(index,'  ',data[index])

# for循环迭代
for item in data:
    print(item)

#使用enumerate进行迭代
data=[1,2,3,4,5]
for index,num in enumerate(data):
    print(index,'  ',num)

#list添加、删除元素
list=[1,2,3,4,5]
list.append(6)
list.insert(1,'wawa')
list1=[100,200]
list+=list1
if 3 in list:
    list.remove(3)  #删除元素3
list.pop(0)
list.pop(3)    #删除第三个元素
list.clear()

#和string一样，list也可以切片操作
list=[1,3,4,5,5]
list[1:3]

#list排序
list=[1,2,3,4,5,6,345,7]
list1=sorted(list)

#堆排序
import heapq
list=[1,7,4,5,6]
print(heapq.nlargest(2,list))
print(heapq.nsmallest(3,list))






