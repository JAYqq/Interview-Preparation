#include<iostream>
#include<vector>
using namespace std;
template <typename T>
int compare(const T &v1,const T &v2)
{
    if(v1>v2) return 1;
    else return 0;
}
int main()
{
    int result1=compare(1,2);
    vector<int> vec1{1,2,3},vec2{4,5,6};
    cout<<result1<<" "<<compare(vec1,vec2)<<endl;
    return 0;
}