// SPOJ Problem 346. Bytelandian gold coins
#include<stdio.h>
int main()
{
	long long sum=0,n;
	while(scanf("%lld",&n)!=EOF){
		sum = n/2 + n/3 + n/4;
		if(sum>n)
			printf("\n%lld",sum);
		else
			printf("\n%lld",n);
	}
}
