1. linux下如何快速将文件每行倒序输出

   tac命令可以倒着输出文件内容，相对于cat命令

   常见的cat -b 列出行号

2. Linux的分区形式有MBR分区和GPT分区形式

3. 查看内核版本：uname -r   查看

4. 修改启动bash界面：修改/ect/issue文件

5. 文件权限修改：

   - chgrp +组名+文件名   修改文件所在组
   - chown +用户+文件名  修改文件的拥有者
   - chmod +...+文件名   修改文件权限

   目录的rwx分别指的是：是否可以读取目录内容的权限：ls、是否可以移动目录下文件或者修改的权限、是否可以进入目录的权限

6. stty -a可以显示所有按键列表，比如intr=^c表示按下ctrl+c可以终止正在运行的程序。

7. linux默认搭配热键：
   Ctrl + C     终止目前的命令
   Ctrl + D     输入结束 (EOF),例如邮件结束的时候;
   Ctrl + M     就是 Enter 啦!
   Ctrl + S     暂停屏幕的输出
   Ctrl + Q     恢复屏幕的输出Ctrl + U 在提示字符下,将整列命令删除
   Ctrl + Z    『暂停』目前的命令

8. **数据流重导向**

   ```shell
   ll / > ~/info        #表示将ll命令的输出内容输出到info文件，存在则覆盖掉
   find /home -name .bashrc > list_right 2> list_error   #由于find会出现权限问题，所以可以这样将错													   #误信息输出到list_error
   find /home -name .bashrc 2> /dev/null   #这个可以将错误信息吃掉，/dev/null是垃圾桶黑洞装置
   find /home -name .bashrc > list 2> &1   #将错误和正确的信息都写到同一个文件中去
   ```

9. **管线命令**

   ```shell
   ls -al /etc | less  #这样可以将ls输出的再用less命令，避免一下子打印在屏幕上，管道命令必须接受输入，不                     #能是ls、cat这样的
   ```

   **grep**

   ```shell
   grep --color=auto 'MANPATH' /etc/man_db.conf      #输出包含“MANPATH”的所有行
   grep -n 'MANPATH' /etc/man_db.conf      #输出有"MANPATH"的行数
   grep -v    #输出不含指定字符串的行
   ```

   **cut**

   ```shell
   #mason    pts/0        tmux(7377).%1    Wed May 27 16:59   still logged in    last命令
   last | cut -d ' ' -f 1     #这样就能获取到mason
   ```

   cut -f .. -d   ，-f是指定分割符，-d是指定

   **uniq**

   ```shell
   last | cut -d ' ' -f1 | sort | uniq -c      #获取登录用户的次数
   1 
   9 mason
   3 reboot
   1 wtmp
   ```

   uniq相当于group_by。

   **tr**

   ```shell
   选项与参数:
   -d :删除讯息当中的 SET1 这个字符串;
   -s :取代掉重复的字符!
   cat /etc/passwd | tr -d ':'             #tr删除输出中的字符
   ```

   **join**

   ```shell
   选项与参数:
   -t
   :join 默认以空格符分隔数据,并且比对『第一个字段』的数据,
   如果两个文件相同,则将两笔数据联成一行,且第一个字段放在第一个!
   -i :忽略大小写的差异;
   -1 :这个是数字的 1 ,代表『第一个文件要用那个字段来分析』的意思;
   -2 :代表『第二个文件要用那个字段来分析』的意思。
   join -t ':' -1 4 /etc/passwd -2 3 /etc/group | head -n 3  #以':'分割，第一个文件的第四个和第二                                                           #个文件的第三个join
   ```

10. 基础正则

    ```shell
    grep -n 'g*g' regular_express.txt      # *代表可以有任意多个前面的值
    grep -n '[0-9][0-9]*' regular_express.txt    #表示数字序列
    grep -n 'go\{2,5\}g' regular_express.txt     #go后面有2到5个o，需要用/转义括号
    grep -n 'go\{2,\}g' regular_express.txt      #两个以上的o，就不需要限定右边的
    ```

    

