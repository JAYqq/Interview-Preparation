#include<iostream>
class Temp{
    public:
        void operator=(const Temp &temp){//赋值
            num=temp.num;
            str=temp.str;
            // return *this;
        }
        void show();
        Temp(const Temp&);
        Temp(){};
        Temp(int num,std::string str);
    private:
        int num;
        std::string str;
};
Temp::Temp(int cnum,std::string cstr)
{
    num=cnum;
    str=cstr;
}
void Temp::show()
{
    std::cout<<num<<"  "<<str<<std::endl;
}
int main()
{
    Temp tmp1(12,"first");
    tmp1.show();
    Temp tmp2(24,"second");
    tmp1=tmp2;
    tmp1.show();
    return 0;
}
//这样tmp1就被tmp2覆盖掉了