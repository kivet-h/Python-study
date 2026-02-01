"""
    13.3 操作文件和目录
"""
# 如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。

# 如果要在Python程序中执行这些目录和文件的操作怎么办？
# 其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。
# Python 控制台中执行，或者终端中执行：python 13.2\ 操作文件和目录.py
# import os
# print(os.name)
# # ==>
# # nt

# 如果是posix，说明系统是Linux、Unix或macOS，
# 如果是nt，就是Windows系统。

# 要获取详细的系统信息，可以调用uname()函数：
# >>> os.uname()
# posix.uname_result(sysname='Darwin', nodename='MichaelMacPro.local', release='14.3.0', version='Darwin Kernel Version 14.3.0: Mon Mar 23 11:59:05 PDT 2015; root:xnu-2782.20.48~5/RELEASE_X86_64', machine='x86_64')

# 注意uname()函数在Windows上不提供，执行时会报错。也就是说，os模块的某些函数是跟操作系统相关的。















# ================================================== 环境变量 ==================================================
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
# Python 控制台中执行，或者终端中执行：python 13.2\ 操作文件和目录.py
# import os
# print(os.environ)
# ==>
# environ({'ACSETUPSVCPORT': '23210', 'ACSVCPORT': '17532', 'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\kivet\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'KIVET', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'COMMONPROGRAMFILES(X86)': 'C:\\Prog
# ram Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'EXEPATH': 'C:\\Program Files\\Git\\bin', 'ENABLELOG': 'INFO', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Defau
# lt', 'HDC_SERVER_PORT': '65037', 'HOME': 'C:\\Users\\kivet', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\kivet', 'LOCALAPPDATA': 'C:\\Users\\kivet\\AppData\\Local', 'LOGONSERVER': '\\\\KIVET', 'MSYSTEM': 'MINGW64', 'NUMBER_OF_PROCESSORS': '16', 'NVM_HOME': 'D:\\Software\\Install\\NVM\\nvm', 'NVM_SYMLINK': 'D:\
# \Software\\Install\\nodejs', 'OLLAMA_MODELS': 'D:\\Ollama\\Models', 'OS': 'Windows_NT', 'ONEDRIVE': 'C:\\Users\\kivet\\OneDrive', 'PATH': 'C:\\Program Files\\Git\\mingw64\\bin;C:\\Program Files\\Git\\usr\\bin;C:\\Users\\kivet\\bin;C:\\Program Files\\Common Files\\Oracle\\Java\\javapath;C:\\Program Files (x8
# 6)\\Common Files\\Oracle\\Java\\javapath;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files\\Git\\cmd;D:\\Software\\Install\\NVM\\nvm;D:\\Software\\Install\\nodejs;C:\\Program Files\\dotnet\\;C:\\P
# rogram Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Users\\kivet\\AppData\\Local\\pnpm\\global\\5;D:\\Software\\Install\\WechatDevtools\\微信web开发者工具\\dll;C:\\Program Files\\NVIDIA Corporation\\NVIDIA App\\NvDLISR;D:\\Software\\Install\\anaconda3;D:\\Software\\Install\\anaconda3\\Scripts;D:\\Soft
# ware\\Install\\Python\\Scripts\\;D:\\Software\\Install\\Python\\;C:\\Users\\kivet\\AppData\\Local\\pnpm;C:\\Users\\kivet\\AppData\\Local\\Microsoft\\WindowsApps;D:\\Software\\Install\\NVM\\nvm;D:\\Software\\Install\\nodejs;D:\\Software\\Install\\VSCode\\Microsoft VS Code\\bin;D:\\Ollama;D:\\Software\\Instal
# l\\Cursor\\cursor\\resources\\app\\bin', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PLINK_PROTOCOL': 'ssh', 'PNPM_HOME': 'C:\\Users\\kivet\\AppData\\Local\\pnpm', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 151 Stepping 2, GenuineIntel', 'PROC
# ESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '9702', 'PROGRAMFILES': 'C:\\Program Files', 'PS1': '\\[\\033]0;$TITLEPREFIX:$PWD\\007\\]\\n\\[\\033[32m\\]\\u@\\h \\[\\033[35m\\]$MSYSTEM \\[\\033[33m\\]\\w\\[\\033[36m\\]`__git_ps1`\\[\\033[0m\\]\\n$ ', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules
# ;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PWD': 'D:/web/python-study-ljf/13.IO编程', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'RLSSVCPORT': '22112', 'SESSIONNAME': 'Console', 'SHLVL
# ': '1', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\kivet\\AppData\\Local\\Temp', 'TERM': 'xterm-256color', 'TERMINAL_EMULATOR': 'JetBrains-JediTerm', 'TERM_SESSION_ID': '719d8e06-1e0a-49c2-9131-c49abdd1407f', 'TMP': 'C:\\Users\\kivet\\AppData\\Local\\Temp', 'USERDOMAIN': 'KIVET', 'USERDOMAIN_ROAMINGPROFILE': 'KIVET', 'USERNAME': 'kivet', 'USERPROFILE': 'C:\\Users\\kivet', 'WINDIR': 'C:\\Windows', 'ZES_ENABLE_SYSMAN': '1', '_': 'D:/Software/Install/anaconda3/python'})


