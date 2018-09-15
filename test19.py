import sys
print('命令行参数如下:')
for i in sys.argv:
    print(i)
print('\n\nPython 路径为：', sys.path, '\n')
# 1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
# 2、sys.argv 是一个包含命令行参数的列表。
# 3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。

# import support
# support.print_func("world")

# import sys
# print(sys.path)

# import fibo
# fibo.fib(1000)
# print(fibo.fib2(1000))
# print(fibo.__name__)
# # 如果你打算经常使用一个函数，你可以把它赋给一个本地的名称
# fib = fibo.fib
# fib(1000)

# from fibo import fib, fib2
# # from fibo import *
# fib(500)
# print(fib2(500))

# 一个模块被另一个程序第一次引入时，其主程序将运行。
# 如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行
# 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
# if __name__ == '__main__':
#    print('程序自身在运行')
# else:
#    print('我来自另一模块')

# 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
# import fibo,sys
# print(dir(fibo))
# print(dir(sys))

# 如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称:
# a = [1, 2, 3, 4, 5]
# import fibo
# fib = fibo.fib
# print(dir()) # 得到一个当前模块中定义的属性列表
# a = 5 # 建立一个新的变量 'a'
# print(dir())
# del a # 删除变量名a
# print(dir())

# 包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
# 比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。
# 这里给出了一种可能的包结构（在分层的文件系统中）:
# sound/                          顶层包
#       __init__.py               初始化 sound 包
#       formats/                  文件格式转换子包
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  声音效果子包
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  filters 子包
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py
#               ...
# 在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。
# 目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。
# 用户可以每次只导入一个包里面的特定模块，比如:
# import sound.effects.echo
# 这将会导入子模块:sound.effects.echo。 他必须使用全名去访问:
# sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
# 还有一种导入子模块的方法是:
# from sound.effects import echo
# 这同样会导入子模块: echo，并且他不需要那些冗长的前缀，所以他可以这样使用:
# echo.echofilter(input, output, delay=0.7, atten=4)
# 还有一种变化就是直接导入一个函数或者变量:
# from sound.effects.echo import echofilter
# 同样的，这种方法会导入子模块: echo，并且可以直接使用他的 echofilter() 函数:
# echofilter(input, output, delay=0.7, atten=4)

# 注意当使用from package import item这种形式的时候，对应的item既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量。
# import语法会首先把item当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。如果还没找到，恭喜，一个:exc:ImportError 异常被抛出了。
# 反之，如果使用形如import item.subitem.subsubitem这种导入形式，除了最后一项，都必须是包，而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字。

# 这里有一个例子，在:file:sounds/effects/__init__.py中包含如下代码:
# __all__ = ["echo", "surround", "reverse"]
# 这表示当你使用from sound.effects import *这种用法时，你只会导入包里面这三个子模块。

# 如果 __all__ 真的没有定义，那么使用from sound.effects import *这种语法的时候，就不会导入包 sound.effects 里的任何子模块。他只是把包sound.effects和它里面定义的所有内容导入进来（可能运行__init__.py里定义的初始化代码）。
# 这会把 __init__.py 里面定义的所有名字导入进来。并且他不会破坏掉我们在这句话之前导入的所有明确指定的模块。
# 看下这部分代码:
# import sound.effects.echo
# import sound.effects.surround
# from sound.effects import *

# 如果在结构中包是一个子包（比如这个例子中对于包sound来说），而你又想导入兄弟包（同级别的包）你就得使用导入绝对的路径来导入。
# 比如，如果模块sound.filters.vocoder 要使用包sound.effects中的模块echo，你就要写成 from sound.effects import echo。
# from . import echo
# from .. import formats
# from ..filters import equalizer
# 无论是隐式的还是显式的相对导入都是从当前模块开始的。主模块的名字永远是"__main__"，一个Python应用程序的主模块，应当总是使用绝对路径引用。
