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
    // test(NULL); //报错！
  	test(); //ok！
    return 0;
}