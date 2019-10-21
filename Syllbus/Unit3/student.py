class Student:
    def __init__(self,sid=0,sname="",smarks=0):
        self.sid = sid
        self.sname = sname
        self.smarks = smarks

    def set_id(self,sid):
        self.sid = sid
    def set_name(self,sname):
        self.sname = sname
    def set_marks(self,smarks):
        self.smarks = smarks

    def get_id(self):
        return self.sid
    def get_name(self):
        return self.sname
    def get_marks(self):
        return self.smarks
    
