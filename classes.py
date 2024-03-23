class person:
     # class attribute
    def __init__ (self,name,age,gender):#constructor
      self. name=name #instance attribute
      self.age=age
      self._gender= gender

    def introduce(self):
       print('My name is',self.name ,'of age',self.age,'and am a',self._gender)

p1=person('Kenn',20,'Male')
p1.introduce()


