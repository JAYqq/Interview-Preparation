#include<iostream>
using namespace std;
int main()
{
    uint32_t n;
    int ans=0;
    cin>>n;
    while(n){
        if(n&1){
            ans++;
        }
        n>>=1;
    }
    cout<<ans<<endl;
    return 0;
}