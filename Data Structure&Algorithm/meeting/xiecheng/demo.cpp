#include<bits/stdc++.h>
/*
链接：https://www.nowcoder.com/questionTerminal/1fe6c3136d2a45fa8ef555b459b6dd26
来源：牛客网

小A参加了一个n人的活动，每个人都有一个唯一编号i(i>=0 & i<n)，其中m对相互认识，在活动中两个人可以通过互相都认识的一个人介绍认识。现在问活动结束后，小A最多会认识多少人？


输入描述:
第一行聚会的人数：n（n>=3 & n<10000）；
第二行小A的编号: ai（ai >= 0 & ai < n)；
第三互相认识的数目: m（m>=1 & m
< n(n-1)/2）；
第4到m+3行为互相认识的对，以','分割的编号。


输出描述:
输出小A最多会新认识的多少人？
*/
using namespace std;
const int maxn = 1e5 + 8;
vector<int> G[maxn];
int res = 0;

//深度遍历 找到一个集合的人
void dfs(int ai, vector<bool> &v) {
	for (int i = 0; i < G[ai].size(); ++i) {
		if (!v[G[ai][i]]) {
			v[G[ai][i]] = true;
			res++;
			dfs(G[ai][i], v);
		}	

	}
	return;
}


int main() {
	int n, ai, m;
	cin >> n >> ai >> m;
    //构建邻接表
	while (m--) {
		int p1, p2;
		char chs;
		cin >> p1 >> chs >> p2;
		G[p1].push_back(p2);
		G[p2].push_back(p1);
		
	}
	vector<bool> visited(n, false);
    
    //除去本来就认识的人和自己
	int already = G[ai].size() + 1;
	dfs(ai,visited);

	cout << res - already << endl;

	return 0;
}