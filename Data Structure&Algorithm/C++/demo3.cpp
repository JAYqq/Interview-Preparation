#include <iostream>
class Person
{
private:
    int *data;

public:
    Person() : data(new int[1000000]) {}
    ~Person() { delete[] data; }

    // 拷贝构造函数，需要拷贝动态资源
    Person(const Person &other) : data(new int[1000000])
    {
        std::copy(other.data, other.data + 1000000, data);
    }

    // 移动构造函数，无需拷贝动态资源
    Person(Person &&other) : data(other.data)
    {
        other.data = nullptr; // 源对象的指针应该置空，以免源对象析构时影响本对象
    }

    //赋值运算符，但是这样会涉及到很大一块内存的拷贝问题，所以才需要一个
    Person &operator=(const Person &p)
    {
        delete data;
        data = new int[1000000];
        std::copy(p.data, p.data + 1000000, data);
        return *this;
    }

    //移动赋值运算符
    Person& operator=(Person &&p)
    {
        std::cout<<"Move"<<std::endl;
        data = p.data;
        p.data=nullptr;
        return *this;
    }
};

void func(Person p)
{
    // do_something
    std::cout << "Func" << std::endl;
}

int main()
{
    Person p;
    func(p);        // 调用Person的拷贝构造函数来创建实参
    func(Person()); // 调用Person的移动构造函数来创建实参
    Person p2;
    p = p2;            //调用赋值运算符重载(这里还是普通赋值运算符)
    p = std::move(p2); //调用移动赋值运算符
    return 0;
}