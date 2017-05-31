class Event:
    def __init__(self):
        self.subscribed=[]
    def invoke(self,*args,**kwargs):
        for f in self.subscribed:
            f(*args,**kwargs)
    def handler(self,func):
        self.subscribed.append(func)
        def main(*args,**kwargs):
            func(*args,**kwargs)
        return main
    def add_handler(self,func):
        self.subscribed.append(func)
    def remove_handler(self,func):
        self.subscribed.remove(func)
    def remove_all_handlers(self,func):
        self.subscribed=[]
class EventHandler:
    def __init__(self,*events):
        for e in events:
            e.add_handler(self.__invoker)
        self.subscribed=[]
    def __invoker (self,*args,**kwargs):
        for f in self.subscribed:
            f(*args,**kwargs)
    def subscribe_to(self,event):
        event.add_handler(self.__invoker)
    def unsubscribe_from(self,event):
        event.remove_handler(self.__invoker)
    def add_handler(self,func):
        self.subscribed.append(func)
    def remove_handler(self,func):
        self.subscribed.remove(func)
    def remove_all_handlers(self,func):
        self.subscribed=[]
    def handler(self,func):
        self.subscribed.append(func)
        def main(*args,**kwargs):
            func(*args,**kwargs)
        return main


