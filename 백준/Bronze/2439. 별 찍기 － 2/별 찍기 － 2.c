#include<stdio.h>
int main(void)
{
    int i,j,k,n;
    scanf("%d",&n);
    for(k=1;k<=n;k++)
    {
        for(i=n;i>k;i--)
            printf(" ");
        for(j=1;j<=k;j++)
            printf("*");
        printf("\n");
    }
}