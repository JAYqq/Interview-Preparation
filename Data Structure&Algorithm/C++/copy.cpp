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
        std::cout<<"普通赋值运算符"<<std::endl;
        if(&s==this)
        {
            return *this;
        }
        delete[] str;
        str=new char[strlen(s.str)+1];
        strcpy(str,s.str);
        return *this;
    }

    MyString& operator=(MyString&& mstr) noexcept
    {
        std::cout<<"移动赋值运算符"<<std::endl;
        str=mstr.str;
        mstr.str=nullptr;
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
    MyString ystr(MyString xstr);
    // ystr="World";
    // mstr=ystr;
    // mstr=std::move(ystr);
    mstr.get_str();
    return 0;
}
