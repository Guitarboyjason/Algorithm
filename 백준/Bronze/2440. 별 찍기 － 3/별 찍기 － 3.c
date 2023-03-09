#include<stdio.h>
int main(void)
{
    int i,n,j;
    scanf("%d",&n);
    for(j=0;j<n;j++)
    {
    for(i=n-j;i>0;i--)
        printf("*");
    printf("\n");
    }
}