# 目录

[TOC]



## 各种类型大小

https://blog.csdn.net/zy47675676/article/details/91474604?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase

对于各种类型的大小没有硬性的规定，但是有一些原则

- ANSI C规定 `char` 类型一定是8位。
- `long` 类型的长度和cpu字长一样。
- `int` 长度没有规定，但是不比 `short` 短不比 `long` 长，并且linux上支持的所有体系中 `int` 长度目前都是32位。
- `short` 和 `int` 类似，目前linux上长度都是16位。

### 静态类型和动态类型

简单来说，静态类型就是在编译期间就知道了变量的类型，比如以下：

```cpp
int age=18;
auto ptr=age;
```

动态类型就是只有到了运行阶段才知道的类型，像基类指针指向了子类后调用虚函数就会指向子类的虚函数。

## char (*p) [] 、char \*p[]、char (\*p)()的区别？

由于[]的优先级高于\*，所以char(*p)[]是指向一个数组的指针，char \*p[]指的是一个存放指针的数组。

char(\*p)()指的是返回值是char指针的一个方法

## 手写int atoi(char *str)

https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/

```c
int strToInt(char* str){
    /*
    1.基本逻辑就是先判断空格，去除；然后判断©️，记录到flag
    2.往后找数字，换算成一个整数
    这里最重要的是整数溢出的判断，因为这边的数值范围是-2^31~2^31-1，也就是[-2147483648，2147483647]，所以我们在进行ans=ans*10+r之前，需要判断一下这一层的ans是否已经溢出整数的范围，
    两种情况：
    1.ans>INT_MAX/10，也就是ans>214748364，那么一定溢出了
    2.ans==INT_MAX/10 && r>7，也就是214748364这一部分是一样的，需要比较个位，所以只要大于7，
    就是溢出了。

    */
    int ans=0;
    int flag=1;
    int r;
    while(*str==' ') str++;
    if(*str=='-') flag = -1;
    if(*str=='+' || *str=='-') str++; 
    while(*str>='0' && *str<='9')
    {
        r=*str-'0';
        if(ans>INT_MAX/10 || ans==INT_MAX/10 && r>7) return flag==1?INT_MAX:INT_MIN;
        ans=ans*10+r;
        str++;
    }
    return ans*flag;
}
```

## 指针和引用的区别

- 指针是一个变量，而引用只是别名，所以指针本身后开辟栈空间储存，而引用本身不占空间
- 指针可以有多级指针，但是引用只能一级
- 指针可以的是空指针，而引用不能指向空
- 指针的值在初始化完后可以重新指向，而引用不能重新指向新对象

## 野指针和悬空指针

### 野指针

“野指针”则是不确定其具体指向的指针。“野指针”最常来自于未初始化的指针，例如下面这段C语言代码：

void *p;

// 此时 p 是“野指针”

因为“野指针”可能指向任意内存段，因此它可能会损坏正常的数据，也有可能引发其他未知错误，

### 悬空指针

C语言中的指针可以指向一块内存，如果这块内存稍后被操作系统回收（被释放），但是指针仍然指向这块内存，那么，此时该指针就是“悬空指针”

## C和C++的区别

https://www.zhihu.com/question/28834538/answer/100698972

C++是面向对象的语言，而C是面向过程的。C++几乎是C的超集，C++比C多了很多的语法概念，就像RALL，rall是资源初始化的概念，资源的使用至少有三个阶段，也就是资源的获取，使用，释放。但是这个释放经常被忘记，C++不像java，python可以自己释放资源，而是需要程序员手动释放。所以RALL就是C++将资源获取的过程封装成一个类，通过构造函数获取资源，析构函数释放资源，这也是正好利用了C++的特性。

https://zhuanlan.zhihu.com/p/34660259（RALL原理介绍）

## const

- c++中的const默认是内部连接，c中默认是外部链接，内部连接是不能只声明不赋值的。

- c++中const对于基础类型或者全局常量不会开辟内存，而是放在符号表中，而如果是局部常量那么就会放在栈中。

- 顶层const

  表示指针本身是一个常量，以下都是

  ```cpp
  int *const num;
  const int num=42;
  ```

- 底层const

  表示指针指向的是一个常量

  ```cpp
  const int* num=&ci;
  const int& num=ci;  //声明引用的const都是底层const
  ```

- const修饰函数参数：

  我们一般这样写：

  ```cpp
  void func(A a){}
  ```

  但是这样以 **值传递**的方式会触发拷贝构造函数，拷贝会损失效率，所以如果我们不需要修改这个变量，我们可以这样：

  ```cpp
  void func(const A &a)
  ```

  指针也是一样处理。

- const 修饰函数

  这个分为两种：

  ```cpp
  const int getValue();
  int getValue2() const;
  ```

  第一种表示函数的返回值是const，第二种表示此函数的this指针是const，也就是此函数无法改变类成员变量。

### const 和 constexpr区别

- Constexpr  是编译期常量也就是编译器在编译的时候就可以计算这个值；const是运行时常量，也就是在编译期间是不知道const储存的值的

  ```c++
  const int num1=3;
  const int []={num1} //错误，编译到这里不知道num1的值
  ```

- ```c++
  const int *p=a;  //指向一个整型常量的指针
  constexpr int *p=a;   //指向一个整型的常量指针
  ```

- constexpr修饰的函数，返回值不一定是编译期常量

### const和define

1. const是运行时常量，二而define 是编译期的宏定义
2. define没有类型，所以没有类型检查，而const有类型检查在编译期间
3. define时宏展开，哪里使用哪里展开，不占内存；而const会分配内存。

### C++和C的const区别

c++中默认const是内部连接，也就是只对本文件有用，extern声明后才会变成外部链接；C中默认是外部链接。

