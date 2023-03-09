#include<stdio.h>
int main(void)
{
	int x,y,n;
	int sum = 0;

	scanf("%d %d", &x, &y);
	for (n = 1; n < x; n++)
	{
		switch (n)
		{
		case 1:
		case 3:
		case 5:
		case 7:
		case 8:
		case 10:
		case 12:
			sum = sum + 31;
		break;
		case 4:
		case 6: 
		case 9:
		case 11:
			sum = sum + 30;
			break;
		default :
			sum = sum + 28;
			break;
		}
	}
	sum = sum + y;
	switch (sum % 7)
	{
	case 1:
		printf("MON");
		break;
	case 2:
		printf("TUE");
		break;
	case 3:
		printf("WED");
		break;
	case 4:
		printf("THU");
		break;
	case 5:
		printf("FRI");
		break;
	case 6:
		printf("SAT");
		break;
	case 0:
		printf("SUN");
		break;
	}
	return 0;
}