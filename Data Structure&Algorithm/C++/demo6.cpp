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
    B(){cout<<"B"<<endl;}
};
int main()
{
    A* a=A::get_A();
    B a;
    // delete a;
    A::delete_A(a);
}