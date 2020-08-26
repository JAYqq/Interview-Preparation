#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
void dealArr(vector<int>& arr,int p)
{
    
}
int main()
{
    int n,a;
    vector<int> arr;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>a;
        arr.push_back(a);
    }
    int m,b;
    cin>>m;
    while(m)
    {
        cin>>b;
        int p=pow(2,b);
        dealArr(arr,p);
        m--;
    }

}