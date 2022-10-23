import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'

    publisher_id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(100), nullable=False)

    def __str__(self):
        return f'Publisher "{self.name}" with ID {self.publisher_id}.'


class Book(Base):
    __tablename__ = 'book'

    book_id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(100), nullable=False)
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey('publisher.publisher_id'), nullable=False)

    publisher = relationship(Publisher, backref='book')

    def __str__(self):
        return f'Book "{self.title}", publisher ID {self.publisher_id}.'


class Shop(Base):
    __tablename__ = 'shop'

    shop_id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(100), nullable=False)

    def __str__(self):
        return f'Shop "{self.name}" with ID {self.shop_id}.'


class Stock(Base):
    __tablename__ = 'stock'

    stock_id = sq.Column(sq.Integer, primary_key=True)
    book_id = sq.Column(sq.Integer, sq.ForeignKey('book.book_id'), nullable=False)
    shop_id = sq.Column(sq.Integer, sq.ForeignKey('shop.shop_id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    shop = relationship(Shop, backref='stock')
    book = relationship(Book, backref='stock')

    def __str__(self):
        return f'Stock with ID {self.stock_id} count = {self.count}.'


class Sale(Base):
    __tablename__ = 'sale'

    sale_id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.DECIMAL, nullable=False)
    data_sale = sq.Column(sq.String(50), nullable=False)
    stock_id = sq.Column(sq.Integer, sq.ForeignKey('stock.stock_id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship(Stock, backref='sale')

    def __str__(self):
        return f'Sale price is {self.price}, stock ID {self.stock_id}.'


def create_tables(engine):
    Base.metadata.create_all(engine)


def drop_tables(engine):
    Base.metadata.drop_all(engine)


def get_publisher(some_session):
    """You can find a Publisher by ID or by its name"""
    var = input(f'Пожалуйста выберите, как будем искать издателя: 1 - по ID, 2 - по названию.\n')
    if var == '1':
        id_ = input('Введите id Издателя: ')
        for record in some_session.query(Publisher).filter(Publisher.publisher_id == id_).all():
            return record
    elif var == '2':
        name = input('Введите название Издателя: ')
        for record in some_session.query(Publisher).filter(Publisher.name == name).all():
            return record


def get_shops(some_session, some_publisher_name):
    """You can find shops, where you can buy a book by certain Publisher. Return a listFinal"""
    q = some_session.query(Shop).join(Stock.shop).join(Stock.book).\
        join(Book.publisher).filter(Publisher.name == some_publisher_name)
    return q
