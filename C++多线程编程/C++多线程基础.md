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

detach 会脱离主线程去运行，所以无法控制该脱离的线程和当前线程的先后顺序，线程分离后与主线程无法直接交互，也不能被join

join会使得当前线程等到指定线程结束后再退出。

### detach脱离线程的应用

分离线程称为守护线程，即没有任何显式接口并运行在后台的线程，其特点是长时间运行。比如有一个文档处理应用，为了同时编辑多个文档，每次打开一个新文档则可以开一个分离线程

```cpp
void edit_document(const std::string& filename)
{
    open_document_and_display_gui(filename);
    while (!done_editing())
    {
        user_command cmd=get_user_input();
        if (cmd.type == open_new_document)
        {
            const std::string new_name = get_filename_from_user();
            std::thread t(edit_document, new_name);
            t.detach();
        }
        else
        {
            process_user_input(cmd);
        }
    }
}
```



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

```cpp
#include<iostream>
#include<thread>
class Thread_handle{
private:
    std::thread& th;
public:
    Thread_handle(std::thread& t):th(t){}
    ~Thread_handle(){
        if(th.joinable()) th.join();
        // std::cout<<"~"<<std::endl;
    }
    Thread_handle& operator=(const Thread_handle&)=delete; //将赋值重载禁用
};
struct tmp
{
    int& num;
    tmp(int& target):num(target){}
    void operator()() const{
        for(int i=0;i<100;i++)
            std::cout<<num;
    }
};
int main()
{
    int a=9;
    tmp temp(a);
    std::thread th1(temp);
    Thread_handle t_handle(th1);
}

```

这样就可以不用担心线程等待的问题了。

### 线程管理权转移

```cpp
#include <iostream>
#include <thread>
void f()
{
    std::cout << "f()" << std::endl;
}
void g()
{
    std::cout << "g()" << std::endl;
}
int main()
{
    std::thread t1(f);
    std::thread t2 = std::move(t1); //因为t1是一个左值，但是这里需要一个右值
    t1=std::thread(g);
    t1.join();
    t2.join();
}
```

