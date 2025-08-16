'''
@Author : Hemant Kshirsagar
@goal : To implement a basic version of class Book
'''

class Book :
    def __init__(self, title : str, author_list : list[str], edition : int, no_pages : int, price : float) :
        self.bk_title = title
        self.bk_authors = author_list
        self.bk_edition = edition
        self.bk_no_pages = no_pages
        self.bk_price = price

    def __str__(self) :
        return f'{self.__dict__}'
    
b = Book("Python Programming", ["Writer"], 1, 1500, 3500)
print(b)
