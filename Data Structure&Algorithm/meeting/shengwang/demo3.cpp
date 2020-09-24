#include<iostream>
using namespace std;
class Temp{
public:
    int x,y;
    Temp(int a=0,int b=0):x(a),y(b){}
    virtual void func(){cout<<"func"<<endl;}
};
class SonTemp{
};
int main()
{
    Temp tmp; //如果没有赋初始值，那么就就出错。
    tmp=1; //居然直接可以把1付给它
    SonTemp *son=new SonTemp();

}