// SPOJ Problem 6471. Printing some primes

#include<stdio.h>
#include<math.h>
int main()
{
	int count=0,first=1;
	long long i,j,val=100000000;
	int prime =1;

	for(i=2;i<=val;i++)
	{
		prime = 1;
		for(j=2;j<sqrt(i);j++)
		{
			if(i%j==0)
			{
				prime = 0;
				break;
			}
		}//end inner for

		if(prime)
		{
			if(first){
				printf("%lld\n",i);
				first = 0;
			}

			count += 1;
			if(count==101)
			{
				printf("%lld\n",i);
				count = 0;
			}
		}// end if	
	}//end outer for
}
