#include<iostream>
#include<vector>
#include<map>
using namespace std;
vector<int> arr;
vector<int> res;
map<int,bool> mm;
void dfs(int k,int ans)
{
    if(k==0&&!mm[ans]){
        mm[ans]=true;
        res.push_back(ans);
        return;
    }
    for(int i=0;i<arr.size();i++){
        dfs(k-1,ans+arr[i]);
    }
}
int main(){
    int a,b,k;
    cin>>a>>b>>k;
    arr.push_back(a);
    arr.push_back(b);
    dfs(k,0);
}