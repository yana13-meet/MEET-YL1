class Integer(object):

     def __init__(self, number, positive):
         self.number = number
         self.p = positive
     def display(self):
            print self.p + str(self.number)

class NegativeInteger(Integer):
	


if __name__=="__main__":
      test = Integer(1998, "-")
      test.display()
      

