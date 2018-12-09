#include<bits/stdc++.h>
#include<time.h>
using namespace std;
struct node{
	long long int day;
	long long int val;
}peo[1000000];
bool cmp(node a,node b)
{
	if(a.val==b.val)return a.day<b.day;
	return a.val>b.val;
}
bool bj[1000000];
int main()
{



	freopen("homework.in","r",stdin);
	freopen("homework.out","w",stdout);
  

 

	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
		cin>>peo[i].day>>peo[i].val;
	sort(peo+1,peo+n+1,cmp);
	//for(int i=0;i<n;i++)
		//cout<<peo[i].day<<" "<<peo[i].val<<endl;
	 int ans=0;
	int l=0;
	bool f=false;
	int tmp=0;
	for(int i=1;i<=n;i++)
	{
		//先循环1到n天
		//然后找最接近的 
	
		if(peo[i].day<=l) continue;
		f=true;
		tmp=peo[i].day;
		while(bj[tmp]==1&&tmp!=0)
		tmp--;
			if(tmp!=0) f=0,bj[tmp]=1,ans+=peo[i].val; 
		if(f)
        l=peo[i].day;
	}
	cout<<ans<<endl;
	 

}
