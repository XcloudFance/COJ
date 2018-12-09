#include<bits/stdc++.h>
using namespace std;
struct a
{
	int st;
	int end;
	int t;
}b[10001];
int n,m,num=0;
int road[10001]={0};
bool cmp(a x,a y)
{
	return x.end<y.end;
}
int main()
{
freopen("trans.in","r",stdin);
freopen("trans.out","w",stdout);
	cin>>m;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		cin>>b[i].st >>b[i].end >>b[i].t ;
	}
	sort(b+1,b+n+1,cmp);
	for(int i=1;i<=n;i++)
	{
		int sum=0;
		for(int j=b[i].st ;j<=b[i].end ;j++)
		{
			if(road[j]==1) sum++;	
		}
		
	  	if(sum>=b[i].t) continue;
		for(int j=b[i].end ;j>=b[i].st;j--)
		{
			if(!road[j])
			{
				road[j]=1;
				sum++;
				num++;
				if(sum==b[i].t)
				break;
			}
			
		}
	}
	cout<<num;
	
}
