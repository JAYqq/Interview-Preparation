#include <iostream>
#include <algorithm>
using namespace std;
int arr[100002];
bool cmp(int i, int j) { return (i > j); } //降序排列
int main()
{
    int n;
    cin >> n;
    int i;
    for (i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    if(n%2==1){
        arr[i]=0;
        n++;
    }
    sort(arr, arr + n, cmp);
    int ans=0;
    for (int i = 0; i < n-1; i+=2)
    {
        ans+=arr[i]-arr[i+1];
    }
    cout<<ans<<endl;
    return 0;
}