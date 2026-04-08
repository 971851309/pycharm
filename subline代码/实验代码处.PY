#添加一个size()方法，方便用户查询链表的大小
#改进
#实现一个结构，可以自己查询元素，添加元素，插入元素，删除元素
#定义一个最简单的链表
class IntList(object):
	def __init__(self,f,r):
		self.first = f
		self.rest = r
	


	def size(self):
		if self.rest is None:
			return 1
		else:
			return 1 + self.rest.size()

l = IntList(5,None)
l = IntList(10,l)
l = IntList(15,l)
print(l.rest.rest.first)
print(l.size())
 