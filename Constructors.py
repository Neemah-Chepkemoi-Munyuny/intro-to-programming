# Description: This file contains the code for constructors in python   

class Parent: 
 #This is an attribute of the parent class
 parentAttr = 100

 #This inbuilt method is called when an object is created and is invoked by Parent()
def __init__(self):
 print ("Calling parent constructor")

 #We define our own method to be called whenever we want to in the program
def parentMethod(self):
 print ('Calling parent method')

#
def setAttr(self, attr):
 Parent.parentAttr = attr
def getAttr(self):
 print ("Parent attribute :"), Parent.parentAttr

class Child(Parent): # define child class
 def __init__(self):
  print ("Calling child constructor")
def childMethod(self):
 print ('Calling child method')
        

