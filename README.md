# pysharp - v1.1
C# functions and classes in python.

To install donwload folder




Using:
---------------------------------
----------------------------------
            
            FOR2
for2 - c# for analog

example:
```python
for e in for2('x=7','x**2<=10','x+=2'):
  print(e)
```
--------------------------------
            
            SWITCH
switch - c# analog

example:
```python
for case in switch(var):
  if case(3):
    pass
  if case(4):
    print('four')
    break
  if case(5):
    print('five')
    break
  else:
    print('Unknown')
 ```
 -----------------
        
        STR2
str2 - standart python str class with new methods:
```python 
mstr2 = str2('Hello World')
```
|Name     |Description|Usage|
--------------|:----------:|--------------|
|last_index_of(char)|returns index of last entry|``` mstr2.last_index_of('h')```|
|all_index_of_char(char)|returns list of index entries|``` mstr2.all_index_of('h')```|
|first_index_of_char(char)|returns index of first entry|``` mstr2.first_index_of('h')```|
|reverse()|returns new reversed string|``` mstr2.reverse()```|
|to_list()|returns list of chars|``` mstr2.to_list()```|
|set_by_index(index,char)|returns new string with replaced char|``` mstr2.set_by_index(2,'h')```|
|remove(char)|returns new string with removed all equals chars|``` mstr2.remove('h')```|
|remove_at(index)|returns new string with removed chars|``` mstr2.remove_at(2)```|
------------------------------------

       LIST2
list2 - standart python list2 class with new methods:
```python 
mlist2 = list2([4,6,4,7,8])
```
|Name   |Description|Usage|
|---------|:--------:|------|
|last_index_of(char)|returns index of last entry|``` mlist2.last_index_of('h')```|
|all_index_of_char(char)|returns list of index entries|``` mlist2.all_index_of('h')```|
|first_index_of_char(char)|returns index of first entry|``` mlist2.first_index_of('h')```|
|reverse()|returns new reversed array|``` mlist2.reverse()```|
|append_range(list)|append every element in list to self|``` mlist2.append_range([2,3,4])```|
|first_or_default(variable,expression,default=0)|returns first element that matches the condition|```mlist2.first_or_default('z','z+3>4',default=0)```|
|remove_range(list)|remove every element in list from self|```mlist2.remove_range([4,7,4])```|
|remove_at(index)|remove element by index from self|```mlist2.remove_at(2)```|
|first()|returns first element|```mlist2.first()```|
------------------------------------

        EVENT and EVENTHANDLER
Event - class that implements support for events and handlers

```python 
mEvent = Event()
```

|Name     |Description|Usage|
--------------|:----------:|--------------|
|invoke(args,kwargs)|Invoke all subscribed handlers|``` mEvent.invoke('Hello World')```|
|add_handler(func)|Subscribed new handler|``` mEvent.add_handler(mDef)```|
|remove_handler(func)|Unsubscribed handler|``` mEvent.remove_handler(mDef)```|
|remove_all_handlers()|Unsubscribed all handlers|``` mEvent.remove_all_handlers```|
|handler              |decorator for easy subscribe|```mDef = mEvent.handler(mDef)```|

Example:

```python
mEvent = Event()
@mEvent.handler
def HW(name):
   print(name)
mEvent.invoke('John')
```

EventHandler - class implents handler container. Support subscribe to many events

```python
mEventHandler = EventHandler(mEvent,mEvent2...)
```

|Name     |Description|Usage|
--------------|:----------:|--------------|
|add_handler(func)|Subscribed new handler|``` mEventHandler.add_handler(mDef)```|
|remove_handler(func)|Unsubscribed handler|``` mEventHandler.remove_handler(mDef)```|
|remove_all_handlers()|Unsubscribed all handlers|``` mEventHandler.remove_all_handlers```|
|unsubscribe_from(event)|Unsubscribe handler_container from event|```mEventHandler.unsubscribe_from(mEvent3)```|
|subscribe_to(event)|Subscribe handler_container to event|```mEventHandler.subscribe_to(mEvent3)```|
|handler              |decorator for easy subscribe|```mDef = mEventHandler.handler(mDef)```|

Example:

```python
mEventHandler = EventHandler(mEvent,mEvent2)
@mEventHandler.handler
def HW(name):
   print(name)
mEvent.invoke('John')
mEvent2.invoke('Smit')
```
