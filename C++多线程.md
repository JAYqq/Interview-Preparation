## 多线程基础

### 基本使用

```cpp
#include<thread>
#include<iostream>
void fun1()
{
    std::cout<<"fun1"<<std::endl;
}
//携带参数
void fun2(const int num)
{
    std::cout<<"fun2"<<" "<<num<<std::endl;
}
struct tmp
{
    void operator()()const{
        std::cout<<"tmp struct"<<std::endl;
    }
};

int main()
{
    std::thread thread1(fun1);
    std::thread thread2(fun2,3);
    std::thread thread3((tmp())); //重载()
    std::thread thread4{tmp()}; 
    std::thread thread5{[] {std::cout<<"lambda"<<std::endl;}}; //使用lambda也可以
    thread1.join();
    thread2.join();
    thread3.join();
    thread4.join();
    thread5.join();
}
```

### thread的join和detach

```cpp
#include<iostream>
#include<thread>
/*
这边主要模拟了detach和join的用处
*/
struct tmp
{
    int& num;
    tmp(int& target):num(target){}
    void operator()() const{
        for(int i=0;i<100;i++)
            std::cout<<num;
    }
};
void func()
{
    int x=9;
    tmp t(x);
    std::thread thread1(t);
    thread1.detach();  //如果是脱离了线程，那么tmp中由于是使用了引用，所以func可能会比tmp先执行完，导致错误
    // thread1.join();  //所以需要join等待线程执行完后才退出当前线程，保证栈变量在tmp执行完之前存在
}
int main()
{
    std::thread thread2(func);
    thread2.join();
}
```

detach 会脱离主线程去运行，所以无法控制该脱离的线程和当前线程的先后顺序。

join会使得当前线程等到指定线程结束后再退出。

### 使用RALL管理线程

如果线程运行过程中发生异常，之后调用的[join](https://en.cppreference.com/w/cpp/thread/thread/join)会被忽略，为此需要捕获异常并在处理异常时调用[join](https://en.cppreference.com/w/cpp/thread/thread/join)

```cpp
void f()
{
    int x = 0;
    A a(x);
    std::thread t(a);
    try
    {
        doSomethingHere();
    }
    catch(...)
    {
        t.join();
        throw;
    }
    t.join();
}
```