11. **排序**

    ```shell
    #whoopsie:x:112:117::/nonexistent:/bin/false  #/etc/passwd  格式
    cat /etc/passwd | sort -t ':' -k 3            #根据‘：’划分，然后根据第三个排序，也就是上面的112
    ```

12. 分区命令

    ```shell
    [dmtsai@study ~]$ split [-bl] file PREFIX
    选项与参数:
    -b :后面可接欲分区成的文件大小,可加单位,例如 b, k, m 等;
    -l :以行数来进行分区。
    PREFIX :代表前导符的意思,可作为分区文件的前导文字。
    
    ```

    

### VIM

1. ctrl+s会锁住整个界面，此时可以ctrl+q退出锁定状态

### 文件系统

https://zhuanlan.zhihu.com/p/105086274

Linux中一切资源都是以文件的形式存在的，包括磁盘、设备、socket等，只要是文件就可以进行读写。进程在操作系统中是一个数据结构

```c
struct task_struct {
    // 进程状态
    long              state;
    // 虚拟内存结构体
    struct mm_struct  *mm;
    // 进程号
    pid_t             pid;
    // 指向父进程的指针
    struct task_struct   *parent;
    // 子进程列表
    struct list_head      children;
    // 存放文件系统信息的指针
    struct fs_struct      *fs;
    // 一个数组，包含该进程打开的文件指针
    struct files_struct   *files;
};
```

我们执行一个程序，也就创建了一个进程，这个程序中我们需要对文件进行一些读写操作，所以进程中会维护文件描述符数组，存放着这个进程打开的所有文件。这个数组初始化有三个，一个是指向输入一个指向输出一个指向错误，这也是为什么吗一个进程创建第一个文件拿到的文件描述符是从3开始。

所以输出重定向和输入重定向就是将files[1]和files[0]指向不同的文件就可以了。

进程间的管道通信也就是将一个进程的输入流和另一文件的输出流执行一个文件进行通信。

**文件描述符**

**文件描述符是指内核储存文件描述符表的索引**。因为进程访问文件是根据文件描述符通过系统调用让内核帮助获取文件到主存，进程没有直接访问文件的权限。

### SHELL

1. 我们执行一个命令，比如ls，系统是通过PATH这个环境变量的内容记录的路径顺序去寻找指令，如果不存在这个指令，就会报错。

2. echo $PATH  用echo查看变量名

3. 将自定义变量设定为环境变量

   使用export命令（P428,10.2）1029914310

   使用unset 命令取消设定的变量

4. 使用 env 命令查看当前shell的环境变量，使用set查看所有变量（不仅是环境变量，也包括自己设定的变量）

5. ？也是一个变量，echo ?可以查看到上一个命令执行的结果，如果是0表示没有错误

6. 使用read+变量名可以实现让用户自定义输入变量名

7. declare进行变量宣告，设置变量的属性（只读、可写）还可以进行运算

   ```sh
   sum=1+2+3
   declare -i sum
   echo $sum  #显示6而不是1+2+3这个字符串
   ```

8. ulimit  限制用户的一些系统资源

9. /etc/profile   这是每个shell登录后都会去读取的文件

10. 用户登录shell后出现bash给用户使用的过程中发生了什么？

    ![](/home/mason/Pictures/2020-05-27/Screenshot from 2020-05-27 16-58-29.png)

    首先系统会去读取/etc/profile文件，这个是每个shell都会读取的，这个文件里面也会调用/etc/profile.d/下的所有.sh文件，然后系统还会去读取~/.bash_profile文件，这是有三个顺序的（~/.bash_profile、~/.bash_login、~/.profile，按照顺序来，一个存在，后面就不会加载了），然后这三个里面一定还会去调用~/.bashrc文件

11. source 命令主要的功能就是可以直接将用户自定义的环境变量加载到当前shell的环境，所以当多个人需要不同配置文件时，可以自定义配置文件然后去source

12. ```sh
    set -u  #如果使用了不存在的变量，就报错，取消则是set +u
    echo $name   #name不存在就会报错
    
    set -x  #执行前会先打印出指令内容
    [dmtsai@study ~]$ echo ${HOME}
    + echo /home/dmtsai
    /home/dmtsai
    ```

### Nginx

