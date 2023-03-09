#include<stdio.h>
int sum(int a, int b)
{
	return a + b;
}
int main() {
	int T, i,a,b;
	scanf("%d", &T);
	for (i = 0; i < T; i++) {
		scanf("%d %d", &a, &b);
		printf("%d\n", sum(a, b));
	}
}