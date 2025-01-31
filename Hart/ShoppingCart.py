class Product:
  """
  Shopping Cart Hacker Rank Solution

  Represent Product

  >>> laptop = Product("Laptop", 1200)
  >>> laptop.price
  1200
  """
  def __init__(self, name, price):
    self.name = name
    self.price = price

class YellowCart:
  """
  Yellow Cart Shopping

  >>> cart = YellowCart()
  >>> cart.Total()
  0
  >>> laptop = Product("Laptop", 1200)
  >>> cart.Append(laptop)
  >>> len(cart)
  1
  >>> cart.Total()
  1200
  """
  def __init__(self):
    self.items = []

  def Total(self):
    result = sum(item.price for item in self.items)
    return result

  def Append(self, product : Product):
    self.items.append(product)

  def __len__(self):
    return len(self.items)

if __name__ == "__main__":
  import doctest
  doctest.testmod()