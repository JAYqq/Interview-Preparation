#include<iostream>
#include<stack>
#include<vector>
using namespace std;
int main()
{
    int n,a;
    cin>>n;
    vector<int> arr;
    stack<int> lsight,rsight;
    vector<int> score(n,1);
    for(int i=0;i<n;i++){
        cin>>a;
        arr.push_back(a);
    }
    for(int i=0;i<n;i++){
        score[i]+=lsight.size();
        while(!lsight.empty()&&arr[i]>=lsight.top()){
            lsight.pop();
        }
        lsight.push(arr[i]);
    }
    for(int i=n-1;i>=0;i--){
        score[i]+=rsight.size();
        while(!rsight.empty()&&arr[i]>=rsight.top()){
            rsight.pop();
        }
        rsight.push(arr[i]);
    }
    for(int i=0;i<score.size();i++){
        cout<<score[i]<<" ";
    }
    return 0;
}