# 要获取某个环境变量的值，可以调用os.environ.get('key')：
# Python 控制台中执行，或者终端中执行：python 13.2\ 操作文件和目录.py
# import os
# print(os.environ.get('PATH'))
# ==>
# C:\Program Files\Git\mingw64\bin;C:\Program Files\Git\usr\bin;C:\Users\kivet\bin;C:\Program Files\Common Files\Oracle\Java\javapath;C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32
# \OpenSSH\;C:\Program Files\Git\cmd;D:\Software\Install\NVM\nvm;D:\Software\Install\nodejs;C:\Program Files\dotnet\;C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;C:\Users\kivet\AppData\Local\pnpm\global\5;D:\Software\Install\WechatDevtools\微信web开发者工具\dll;C:\Program Files\NVIDIA Corporation\NV
# IDIA App\NvDLISR;D:\Software\Install\anaconda3;D:\Software\Install\anaconda3\Scripts;D:\Software\Install\Python\Scripts\;D:\Software\Install\Python\;C:\Users\kivet\AppData\Local\pnpm;C:\Users\kivet\AppData\Local\Microsoft\WindowsApps;D:\Software\Install\NVM\nvm;D:\Software\Install\nodejs;D:\Software\Install\VSCode\Microsoft VS Code\bin;D:\Ollama;D:\Software\Install\Cursor\cursor\resources\app\bin













# ================================================== 操作文件和目录 ==================================================
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。

# 查看、创建和删除目录可以这么调用：
# import os

# 查看当前目录的绝对路径:
# print(os.path.abspath('.'))
# ==> D:\web\python-study-ljf\13.IO编程


# # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# os.path.join('D:/web/python-study-ljf/13.IO编程', 'testdir')
# # 然后创建一个目录:
# os.mkdir('D:/web/python-study-ljf/13.IO编程/testdir')
# Python 控制台中执行，或者终端中执行：python 13.2\ 操作文件和目录.py
# ==> 能看到，在D:/web/python-study-ljf/13.IO编程目录下多出了一个testdir目录

# 再次在Python 控制台中执行，或者终端中执行：python 13.2\ 操作文件和目录.py，会报错：
# Traceback (most recent call last):
#   File "D:\web\python-study-ljf\13.IO编程\13.3 操作文件和目录.py", line 90, in <module>
#     os.mkdir('D:/web/python-study-ljf/13.IO编程/testdir')
# FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: 'D:/web/python-study-ljf/13.IO编程/testdir'



# 删掉一个目录:
# os.rmdir('D:/web/python-study-ljf/13.IO编程/testdir')
# ==> D:/web/python-study-ljf/13.IO编程目录下的testdir目录被删除








# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
# 在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
# part-1/part-2

# 而Windows下会返回这样的字符串：
# part-1\part-2




# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
# import os
# print(os.path.split('D:/web/python-study-ljf/13.IO编程/13.3 操作文件和目录.py'))
# ==> ('D:/web/python-study-ljf/13.IO编程', '13.3 操作文件和目录.py')


# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
# import os
# print(os.path.splitext('D:/web/python-study-ljf/13.IO编程/13.3 操作文件和目录.py'))
# ==> ('D:/web/python-study-ljf/13.IO编程/13.3 操作文件和目录', '.py')

# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。



# 文件操作使用下面的函数。假定当前目录下有一个test.txt文件：
# # 对文件重命名:
# >>> os.rename('test.txt', 'test.py')
# # 删掉文件:
# >>> os.remove('test.py')



# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。

# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。








# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
# import os
# fs = [x for x in os.listdir('.') if os.path.isdir(x)]
# print(fs)
# ==> 打印出当前目录下所有的目录名称，类似[dir1, dor2, ...]，如果当前目录下没有目录，则打印出[]


# 要列出所有的.py文件，也只需一行代码：
# import os
# print(os.listdir('.'))
# 打印出当前目录下所有.py的文件，类似于：['13.0 IO编程.py', '13.1 文件读写.py', '13.1 测试图片.png', '13.2 StringIO和BytesIO.py', '13.3 操作文件和目录.py', 'test.txt']

# fs = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
# print(fs)
# 打印出当前目录下所有.py的文件，类似于：['13.0 IO编程.py', '13.1 文件读写.py', '13.2 StringIO和BytesIO.py', '13.3 操作文件和目录.py']