所以c++默认链接不会创建内存给全局的字面值常量，而局部的非static const值会储存在内存空间的栈空间中

## auto

   ```c++
   const int a=9;
   auto num=a;   //num是一个整型，会忽略顶层const
   auto &num=a;  //num是一个整型常量
   ```

## delcype

我们希望编译阶段，编译器通过表达式类型推断出变量的类型：

```cpp
decltype(fun()) del=x;   //这时候可以通过fun函数返回类型判断del的类型，x是fun的返回值
int a=42,&b=1;
decltype(b) del2; //错误，因为b是引用类型，必须初始化
decltype(b+1) del3;  //正确，虽然b是引用但是b+1是一个表达式，返回一个int类型给del3
```

### Delcype和auto的区别

1. 对于引用类型，auto会自动忽视顶层const

   ```cpp
   const int num=3;
   auto b = num;    //这里的b是一个非常量int
   decltype(num) del;   //这里del就是一个常量类型
   ```

2. decltype类型加上括号就是一个引用

   ```cpp
   int num=9;
   decltype((num)) del=num;  //这样del就是一个int的引用类型，所以需要初始化
   ```

## Explicit

是为了防止类出现隐式类型转换，比如：

```cpp
#include<iostream>
using namespace std;
class Temp{
public:
    int x,y;
    Temp(int a=0,int b=0):x(a),y(b){}
};
int main()
{
    Temp tmp; //如果没有赋初始值，那么就就出错。
    tmp=1; //居然直接可以把1付给它
}
```

这样会出现隐式类型转换

```cpp
explicit Temp(int a=0,int b=0):x(a),y(b){}
```

这样就可以防止隐式类型转换了。

## NULL和nullptr

**NULL**

c语言中的NULL

```c
#define NULL ((void*)0)
```

c++中的NULL

```cpp
#define NULL 0
```

NULL在C++中是整数0，为什么NULL不能是空指针，因**为C++中不能将void类型的指针隐形转换**，所以NULL不可定义为void*。

**为什么建议使用nullptr（空指针）而不是NULL？**

1. nullptr可以转换成任意类型的指针，而NULL不行

   ```cpp
   #include<iostream>
   using namespace std;
   void test(void *p)
   {
       cout<<"p is pointer "<<p<<endl;
   }
   void test(int num)
   {
       cout<<"num is int "<<num<<endl;
   }
   int main(void)
   {
   
       test(NULL); //报错！
     	test(nullptr); //ok！
       return 0;
   }
   ```

2. 所有无用指针定义为nullptr，在析构函数中可以统一区分。

## 函数重载

相同名字不同参数，但是不能是仅仅返回值不同，因为这样会产生二义性。

相同名字不同参数的函数在编译器编译的时候会产生两个不同的名字，来表示两个不同的方法。

**类型安全连接**

道函数实际上应该是f（int），但编译器并不知道，因为它被告知—通过一个 

明确的声明—这个函数是f（char）。因此编译成功了，在C中，连接也能成功，但在C++中却不行。因为编译器会修饰这些名字，把它变成了诸如f_int之类的名字，而使用的 

函数则是f_char。当连接器试图找到f_char引用时，它只能找到f_int，所以它就会报告一条 

出错信息。这就是类型安全连接。

## static

https://zhuanlan.zhihu.com/p/37439983

```cpp
#include<iostream>
using namespace std;
char get_num(const char* chararr=0){
    static const char *s;
    if(chararr){
        s=chararr;
    }
    return *s++;
}
int main()
{
    char *str="scw3837";
    get_num(str);
    for(int i=0;i<3;i++){
        cout<<get_num()<<endl;  //输出c、w、3
    }
    return 0;
}
```

### 静态成员

静态成员可以脱离类的作用域，独立于该类的任意对象

- 静态成员函数可以直接访问static成员但是不能直接访问非static
- static成员函数没有this指针，因为static是独立于类的对象的，this指向的正是对象
- static成员不能在定义的时候初始化，**只能在类的外部赋值** 但是只要是 static const int a=30，这样有const修饰就可以（const是内部连接，必须初始化就定义）
- 非static的数据成员不能作为另一个成员函数的实参，因为它的值不能独立于所属的对象，而static变量可以。也就是对象是不能通过访问符去访问到实参的，而static修饰的可以当作是一个全局变量，所以是可以的。
- 一个类中的所有静态成员变量都在一个静态储存区内，所以对于一个类的所有对象而言，这个静态变量相当于一个全局变量
- 静态数据成员可以和普通成员一样用private、protected、public这样修饰
- sizeof一个有静态变量的类发现这个静态成员不包含在里面

### **和全局变量相比，静态数据成员的优势**

1. 静态数据成员仅在单个程序中全局，不会与其他文件命名发生冲突
2. 可以用private等修饰符修饰

### 静态成员函数

- 静态成员函数属于类本身而不是实例，所以没有this指针，不能访问一般的数据成员只能访问静态成员，因为静态成员函数在实例被创建的时候就可以调用了，但是此时非静态成员还没定义
- 

## 引用

- 不能有NULL引用

- 指针引用

  ```cpp
  void increment(int*& i){i++}
  ```

  这里是i地址增加了而不是i指向的内容增加了

- 

## union

https://zhuanlan.zhihu.com/p/131458347

联合体，体内的变量共享内存大小，大小为体内最大的值大小。



## 内联函数

https://zhuanlan.zhihu.com/p/101090186

