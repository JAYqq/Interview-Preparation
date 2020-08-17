#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int n,k;
    vector<int> arr;
    cin>>n>>k;
    for(int i=0;i<n;i++)
    {
        int temp;
        cin>>temp;
        arr.push_back(temp);
    }
    int left=0;
    int right=n-1;
    while(left<right)
    {
        if(arr[left]+arr[right]==k){
            cout<<arr[left]<<" "<<arr[right]<<endl;
            left+=1;
            right-=1;
        }
        if(arr[left]+arr[right]<k)
            left+=1;
        if(arr[left]+arr[right]>k)
            right-=1;
    }
}