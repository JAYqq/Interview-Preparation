#include<iostream>
using namespace std;
int main()
{
    int n,m;
    cin>>n>>m;
    int temp=n/(m*2);
    int rem=n%(m*2);
    int ans=0;
    if(rem>0){
        for(int i=n;i>n-m;i--)
           ans+=i;
    }
    ans=temp*m*m-ans;
    cout<<ans<<endl;
}
// -1 -2 -3 4 5 6 -7 -8 -9