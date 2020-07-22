#include <stdio.h>


int main(void)
{
    int N;
    long double ans = 0;
    scanf("%d", &N);
    if (N%2 == 0) ans = 0.5;
    else
    {
        ans = 0.5 * (N+1) / N;
    }
    printf("%Lf\n", ans);
}