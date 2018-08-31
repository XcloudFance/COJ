#include<cstdio>
#include<iostream>
using namespace std;
int n;
int fbnq(int h){
	switch(h)
	{
		case 0 :return 0;
		case 1 :return 1;
		default: return(fbnq(h-1)+fbnq(h-2));
	}
}
int main()
{
	freopen("fbi.in","r",stdin);
freopen("fbi.out","w",stdout);

	cin>>n;
	cout<<fbnq(n-1);
	return 0;
}
