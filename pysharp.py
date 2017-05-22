class for2(object):
    def __init__(self,*args):
        iname = args[0].split('=')[0]
        forlambda = args[1].replace(iname,'x')
        self.iflambd = lambda x: eval(forlambda)
        self.ivalue = int(args[0].split('=')[1])
        forlambda2 = args[2].replace(iname,'x').replace('x=','').replace('=','')
        self.iterlambd =lambda x: eval(forlambda2)
        self.first=True
    def __iter__(self):
        return self
    def __next__(self):
        if(self.first):
            self.first=False
            return self.ivalue
        self.ivalue = self.iterlambd(self.ivalue)
        if(self.iflambd(self.ivalue)):
            return self.ivalue

        else:
            raise StopIteration()

class switch(object):
    def __init__(self, value):
        self.value = value  # значение, которое будем искать
        self.fall = False   # для пустых case блоков

    def __iter__(self):     # для использования в цикле for
        """ Возвращает один раз метод match и завершается """
        yield self.match
        raise StopIteration

    def match(self, *args):
        """ Указывает, нужно ли заходить в тестовый вариант """
        if self.fall or not args:
            # пустой список аргументов означает последний блок case
            # fall означает, что ранее сработало условие и нужно заходить
            #   в каждый case до первого break
            return True
        elif self.value in args:
            self.fall = True
            return True
        return False
class list2(list):
    def first(self):
        return self[0]
    def first_or_default(self,variable,expression,default=0):
        ilambd = lambda x: eval(expression.replace(variable,'x'))
        for a in self:
            if(ilambd(a)):
                return a
        return default
    def append_range(self,_T):
        for element in _T:
            self.append(element)
    def first_index_of(self, _T):
        i=0
        for a in self:
            if(a==_T):
                return i
            i+=1
        return -1
    def remove_range(self, _T):
        for a in _T:
            self.remove(a)
    def reverse(self):
        self = self[::-1]
        return self
    def all_index_of(self,_T):
        all = []
        i=0
        for a in self:
            if a==_T:
                all.append(i)
            i+=1
        return all
    def last_index_of(self,_T):
        i = len(self)-1
        for a in self.reverse():
            if (a == _T):
                return i
            i -= 1
        return -1
    def remove_at(self,index):
        del self[index]

class str2(str):
    def last_index_of(self,_T):
        i = len(self)-1
        for a in self.reverse():
            if (a == _T):
                return i
            i -= 1
        return -1
    def all_index_of(self,_T):
        all = []
        i=0
        for a in self:
            if a==_T:
                all.append(i)
            i+=1
        return all
    def first_index_of(self, _T):
        i=0
        for a in self:
            if(a==_T):
                return i
            i+=1
        return -1
    def to_list(self):
        return list(self)
    def reverse(self):
        self = self[::-1]
        return self
    def set_by_index(self, key, value):
        e = list(self)
        e[key]=value
        return ''.join(e)
    def remove(self,value):
        return self.replace(value,'')
    def remove_at(self,index):
        e = list(self)
        del e[index]
        return ''.join(e)






