from abc import abstractmethod


class band:
    def __init__(self,name,members):
        self.name = name
        self.members = members


class Musician():
    def __init__(self,name):
        self.name = name

class Guitarist(Musician):
    
    def __init__(self,name):
        super().__init__(name)
    

class Bassist(Musician):
    
    def __init__(self,name):
        super().__init__(name)
    

class Drummer(Musician):
    
    def __init__(self,name):
        super().__init__(name)
   