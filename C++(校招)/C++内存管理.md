## Beam

Beam是一款静态分析工具，由于

## valgrind

http://senlinzhan.github.io/2017/12/31/valgrind/

Valgrind工具包包含多个工具，如Memcheck,Cachegrind,Helgrind, Callgrind，Massif。

**Memcheck**

最常用的工具，用来检测程序中出现的内存问题，所有对内存的读写都会被检测到，一切对malloc()/free()/new/delete的调用都会被捕获。所以，Memcheck 工具主要检查下面的程序错误

| 内容                                       | 描述                                                         |
| ------------------------------------------ | ------------------------------------------------------------ |
| 使用未初始化的内存                         | Use of uninitialised memory                                  |
| 使用已经释放了的内存                       | Reading/writing memory after it has been free’d              |
| 使用超过 malloc分配的内存空间              | Reading/writing off the end of malloc’d blocks               |
| 对堆栈的非法访问                           | Reading/writing inappropriate areas on the stack             |
| 申请的空间是否有释放                       | Memory leaks – where pointers to malloc’d blocks are lost forever |
| malloc/free/new/delete申请和释放内存的匹配 | Mismatched use of malloc/new/new [] vs free/delete/delete [] |
| src和dst的重叠                             | Overlapping src and dst pointers in memcpy() and related functions |

这些问题往往是C/C++程序员最头疼的问题，Memcheck在这里帮上了大忙。

**Callgrind**

和gprof类似的分析工具，但它对程序的运行观察更是入微，能给我们提供更多的信息。和gprof不同，它不需要在编译源代码时附加特殊选项，但加上调试选项是推荐的。Callgrind收集程序运行时的一些数据，建立函数调用关系图，还可以有选择地进行cache模拟。在运行结束时，它会把分析数据写入一个文件。callgrind_annotate可以把这个文件的内容转化成可读的形式。

**Cachegrind**

Cache分析器，它模拟CPU中的一级缓存I1，Dl和二级缓存，能够精确地指出程序中cache的丢失和命中。如果需要，它还能够为我们提供cache丢失次数，内存引用次数，以及每行代码，每个函数，每个模块，整个程序产生的指令数。这对优化程序有很大的帮助。

**Helgrind**

它主要用来检查多线程程序中出现的竞争问题。Helgrind寻找内存中被多个线程访问，而又没有一贯加锁的区域，这些区域往往是线程之间失去同步的地方，而且会导致难以发掘的错误。Helgrind实现了名为“Eraser”的竞争检测算法，并做了进一步改进，减少了报告错误的次数。不过，Helgrind仍然处于实验阶段。

**Massif**

堆栈分析器，它能测量程序在堆栈中使用了多少内存，告诉我们堆块，堆管理块和栈的大小。Massif能帮助我们减少内存的使用，在带有虚拟内存的现代系统中，它还能够加速我们程序的运行，减少程序停留在交换区中的几率。

> 此外，lackey和nulgrind也会提供。Lackey是小型工具，很少用到；Nulgrind只是为开发者展示如何创建一个工具
>
> **注意**
>
> 1. Valgrind不检查静态分配数组的使用情况
> 2. Valgrind占用了更多的内存–可达两倍于你程序的正常使用量
> 3. 如果你用Valgrind来检测使用大量内存的程序就会遇到问题，它可能会用很长的时间来运行测试

### 内存泄漏调试

#### 例一

```cpp
#include <string>
int main()
{
    auto ptr = new std::string("Hello, World!");
    delete ptr;
    return 0;
}
```

我们先编译后再调试

```shell
mason@iz2ze1ycujbqzy2o5d6cnaz  ~/workspace/c++/memory  g++11 -g test.cpp -o test
mason@iz2ze1ycujbqzy2o5d6cnaz  ~/workspace/c++/memory  valgrind --tool=memcheck --leak-check=full ./test
==22851== Memcheck, a memory error detector
==22851== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==22851== Using Valgrind-3.15.0 and LibVEX; rerun with -h for copyright info
==22851== Command: ./test
==22851==
==22851==
==22851== HEAP SUMMARY:
==22851==     in use at exit: 0 bytes in 0 blocks
==22851==   total heap usage: 2 allocs, 2 frees, 38 bytes allocated
==22851==
==22851== All heap blocks were freed -- no leaks are possible
==22851==
==22851== For lists of detected and suppressed errors, rerun with: -s
==22851== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```

主要分析几个点

1. HEAP SUMMARY

   这里写了开辟了两次堆内存，也释放了两次，表示没有都释放完成

2. ERROR SUMMARY

   0 error表示没有错误

#### 例二

