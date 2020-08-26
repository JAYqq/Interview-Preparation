#include<iostream>
#include<memory>
// using namespace std;
class B;  //这里必须要先声明
class A
{
private:
    std::shared_ptr<B> m_test_B;
public:
    A(){
        std::cout<<"A"<<std::endl;
    }
    ~A(){
        std::cout<<"~A"<<std::endl;
    }
    void refer(std::shared_ptr<B> refer_B){
        m_test_B=refer_B;
    }
};
class B
{
private:
    std::shared_ptr<A> my_test_A;
public:
    B(){
        std::cout<<"B"<<std::endl;
    }
    void refer(std::shared_ptr<A> refer_A){
        my_test_A=refer_A;
    }
    ~B(){
        std::cout<<"~B"<<std::endl;
    }
};
int main()
{
    std::shared_ptr<A> mA=std::make_shared<A>();
    std::shared_ptr<B> mB=std::make_shared<B>();
    mA->refer(mB);
    mB->refer(mA);
    return 0;
}