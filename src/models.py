import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Float, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

# instancia de una clase
Base = declarative_base()

# RELATIONSHIP ONE TO ONE
# class Parent(Base):
#     __tablename__ = "parents"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), nullable=False)
    
#     child=relationship("Child", back_populates="parent", uselist=False)

#     def __repr__(self):
#         return f"<Parent {self.id}"



# class Child(Base):
#     __tablename__ = "children"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), nullable=False)

#     parent_id = Column(Integer, ForeignKey("parents.id"))
#     parent = relationship("Parent", back_populates="child")

# ************************************************************************************************************
# RELATIONSHIP ONE TO MANY

# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True)
#     username = Column(String(100), nullable=False, unique=True)
#     email = Column(String(100), nullable=False, unique=True)

#     posts = relationship("Post", back_populates="author")



# class Post(Base):
#     __tablename__ = "posts"
#     id = Column(Integer, primary_key=True)
#     title = Column(String(120), nullable=False)
#     content = Column(String(255), nullable=False)
#     user_id = Column(Integer, ForeignKey("users.id"))

#     author=relationship("User", back_populates="posts")

#******************************************************************************************************************************
#  RELATIONSHIP MANY TO MANY --> VERSION ONE

# class Customer(Base):
#     __tablename__ = "customers"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)

#     asociation = relationship("Asociation", back_populates="customer")

# class Product(Base):
#     __tablename__="products"
#     id = Column(String(100), primary_key=True)
#     name = Column(String(100), nullable=False)
#     price = Column(Float, nullable=False, default=1000)

#     asociation = relationship("Asociation", back_populates="product")


# class Asociation(Base):
#     __tablename__ = "customer_product"
#     id = Column(Integer, primary_key=True)
#     customer_id = Column(Integer, ForeignKey("customers.id"))
#     product_id = Column(Integer, ForeignKey("products.id"))

#     customer = relationship("Customer", back_populates="customers")
#     product = relationship("Product", back_populates="products")



#  RELATIONSHIP MANY TO MANY --> VERSION TWO

association_table=Table(
    "association",
    Base.metadata,
    Column("customer_id", ForeignKey("customers.id")),
    Column("products_id", ForeignKey("products.id"))
)

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    products=relationship("Product", secondary=association_table, back_populates="customers")

class Product(Base):
    __tablename__="products"
    id = Column(String(100), primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False, default=1000)

    customer=relationship("Customer", secondary=association_table, back_populates="products")




## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
