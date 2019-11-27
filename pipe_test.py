# -*- encoding: utf-8 -*-
'''
@File    :   pipe_test.py    
@Author :   Chi Zhang
'''

from multiprocessing import Process,Pipe
# 导入进程，管道模块

def f(conn):
    conn.send([1,'test',None])
    conn.send([2,'test',None])
    print(conn.recv())
    conn.close()

if __name__ == "__main__":
    parent_conn,child_conn = Pipe() #产生两个返回对象，一个是管道这一头，一个是另一头
    p = Process(target=f,args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    print(parent_conn.recv())
    parent_conn.send('father test')
    p.join()