```cpp
#include <string>
int main()
{
    auto ptr = new std::string("Hello, World!");
    return 0;
}
```

我们忘记了delete，然后再检测

```cpp
mason@iz2ze1ycujbqzy2o5d6cnaz  ~/workspace/c++/memory  g++11 -g test.cpp -o test
mason@iz2ze1ycujbqzy2o5d6cnaz  ~/workspace/c++/memory  valgrind --tool=memcheck --leak-check=full ./test
==24000== Memcheck, a memory error detector
==24000== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==24000== Using Valgrind-3.15.0 and LibVEX; rerun with -h for copyright info
==24000== Command: ./test
==24000==
==24000==
==24000== HEAP SUMMARY:
==24000==     in use at exit: 38 bytes in 2 blocks
==24000==   total heap usage: 2 allocs, 0 frees, 38 bytes allocated
==24000==
==24000== 38 (8 direct, 30 indirect) bytes in 1 blocks are definitely lost in loss record 2 of 2
==24000==    at 0x4C2A593: operator new(unsigned long) (vg_replace_malloc.c:344)
==24000==    by 0x4008E1: main (test.cpp:6)
==24000==
==24000== LEAK SUMMARY:
==24000==    definitely lost: 8 bytes in 1 blocks
==24000==    indirectly lost: 30 bytes in 1 blocks
==24000==      possibly lost: 0 bytes in 0 blocks
==24000==    still reachable: 0 bytes in 0 blocks
==24000==         suppressed: 0 bytes in 0 blocks
==24000==
==24000== For lists of detected and suppressed errors, rerun with: -s
==24000== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
```

发现HEAP SUMMARY 两次未释放，然后最后的ERROR也是一个错误，然后根据 by 0x4008E1: main (test.cpp:6)，可以找出哪里的内存没有释放。

### 数组越界

```cpp
#include<iostream>
#include<string>
#include<vector>
//using namespace std;
int main()
{
   auto ptr=new std::string("hello");
   //delete ptr;
   std::vector<int> v(10, 0);
   std::cout << v[10] << std::endl;
   return 0;
}
```

```shell
 mason@iz2ze1ycujbqzy2o5d6cnaz  ~/workspace/c++/memory  valgrind --tool=memcheck --leak-check=full ./test
==30802== Memcheck, a memory error detector
==30802== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==30802== Using Valgrind-3.15.0 and LibVEX; rerun with -h for copyright info
==30802== Command: ./test
==30802==
==30802== Invalid read of size 4
==30802==    at 0x400B0E: main (test.cpp:10)
==30802==  Address 0x5a24118 is 0 bytes after a block of size 40 alloc'd
==30802==    at 0x4C2A593: operator new(unsigned long) (vg_replace_malloc.c:344)
==30802==    by 0x40108B: __gnu_cxx::new_allocator<int>::allocate(unsigned long, void const*) (new_allocator.h:104)
==30802==    by 0x400FD6: std::_Vector_base<int, std::allocator<int> >::_M_allocate(unsigned long) (stl_vector.h:168)
==30802==    by 0x400EC4: std::_Vector_base<int, std::allocator<int> >::_M_create_storage(unsigned long) (stl_vector.h:181)
==30802==    by 0x400D62: std::_Vector_base<int, std::allocator<int> >::_Vector_base(unsigned long, std::allocator<int> const&) (stl_vector.h:136)
==30802==    by 0x400C5B: std::vector<int, std::allocator<int> >::vector(unsigned long, int const&, std::allocator<int> const&) (stl_vector.h:283)
==30802==    by 0x400AF0: main (test.cpp:9)
==30802==
0
==30802==
==30802== HEAP SUMMARY:
==30802==     in use at exit: 38 bytes in 2 blocks
==30802==   total heap usage: 3 allocs, 1 frees, 78 bytes allocated
==30802==
==30802== 38 (8 direct, 30 indirect) bytes in 1 blocks are definitely lost in loss record 2 of 2
==30802==    at 0x4C2A593: operator new(unsigned long) (vg_replace_malloc.c:344)
==30802==    by 0x400AA1: main (test.cpp:7)
==30802==
==30802== LEAK SUMMARY:
==30802==    definitely lost: 8 bytes in 1 blocks
==30802==    indirectly lost: 30 bytes in 1 blocks
==30802==      possibly lost: 0 bytes in 0 blocks
==30802==    still reachable: 0 bytes in 0 blocks
==30802==         suppressed: 0 bytes in 0 blocks
==30802==
==30802== For lists of detected and suppressed errors, rerun with: -s
==30802== ERROR SUMMARY: 2 errors from 2 contexts (suppressed: 0 from 0)
```

Invalid read of size 4. 表明了错误读取。