- C++编译器编译的最终产物是程序，程序就是一连串的指令集合，运行时系统将这些指令放到内存中，所以这些指令都有对应内存地址。程序执行时，CPU的控制器会将这些指令不断的将代码段的指令拿到控制器的指令指针寄存器，然后结合运算单元和数据单元来执行指令，当执行到函数调用指令后，会先保存该指令的地址，并把函数参数复制到函数的堆栈中，函数执行完后再跳转到原地址。
- 内联函数将自己的代码和其他程序联合起来，像是被嵌套进其他程序，这样程序就不需要跳转，而是顺序执行了，因此内联函数的运行速度会更快，但是代价就是消耗更多的内存
- 所有的类内部的函数是默认内联函数（除了虚函数，并且是在类内部定义实现的，在类外实现就不是内联了），但是是否采用内联函数是编译器决定的，而不是一定会用。
- 虚函数当非多态调用的时候也是可以使用内联的：https://www.zhihu.com/question/45894112/answer/100282374
- 

## C++程序的处理过程

### 预处理阶段

g++ -E demo.cpp -o demo.i

主要处理的是#include和#define，把引入的头文件放到引入位置，把define的宏用实际的字符串。

### 编译阶段

g++11 -s demo.i -o demo.s

检查代码的规范性、语法错误，然后翻译成汇编语言

### 汇编阶段

g++11 -c demo.s -o demo.o

把.s文件转换成.o文件

这是一个二进制文件，里面包含了一些全局变量、二进制可执行代码、符号表（记录了函数和变量）、只读数据等。

### 链接阶段

因为代码里面有些函数是没有被实现的，像printf、cout这样的函数，虽然在引入的头文件上有这些函数声明，但是没有被实现。所以需要将这些函数从函数库链接进来，一般从默认从/usr/lib下找

主要分为 **静态链接库和动态链接库**

- 动态链接库

  在编译链接时并没有把库文件的代码加入到可执行文件中，而是在程序执行时由运行时链接文件加载库，这样可以节省系统的开销，一般是.so文件，window下是.dll

- 静态链接库

  在链接阶段，会将汇编生成的目标文件.o与引用到的库一起链接打包到可执行文件中**，linux下是.a文件，windows下是.lib文件

#### 静态链接的时候发生了什么？

最后的可执行文件是ELF格式的，分成了可以加载到内存的代码段和数据段，将小的section组合成大的段，并在开头会有段表头。静态临界库被加载后就会和代码段合并，数据段也会合并。**所以，如果静态链接库更新了，源程序不重新编译的话，不会用到最新的库**

#### 动态链接的时候发生了什么？

https://time.geekbang.org/column/article/90855

基于动态链接编译出来的可执行文件ELF格式稍有不同，主要多了三个东西：

1. 动态连接器，运行时的链接动作都是它做的
2. PLT（过程链接表）
3. GOT（全局偏移量表）

比如现在有个源程序，需要调用libcurd.so里面的create函数，在编译阶段，程序时无法知道调用哪里的create函数的，所以所以就会在PLT中建立一项包含了一些代码的行，这些代码叫做代理代码。执行的时候是通过调用代理代码去调用create函数。而GOT里面会存放create真正的内存地址，这样代理代码就能知道调用哪里的create了。

### 执行阶段

最后可执行文件执行的时候，我们是调用了exec这个系统调用，它会去调用load_elf_binary函数

## 动态链接库和静态链接库制作

- 概念

  上面有

- 制作

  1. 动态链接库

     Max.cpp

     ```cpp
     int max(int a, int b, int c)
     {
        int max = ( a < b ) ? b : a;
        return ( ( max < c ) ? c : max );
     }
     ```

     ```shell
     g++11 -fPIC -shared -o libmax.so demo.cpp
     ```

     生成了.so文件，`PIC` 是 Position Independent Code 的缩写，表示要生成位置无关的代码，这是动态库需要的特性；`-shared` 是链接选项，告诉gcc生成动态库而不是可执行文件

     Max.h

     ```cpp
     #ifndef __MAX_H__
     #define __MAX_H__
     
     int max(int a, int b, int c);
     
     #endif
     ```

     Test.cpp

     ```cpp
     #include <stdio.h>
     #include "max.h"
     
     int main(int argc, char *argv[])
     {
         int a = 12, b = -2, c = 120;
         printf("The max value of 12, -2 and 120 is %d.\n", max(a, b, c));
         return 0;
     }
     ```

     ```c++
     g++11 max.cpp -L. -lmax -o max
     ```

     测试

  2. 静态链接库

     ar命令

比如get_num函数如果不传递参数chararr，那么就会使用静态区变量

### 内部连接和外部链接

https://zhuanlan.zhihu.com/p/150001991

每个cpp文件都是以一个单独的编译单元，每个编译单元就是独立的单元，相互不可见。

- 内部连接（static）

  如果一个名称对编译单元来说是局部的，在链接的时候其他编译单元无法链接到它且不会与其他编译单元中的同样名称相冲突。（例如被关键字static，inline标识）

- 外部链接（extern）

  如果一个名称对编译单元来说不是局部的，而在链接的时候其他的编译单元可以访问它，也就是说它可以和别的编译单元交互。

## 宏定义#define

宏替换，被define替换的值在最后编译出来的代码中是不存在的，因为在预处理阶段就会被替换掉。比如#define success 1，最后编译的代码中不会有success，而是都被替换成1。

### define和const的区别在于：

1. 上面说明的这点，而const定义的值存在于最后的编译代码
2. define无法指定变量的类型

## 封装、继承、多态

是面向对象的三大特性

### 封装

面向对象的基本特征之一，就是将一系列功能相关的方法统一放到一个类中，类可以控制函数或者变量的权限。

### 继承

是一个类对于功能复用的措施，子类可以继承父类的一些功能函数，一个类继承而来的成员的访问权限受两个因素的影响，一个是基类中成员的访问权限，另一个是以何种权限去继承基类。第二种继承方式其实是为了限制派生类的实例访问权限，比如类B是基类A的派生类，并且以private方式继承，所以B的实例是无法访问基类A中的成员，即使这个基类成员在基类中是public的。

