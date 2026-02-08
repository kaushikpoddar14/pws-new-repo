from app.cal.py import add,substract

'''
from app--> folder
calculator --> filename
import --> add,substract(functions)
'''

def test_add():
  assert add(2,3) == 5

def test_sub():
  assert sub(5,3) == 2
