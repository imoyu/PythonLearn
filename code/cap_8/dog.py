# 1. 引入整个模块
import animal
# 2. 引入模块的某个函数
from animal import eat
# 3. 重命名模块
import animal as a
# 4. 重命名函数
from animal import eat as e
# 5. 引入所有的方法
from animal import *

if __name__ == '__main__':
    # 引入自己写的 animal 模块
    # 方式1引入，模块名.方法名调用
    animal.say()
    # 方式2引入，直接调用
    eat()
    # 重命名调用
    a.say()
    e()
