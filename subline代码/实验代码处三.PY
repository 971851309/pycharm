#作业pandas
#第一步，找出最热门的五十本书
import pandas as pd
file = pd.ExcelFile('to_read.csv')

to_read = pd.read_csv('to_read.csv')#读取csv文件
to_read_counts = to_read['book_id'].value_counts().sort_values(ascending=False)#找到book_id列进行value_counts（数值收集）
hottest_50_books_id= to_read_counts[:50].index#对数值进行排序
hottest_50_books_counts= to_read_counts[:50].values#记录数值重复出现的次数
hottest_50_books = pd.DataFrame({
	'book_id':hottest_50_books_id,'to_read_counts':hottest_50_books_counts})#做了两列dataframe一列为book_id，一列为to_read_counts
print(hottest_50_books)

books = pd.read_csv('books.csv')#第二步找到最热的50本书
book_id_and_title = books[['book_id','goodreads_book_id','title']]#选取需要的几列数据
hottest_50_books_with_title = pd.merge(hottest_50_books,book_id_and_title,on='book_id',how='left')#用merge合并，整合book_id合并在left（左边）
print(hottest_50_books_with_title)
hottest_50_books_with_title.to_csv('hottest_50_books_with_title.to_csv')

#第三步，找到5这50本书对应最热的10个标签
book_tags = pd.read_csv('book_tags.csv')
book_tags = book_tags[book_tags['_goodreads_book_id_'].isin(hottest_50_books_with_title['goodreads_book_id'])]
del book_tags['_goodreads_book_id_']
hottest_10_tags = book_tags.groupby('tag_id').sum()#用sum求和
hottest_10_tags = hottest_10_tags.sort_values(by='count',ascending=False)[:10]#倒序排列取前十个
print(hottest_10_tags)



