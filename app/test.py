import asyncio
import time
from typing import NamedTuple
import flask

# async def asynchronous_task():
#     await asyncio.sleep(1)
#     print('async slept 1 sec')

# def sync_task():
#     time.sleep(1)
#     print('sync slept 1 sec')

# async def slow():
#     start = time.time()
#     sync_task()
#     task0 = asyncio.get_running_loop().run_in_executor(None, sync_task)
#     task = asyncio.create_task(asynchronous_task())
#     task1 = asyncio.create_task(asynchronous_task())
#     await task, task1

#     print(time.time() - start)
#     print('ended')

# # asyncio.run(slow())

# # x = 'sema'
# y = {
#     'name': (x := 'sema')
# }

# print(y)
# print(x)
# x = 'nastya'
# print(y)
# print(x)

class Meta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        print(mcs, f"METACLASS __new__ called {kwargs}")
        return super().__new__(mcs, name, bases, namespace)

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print(mcs, f"METACLASS __prepare__ called {kwargs}")
        return super().__prepare__(name, bases, **kwargs)

    def __init__(cls, name, bases, namespace, **kwargs):
        print(cls, f" METACLASS __init__ called {kwargs}")
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        print(cls, f" METACLASS __call__ called {args}")
        return super().__call__(*args, **kwargs)


class Concrete(metaclass=Meta, hui='hui'):
    def __init__(self, name) -> None:
        self.name = name

class Teb(metaclass=Meta, hui='hui'):
    pass

Concrete('sema')
Teb()