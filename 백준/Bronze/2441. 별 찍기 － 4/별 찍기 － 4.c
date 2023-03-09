#include<stdio.h>
int main(void)
{
    int i,j,n;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        for(j=0;j<i;j++)
            printf(" ");
        for(j=n-i;j>0;j--)
            printf("*");
        printf("\n");
    }
}