#include<stdio.h>
int sum(int a, int b)
{
	return a + b;
}
int main() {
	int a,b;
	while (1) {
		scanf("%d %d", &a, &b);
		if (a == 0 && b == 0)
			break;
		printf("%d\n", sum(a, b));
		
	}
}