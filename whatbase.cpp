#include<bits/stdc++.h>
using namespace std;
int emmm(const string &a,int b)
{
	return (a[0] - '0') * b * b +(a[1] - '0') * b +(a[2] - '0');
}
const int maxn = 10005;
int main()
{
	freopen("whatbase.in","r",stdin);
	freopen("whatbase.out","w",stdout);
	//cout<<emmm(maxn,2);	
	int _;cin>>_;
	for(int i=1;i<=_;i++)
	{
		string tmpx,tmpy;cin>>tmpx>>tmpy;
		int tx=10,ty=10;
		while(tx<=maxn&&ty<=maxn)
		{
			int hx=emmm(tmpx,tx);
			int hy=emmm(tmpy,ty);
			if(hx<hy)tx++;
			else if(hy<hx)ty++;
			else
			{
				cout<<tx<<" "<<ty<<endl;
				break;
			} 
		} 
	}
}
