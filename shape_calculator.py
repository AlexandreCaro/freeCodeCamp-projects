#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 08:07:10 2022

@author: alexandre
"""

class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height=height

  def get_area(self):
    return self.width*self.height

  def get_perimeter(self):

    return 2*self.width+2*self.height

  def get_diagonal(self):
    return ((self.width**2+self.height**2)**0.5)

  def get_picture(self):

    string = ""

    if self.width>50 or self.height>50:

      return "Too big for picture"

    for i in range(self.height):

      string += f"*"*self.width + "\n"

    return string

  def get_amount_inside(self, objet):

    size_original = self.get_area()

    size_new = objet.get_area()

    fit = size_original//size_new

    return fit

  def __str__(self):
      
      return "Rectangle(width=" +  str(self.width) + ", height=" + str(self.height) + ")"
        

class Square(Rectangle):

  def __init__(self, width):

    self.width=width
    self.height=width

  def set_side(self, side):

    self.width=side
    self.height=side

  def set_width(self, width):

    self.width = width
    self.height= width

  def set_height(self, height):

    self.width=height
    self.height=height
    
  def __str__(self):
      
      return "Square(side=" + str(self.width) + ")"


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
"""
sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
"""