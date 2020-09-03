#include<list>
#include<mutex>
#include<iostream>
#include<algorithm>
// #include<stack>
using namespace std;
// stack<int> sf;
std::list<int> v;
std::mutex m;

void func(int n){
    std::lock_guard<std::mutex> l(m);
    v.emplace_back(n);
}

bool islistcontains(int n){
    std::lock_guard<std::mutex> l(m);
    return std::find(std::begin(v),std::end(v),n)!=std::end(v);
}

int main(){
    func(3);
    cout<<islistcontains(2)<<endl;
}