继承中有一些注意点：

- 基类中的析构函数一般设计成虚函数，但不一定是纯虚的
- 在class后加上final可以防止类被继承

### 多态

多态说的就是派生类可以重新定义基类中的虚函数，实现自己的功能，这可以有效增强程序的扩充性。

![](https://img-blog.csdn.net/20180813114655864?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NDEyNTgy/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

#### 静态多态

函数的重载或者是模版编程

#### 动态多态

父类的指针可以根据具体指向的子类对象执行不同的函数。

而动态多态里面最重要的机制就是虚函数，虚函数最重要的特性就是动态绑定，也就是对象调用哪个虚函数取决于这个对象绑定的是哪种类型的实例（28中的代码），而支撑虚函数动态绑定功能的机制是虚函数表（29）

## 虚函数

继承过程中，主要有两种成员函数，一种是希望基类可以直接继承不需改变的函数，**另一种的要求派生类重写并覆盖的函数**。对于第二种，就是定义为**虚函数**。任何除了构造函数的非静态函数都可以被定义成抽象函数。

### 虚继承

虚拟继承是多重继承中特有的概念。虚拟基类是为解决多重继承而出现的。
如:类D继承自类B1、B2，而类B1、B2都继 承自类A，因此在类D中两次出现类A中的变量和函数。为了节省内存空间，可以将B1、B2对A的继承定义为虚拟继承，而A就成了虚拟基类,虚拟继承在一般的应用中很少用到，所以也往往被忽视，这也主要是因为在C++中，多重继承是不推荐的，也并不常用，而一旦离开了多重继承，虚拟继承就完全失去了存在的必要因为这样只会降低效率和占用更多的空间。

### 虚函数动态绑定

虚函数的调用是在运行阶段动态绑定的，而不是在编译阶段静态绑定的

![v2-1854c774aa4a93c8e85e7458f74ecc02_1440w.jpg](https://i.loli.net/2020/07/26/3kx8ej5TmLYrRGX.jpg)

- 基类中的虚函数被子类继承后子类中这个方法也同样是虚函数。

- 继承而来的虚函数返回类型，参数都要一样

- 只有虚函数，在子类中才能override:

  ```cpp
  class A{
    virtual void get_num(int num);
  }
  class B:public A{
    void get_num(int num) override;
  }
  ```

- 在成员函数后加上final，在子类中就不能被重写

- 派生类的override虚函数定义必须和父类完全一致。除了一个特例，如果父类中返回值是一个指针或引用，子类override时可以返回这个指针（或引用）的派生。例如，在上面的例子中，在Base中定义了 virtual Base* clone(); 在Derived中可以定义为 virtual Derived* clone()。可以看到，这种放松对于Clone模式是非常有用的。

### 纯虚函数

为了方便使用多态的特性，我们需要在基类中定义一些虚函数，并且有虚函数的基类有时候不需要进行实例化，比如动物类可以有猫狗这样的派生类，但是动物本身的实例是没有意义的，所以这样的类可以被定义成抽象类，**而抽象类的定义就是至少含有一个纯虚函数的类**，纯虚函数声明如下： virtual void funtion1()=0

**析构函数可以是纯虚的，但纯虚析构函数必须有定义体，因为析构函数的调用是在子类中隐含的。**

### 动态绑定和静态绑定

这个可以看23虚函数那边，虚函数实现机制就是动态绑定的。

如果类不包含虚函数，那么编译器在编译期间就会把成员函数的地址确定下来，后面调用的时候只是去对应的地址（在符号表中）去拿就行了，**这就是静态绑定**

``` cpp
class A{
  virtual void show();
}
class B:public A{
  virtual void show();
}
int main(){
  B b;
  A* a=&b;
  a->show();//这边调用的是B的show函数，虽然a是A指针类型
}
```

上面这个现象：基类指针指向了派生类的对象，调用的虚函数会是派生类的虚函数叫做 **动态绑定**，如果不是虚函数，那么无论a怎么指向，都是调用基类的函数。**动态绑定的原理就是虚表的实现**

### 虚表

在有虚函数的类编译期间，会在该类编译成二进制文件并加载到内存中的时候在堆区加一个虚表指针指向全局数据区中的虚表，所以如果在程序中使用sizeof打印有虚函数的类大小，发现会比不含虚函数的类大几个字节（根据计算机决定，32位是32/8=4字节，64位是8字节），虚表中会有多个虚表指针指向不同虚函数的内存地址。**每个类的实例都会有自己的虚表指针**，所以动态绑定的时候就是根据类指针去对应的虚表中寻找虚函数地址。

### 构造函数和析构函数可以是虚函数吗？

构造函数不能是虚函数，因为虚函数是为了多态的实现，并且是动态绑定的，动态绑定的前提是有对象，但是有对象的前提是有构造函数实现，所以互相矛盾。

### 构造函数和析构函数中能否调用虚函数？

能，但是不建议。为什么？因为如果构造函数中调用虚函数，那么继承的时候是先调用基类构造函数然后调用子类的，所以如果在构造函数中调用虚函数，那么基类调用的虚函数就是基类的虚函数，到了子类也是调用基类的虚函数，这就破坏了多态的原则。

而析构函数，是先调用子类的析构函数，此时是调用的子类自己的虚函数，到了基类后，调用的是基类的虚函数，不是子类的。

**所以总结来说，如果构造函数和析构函数中调用虚函数，就不会触发多态，这不是语法上的问题，而是标准的问题**

## C++的内存管理机制

https://zhuanlan.zhihu.com/p/51855842

### 内存管理器做了什么？

在堆上分配内存，有些语言可能使用 new 这样的关键字，有些语言则是在对象的构造时隐式分配，不需要特殊关键字。不管哪种情况，程序通常需要牵涉到三个可能的内存管理器的操作：

1. 让内存管理器分配一个某个大小的内存块
2. 让内存管理器释放一个之前分配的内存块
3. 让内存管理器进行垃圾收集操作，寻找不再使用的内存块并予以释放

C++ 通常会做上面的操作 1 和 2。Java 会做上面的操作 1 和 3。而 Python 会做上面的操作 1、2、3。这是语言的特性和实现方式决定的。

### 栈展开

这也是C++内存管理比较关键的一点，就是C++编译器在程序发生异常的时候会自动调用当前栈内对象的析构函数

```cpp
#include <stdio.h>

class Obj {
public:
  Obj() { puts("Obj()"); }
  ~Obj() { puts("~Obj()"); }
};

void foo(int n)
{
  Obj obj;
  if (n == 42)
    throw "life, the universe and everything";
}

int main()
{
  try {
    foo(41);
    foo(42);
  }
  catch (const char* s) {
    puts(s);
  }
}
/*
Obj()
~Obj()
Obj()
~Obj()
life, the universe and everything
*/
```

### RALL

```cpp
#include<iostream>
using namespace std;
enum shape_type {
    circle,
    square
};
//形状基类
class shape {
public:
    virtual unsigned get_area()=0;
    virtual void show()=0;
    virtual ~shape(){};
};
//圆形
class Circle :public shape
{
private:
    unsigned rad;
public:
    unsigned get_area (){return 3*rad*rad;}
    void show(){cout<<"circle"<<endl;}
    Circle(unsigned rad):rad(rad){}
};
//正方形
class Square :public shape
{
private:
    unsigned rad;
public:
    void show(){cout<<"square"<<endl;}
    unsigned get_area(){return rad*rad;}
    Square(unsigned rad):rad(rad){}
    // ~square();
};
class Factory{
public:
    shape* create_shape(shape_type type) {
        switch (type)
        {
        case circle:
            return new Circle(3);
            break;
        case square:
            return new Square(3);
            break;
        default:
            break;
        }
    }
};

int main()
{
    Factory fac;
    shape* s1=fac.create_shape(shape_type::circle);
    s1->show();
    cout<<s1->get_area()<<endl;
    shape* s2=fac.create_shape(shape_type::square);
    s2->show();
    cout<<s2->get_area()<<endl;
  	//本应该需要delete
    return 0;
}
```

上面的工厂类对不同shape进行了实例创建，但是，这也太容易忘记delete了（上面main中我就没有delete导致了 **内存泄漏**）

根据上面的栈展开和析构函数，我们可以想到把这个实力放到一个对象中，这个对象就在main的栈中，就会主动调用析构函数了，像Python一切皆对象就是帮我们做掉了释放内存的操作。

```cpp
....
....
class shape_wrapper{
public:
    explicit shape_wrapper(shape* ptr=nullptr):ptr_(ptr){}
    shape* get_ptr(){return ptr_;}
    ~shape_wrapper(){delete ptr_;}
private:
    shape* ptr_;
};
int main()
{
    Factory fac;
    shape_wrapper circle_wrapper(fac.create_shape(shape_type::circle));
    cout<<circle_wrapper.get_ptr()->get_area()<<endl;
    circle_wrapper.get_ptr()->show();
    return 0;
}
```

这样我们就把工厂类创建的实例放到了shape_wrapper中，让编译器帮我们主动调用析构函数，妈妈再也不用担心我们忘记释放内存啦。

### 共享内存

## 智能指针

大魔王终于来了。

### Shared_ptr

本质就是使用引用计数，和Python的引用计数相同，当一个对象的引用计数为0的时候，就会主动调用对象的析构函数来释放动态内存。

shared_ptr中调用了new动态开辟内存空间。

```cpp
#include <memory>
#include <iostream>
class Test
{
public:
    Test()
    {
        std::cout << "Test()" << std::endl;
    }
    ~Test()
    {
        std::cout << "~Test()" << std::endl;
    }
};
int main()
{
    std::shared_ptr<Test> p1 = std::make_shared<Test>();
    std::cout << "1 ref:" << p1.use_count() << std::endl;
    {
        std::shared_ptr<Test> p2 = p1;
        std::cout << "2 ref:" << p1.use_count() << std::endl;
    }
    std::cout << "3 ref:" << p1.use_count() << std::endl;
    return 0;
}
```

结果如下：

```text
Test()
1 ref:1
2 ref:2
3 ref:1
~Test()
```

shared_ptr 的内存占用是裸指针的两倍。因为除了要管理一个裸指针外，还要维护一个引用计数。因此相比于 unique_ptr, shared_ptr 的内存占用更高

### weak_ptr

https://zhuanlan.zhihu.com/p/73807983

它主要的是用来辅助shapred的，因为shared既然是引用计数，那么当出现循环引用的时候就会出现计数无法到达0的时候，无法调用析构函数。

## 类的拷贝、移动、赋值、销毁

### 拷贝

#### 浅拷贝和深拷贝

https://zhuanlan.zhihu.com/p/94868622

浅拷贝就是两个指针指向同一块内存数据，深拷贝是不同对象有不同内存块存放相同的数据。

具体实现就是“=“的重载。

#### 拷贝构造函数

```cpp
class A{
  A(const A&); //必须是一个引用类型，并且最佳是const引用
}
```

与合成构造函数不同，合成构造函数也就是编译器默认给我们的类加上的构造函数，前提是我们没有给出任何的构造函数声明。而合成构造函数编译期都会给出的。

#### 合成拷贝构造函数

也就是编译器为我们自动准备的拷贝构造函数，一般情况不会有问题，但是如果拷贝的值涉及到指针或者引用，那么就会导致不同实例引用了同一变量。

#### 拷贝构造函数在一下情况发生

- 将一个对象作为实参传递给一个非引用类型的形参
- 使用聚合类初始化成员的方式

#### 拷贝构造函数和赋值操作符

对于拷贝构造来说，归根结底，落脚点在构造函数上。所以调用拷贝构造的时候，一定是这个对象不存在的时候，如下面这句

```cpp
 bulk_item a = bulk_item(10);
```

那么，a是不存在的，而且是通过其它的bulk_item对象构造出来的，那么则调用的是拷贝构造函数。

如果是

```cpp
 bulk_item a(1);
 a =  bulk_item(10);
```

那么这里就调用的是赋值操作符，因为a是已经存在的对象了，不需要构造了。

### 赋值

https://zhuanlan.zhihu.com/p/94868622

```cpp
#include<stdlib.h>
#include<stdio.h>
#include<string>
#include<iostream>
class MyString
{
private:
    char *str;
public:
    MyString():str(new char[1])
    {
        str[0]=0;
    }
    MyString(char* sr)
    {
        strcpy(str,sr);
    }
    ~MyString()
    {
        delete[] str;
    }
    MyString& operator=(const char *tmp)
    {
        delete[] str;
        str=new char[strlen(tmp)+1];
        strcpy(str,tmp);
        return *this;
    }
    MyString& operator=(const MyString& s)
    {
        if(&s==this)
        {
            return *this;
        }
        delete[] str;
        str=new char[strlen(s.str)+1];
        strcpy(str,s.str);
        return *this;
    }
    void get_str()
    {
        std::cout<<str<<std::endl;
    }
};
int main()
{
    // char *sr="Hello";
    MyString mstr;
    mstr.get_str();
    mstr="Hello";
    mstr.get_str();
    MyString ystr;
    ystr="World";
    mstr=ystr;
    mstr.get_str();
    return 0;
}
```

注意，这是赋值运算符的重载，仅仅是重载，这里把tmp2的值赋给tmp1，tmp2是还有别的用处的，所以与移动构造函数或者是移动赋值运算符不同的是，移动赋值运算符接收一个右值，右值是即将消亡的对象，可以看38里面的代码。

### 移动

移动构造函数是在一个临时对象会消亡但是它的资源本身还是有用的时候，只需要移动就可以了。

1. 理一理复制构造函数、赋值运算符重载、移动构造函数、移动赋值运算符重载（**Important**）

   ```cpp
   class Person {
   private:
       int* data;
   
   public:
       Person() : data(new int[1000000]){}
       ~Person() { delete [] data; }
   
       // 拷贝构造函数，需要拷贝动态资源
       Person(const Person& other) : data(new int[1000000]) {
           std::copy(other.data,other.data+1000000,data);
       }
   
       // 移动构造函数，无需拷贝动态资源
       Person(Person&& other) : data(other.data) {
           other.data=nullptr; // 源对象的指针应该置空，以免源对象析构时影响本对象
       }
     	
     	//赋值运算符，但是这样会涉及到很大一块内存的拷贝问题，所以才需要一个
     	Person& operator=(const Peronsn& p){
         	delete data;
         	data=new int[1000000];
         	std::copy(p.data,p.data+1000000,data);
         	return *this;
       }
     	
     	//移动赋值运算符
     	Person& operator=(Person&& p):data(p.data){
         	data=nullptr;
         	return *this;
       }
   };
   
   void func(Person p){
       // do_something
   } 
   
   int main(){
       Person p;
       func(p); // 调用Person的拷贝构造函数来创建实参
       func(Person()); // 调用Person的移动构造函数来创建实参
     	Person p2;
     	p=p2; //调用赋值运算符重载(这里还是普通赋值运算符)
     	p=std::move(p2); //调用移动赋值运算符
       return 0;
   }
   ```

   注意这里可以调用move函数强制调用移动赋值运算。

2. 析构函数不能为删除的函数

   删除的函数定义是这样：

   ```c++
   void func()=delete;
   ```

   如果是把拷贝构造函数设为delete，那么表示无法使用该类的拷贝构造。

   但是析构函数如果被删除，那么就无法删除这个类的对象了。

   ```cpp
   class S{
      ~S()=delete;
   }
   S s1;  //错误
   S *s1 = new S();   //正确但是无法使用析构函数
   ```

   ## 异质链表

   普通链表每个节点都是相同的类型，但是如果对于不同类型的数据想把他们串成链表，就需要抽离出他们的共同点，然后以他们的共同点去形成链表，但是每个节点里面都有一个指针去指向那个不同类型的部分。

   ## 左值和右值

   简单的来说，当一个对象被用作右值的时候，用的是对象的值，而左值就是对象的地址。

   ### 右值引用和左值引用

   左值引用就是我们最常遇见的：

   ```cpp
   void process_copy(const std::vector<int>& vec_) {
       // do_something
       std::vector<int> vec(vec_); //  不能修改左值，所以要拷贝vector
       vec.push_back(42);
   }
   ```

   右值引用在移动构造函数中很重要

   右值引用有一个很重要的性质，只能绑定到一个即将销毁的对象上

   ```cpp
   int num=9;
   int &&r=num; //错误，num是左值，不能将右值绑定到左值上
   int &rr=num*7;  //错误，num*7是一个右值
   const int &rrr=num*7;  //正确，可以将一个右值绑定到const引用上
   int &&rb=num*7;  //正确，可以将右值绑定，对口
   ```

   ### 右值引用是如何提高性能的？

   https://zhuanlan.zhihu.com/p/54442127

   在C++中，最常见的右值就是函数（包括普通函数和构造函数）的返回值。当一个函数调用完成后，这些没有变量名的返回值通常会被赋值给等号左边的一个左值变量，在没有右值引用的时代，这其实是一个极其消耗性能浪费资源的过程。首先，需要释放左值变量原有的内存资源，然后根据返回值的大小重新申请内存资源，接着才是将返回值的数据复制到左值变量新申请的内存中，最后还要释放掉返回值的内存资源。经过这样四个步骤，才能最终完成一个函数返回值的赋值操作。

   而移动构造就是利用右值引用，因为右值引用的对象是马上需要销毁的对象，但是我们需要复制一个相同的对象，所以我们不需要重新创建空间、复制内容、销毁原来空间等操作，只需要转移一下管理者就可以了。

   ```cpp
   #include <iostream>
   #include <cstring>
   using namespace std;
   class MemoryBlock
   {
   public:
       MemoryBlock(const unsigned int nSize)
       {
           cout << "创建对象，申请内存资源" << nSize << "字节" << endl;
           m_nSize = nSize;
           m_pData = new char[m_nSize];
       }
       ~MemoryBlock()
       {
           cout << "销毁对象";
           if (0 != m_nSize)
           {
               cout << "，释放内存资源" << m_nSize << "字节";
               delete[] m_pData;
               m_nSize = 0;
           }
           cout << endl;
       }
       MemoryBlock(MemoryBlock &&other) noexcept
       {
           cout << "移动资源" << other.m_nSize << "字节" << endl;
           // 将目标对象的内存资源指针直接指向源对象的内存资源
           // 表示将源对象内存资源的管理权移交给目标对象
           m_pData = other.m_pData;
           m_nSize = other.m_nSize; // 复制相应的内存块大小
                                    // 将源对象的内存资源指针设置为nullptr
           // 表示这块内存资源已经归目标对象所有
           // 源对象不再拥有其管理权
           other.m_pData = nullptr;
           other.m_nSize = 0; // 内存块大小设置为0
       }
       // MemoryBlock &operator=(const MemoryBlock &other)
       // {
       //     if (this == &other)
       //     {
       //         return *this;
       //     }
       //     cout << "释放已有内存资源" << m_nSize << "字节" << endl;
       //     delete[] m_pData;
       //     m_nSize = other.GetSize();
       //     cout << "重新申请内存资源" << m_nSize << "字节" << endl;
       //     m_pData = new char[m_nSize];
       //     cout << "复制数据" << m_nSize << "字节" << endl;
       //     memcmp(m_pData, other.GetData(), m_nSize);
       //     return *this;
       // }
       // 可以接收右值引用为参数的赋值操作符
       MemoryBlock &operator=(MemoryBlock &&other)
       {
           // 第一步，释放已有内存资源
           cout << "释放已有资源" << m_nSize << "字节" << endl;
           delete[] m_pData;
           // 第二步，移动资源，也就是移交内存资源的管理权
           cout << "移动资源" << other.m_nSize << "字节" << endl;
           m_pData = other.m_pData;
           m_nSize = other.m_nSize;
           other.m_pData = nullptr;
           other.m_nSize = 0;
   
           return *this;
       }
   
   public:
       unsigned int GetSize() const
       {
           return m_nSize;
       }
       char *GetData() const
       {
           return m_pData;
       }
   
   private:
       unsigned int m_nSize;
       char *m_pData;
   };
   //创建一块内存空间，返回内存块对象
   MemoryBlock CreateBlock(const unsigned int nSize)
   {
       MemoryBlock mem(nSize);
       char *p = mem.GetData();
       memset(mem.GetData(), 'A', mem.GetSize());
       return mem;
   }
   int main()
   {
       MemoryBlock block(256);
       block = CreateBlock(1024);
       cout << "创建的对象大小是" << block.GetSize() << "字节" << endl;
       return 0;
   }
   ```

   这里因为CreateBlock是一个函数，函数返回值是一个右值对象，所以我们可以将赋值操作符参数转为右值引用，直接将对象管理权转交。

   而接收右值引用的构造函数就是 **移动构造函数**

   ## 为什么移动构造函数后面需要加noexcept

   noexcept表示我们的构造函数不会抛出异常，因为其实根本上是因为移动构造函数不分配任何资源，只是将资源的管理权转让给了目标，所以通常不会抛出异常，如果不加的话就会标准库知道我们这个移动构造函数可能会抛出异常，并且为了这个可能而需要做一些其他额外操作。

   另外，如果移动构造函数发生了异常，也就是出现移动没有成功但是旧的对象却释放了（因为移动构造函数接收即将销毁的对象），那么就无法适从了；但是如果是拷贝构造函数，旧的对象一直存在不会影响。所以如果有noexcept修饰，就能显示说明不会有异常，再加上符合右值是一个临时对象的原则，就会调用移动构造函数

   ## sizeof

   不可用于函数

   ### 对于常见类型

   - ANSI C规定 `char` 类型一定是8位。
   - `long` 类型的长度和cpu字长一样。
   - `int` 长度没有规定，但是不比 `short` 短不比 `long` 长，并且linux上支持的所有体系中 `int` 长度目前都是32位。
   - `short` 和 `int` 类似，目前linux上长度都是16位。

   ### 对于指针

   当操作数是指针时， `sizeof` 依赖于编译器。

   例如Microsoft C/C++7.0中， `near` 类指针字节数为2， `far` 、 `huge` 类指针字节数为4。

   **一般Unix的指针字节数为4**。

   ### 对于数组

   当操作数具数组类型时，其结果是数组的总字节数。

   如果操作数是函数中的数组形参或函数类型的形参， `sizeof` 给出其指针的大小。

   ### 对于结构体

   需要内存对齐

   ```cpp
   struct MyStruct 
   { 
       double dda1; 
       char dda; 
       int type 
   }；
   //8+1+3+4=16，16是8倍数，ok！
   struct MyStruct 
   { 
       char dda; 
       double dda1; 
       int type 
   }；
   //1+7+8+4=20,8最小整数倍是24，所以是24
   /*
   设置默认参数n，如果n小于对应值，那么取n否则取对应值；最后的最小整数倍也是取min(结构体中最大数据，n)
   */
   #pragma pack(push) //保存对齐状态 
   #pragma pack(4)//设定为4字节对齐 
   struct test 
   { 
       char m1; 
       double m4; 
       int m3; 
   }; 
   #pragma pack(pop)//恢复对齐状态
   //1+3+8+4=16，16是n=4最小整数倍，ok
   ```

   sizeof(空类)=1

   因为类是需要被实例化的，空的类也是可以实例化的，但是如果空类大小为0，那么就无法去表示一个实例在内存中的空间，如果一个指针指向这个实例，那么这个指针就找不见北了，所以一个字节就可以表示在内存中的地址了。

   ## 函数指针

   https://zhuanlan.zhihu.com/p/37306637

   ```cpp
   #include<iostream>
   using namespace std;
   int foo()
   {
       cout<<"foo"<<endl;
   }
   int boo()
   {
       cout<<"boo"<<endl;
   }
   int goo(int num)
   {
       cout<<num<<endl;
   }
   int main()
   {
       int (*func_ptr)()=foo;
       func_ptr();
       func_ptr=boo;
       func_ptr();
     	int (*func_ptr2)(int)=goo; //需要有一个参数
       func_ptr2(3);
       cout<<reinterpret_cast<void*>(foo)<<endl;
   }
   ```

   ### 将函数用于参数传递

   ```cpp
   #include<iostream>
   using namespace std;
   int add(int a,int b)
   {
       // cout<<a+b<<endl;
       return a+b;
   }
   int sub(int a,int b)
   {
       // cout<<a-b<<endl;
       return a-b;
   }
   void handle(int num1,int num2,int(*func_ptr)(int a,int b))
   {
       cout<<func_ptr(num1,num2);
   }
   int main()
   {
       handle(3,2,add);
       handle(3,2,sub);
       return 0;
   }
   ```

   ## GDB调试

   首先在编译的时候需要加上-g参数：

   ```shell
   g++11 -g demo.cpp -o demo
   ```

   表示编译的时候产生调试信息

   ### 基本调试命令

   - **显示图形化代码 Ctrl+x+a**，或者进入调试界面的时候使用gdb demo -tui这样的形式
   - 启动程序 r (run)
   - 断点 b (breakpoint)
   - 清除/禁用/启用断点 delete/disable/enable
   - 单步 s (step 碰到函数会进入)
   - 单行 n (next 碰到函数不会进行, 而是整条执行)
   - 执行到下一个断点 c (continue)
   - 查看变量 p (print)+name
   - 显示变量 display+name
   - 查看当前调用堆栈 bt (backtrace)
   - 查看某一层调用代码 f (frame)

## 段错误

指访问的内存超出了系统所给这个程序的内存空间。

## C++中重载、重写和隐藏

https://zhuanlan.zhihu.com/p/97720017
重点在于，重载是在同一作用域下定义，重写和隐藏是在不同作用域中

### C语言中为什么不能支持函数重载？

编译器在编译.c文件时，只会给函数进行简单的重命名；具体的方法是给函数名之前加上”_”;所以加入两个函数名相同的函数在编译之后的函数名也照样相同；调用者会因为不知道到底调用那个而出错；

### C++中函数重载底层是如何处理的？

在.cpp文件中，虽然两个函数的函数名一样，但是他们在符号表中生成的名称不一样。

### 函数重载是一种静态多态

多态：用同一个东西表示不同的形态；多态分为静态多态（编译时的多态）；动态多态（运行时的多态）；函数重载是一种静态多态；

## 问问更健康

### 用C++设计一个不能被继承的类

将构造函数或析构函数设为为私有函数，所以该类是无法被继承的。

```cpp
#include<iostream>
using namespace std;
class A{
private:
    A(){cout<<"A"<<endl;}
    ~A(){cout<<"~A"<<endl;}
public:
    static A* get_A(){
        A *a=new A();
        return a;
    }
    static void delete_A(A* a)
    {
        delete a;
    }
};
class B:public A{
public:
    B(){cout<<"B"<<endl;}  //这是错误的，因为A的构造函数是私有无法被访问
};
int main()
{
    A* a=A::get_A();
    B a; //错误
    // delete a;  //错误，因为delete a需要访问A的析构函数，但是析构函数也是私有的
    A::delete_A(a);  //只能通过这样去删除
}
```

### 如何定义一个只能在堆上定义对象的类?栈上呢

只能在堆内存上实例化的类：将析构函数定义为private，在栈上不能自动调用析构函数，只能手动调用。也可以将构造函数定义为private，但这样需要手动写一个函数实现对象的构造。

### 只能在栈内存上实例化的类

将函数operator new和operator delete定义为private，这样使用new操作符创建对象时候，无法调用operator new，delete销毁对象也无法调用operator delete。

### i++和++i的区别

两点区别：

1. i++是返回i原值，然后自增，++i是先自增然后返回增加的后值
2. **i++是右值，++i是左值**

第一点比较明了，第二点在于i++和++i的实现

++i

```cpp
int& int::operator++()
{
  *this+=1;
  return *this;
}
```

i++

```cpp
const int::operator++(int)
{
  int tempVal=*this;
  *this+=1;
  return tempval;
}
```

所以很明显，++i返回的是一个临时变量，而临时变量是右值。



