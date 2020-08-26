#include<iostream>
#include<queue>
using namespace std;
std::queue<int> qu;
int gcd(int a, int b)
{
	if (b == 0)
		return a;
	return
		gcd(b, a%b);
}