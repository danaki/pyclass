import mymodule1
from mymodule2 import fun2
import mymodule3 as m3
from mymodule4 import *
from dirmodule import initfun1, subfun2
from dirmodule.submodule1 import subfun1

if __name__ == "__main__":
    mymodule1.fun1()
    fun2()
    m3.fun3()
    fun4_1()
    fun4_2()

    initfun1()
    subfun1()
    subfun2()