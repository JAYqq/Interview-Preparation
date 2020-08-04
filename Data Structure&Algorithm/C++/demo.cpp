#include<iostream>
using namespace std;
class IntNum{
    private:
        int* inptr;
    public:
        IntNum(int x=0):inptr(new int(x)){cout<<"构造函数"<<endl;}
        IntNum(const IntNum& n):inptr(new int(*n.inptr)){
            cout<<"复制构造函数"<<endl;
        }
        ~IntNum(){
            delete inptr;
            cout<<"析构函数"<<endl;
        }
        int getNum(){return *inptr;}
};
IntNum getInt(){
    IntNum nu;
    return nu;
}
int main()
{
    int&& n=9;
    // int& r=9;
    int &&rr=8;
    int &&rb=std::move(rr);
    cout<<getInt().getNum()<<endl;
    return 0;
}