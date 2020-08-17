//并查集基本应用，最后别忘了减掉本身
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int n,ix,m;
vector<int>f;
int find(int x){
    return x==f[x]?x:f[x]=find(f[x]);
}
int main(void){
    cin>>n>>ix>>m;
    f=vector<int>(n);
    for(int i=0;i<n;i++)f[i]=i;
    int ans=0,b=0;
    while(m--){
        int one,two;
        scanf("%d,%d",&one,&two);
        if(one==ix||two==ix)b++;
        int fx=find(one),fy=find(two);
        if(fx!=fy)f[fx]=fy;
    }
    for(int i=0;i<n;i++){
        if(find(ix)==find(i))ans++;
    }
    cout<<ans-b-1<<endl;
    return 0;
}