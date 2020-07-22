#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define REP(n) for (int i=0; i<(n); i++)

#define Input(a) char a[256]; scanf("%255[^\n]%*c", &a)

#define Int(a) int a; scanf("%d%*c", &a)
#define Int2(a,b) int a,b;scanf("%d%d%*c",&a,&b)

#define IntList(a, n) int a[(n)]; REP((n)) {scanf("%d%*c", &a[i]);}
#define PrintIntList(a,n) REP((n)-1) {printf("%d ", a[i]);} printf("%d\n", a[(n)-1])



int main(void)
{
    // Input(buffer);
    // Input(buffer2);
    // printf("%s\n", buffer);
    // printf("%s\n", buffer2);

    Int(d);
    printf("%d\n", d);
    // Int(d2);
    // printf("%d\n", d2);

    IntList(as, d);
    PrintIntList(as, d);

    // Int2(p, q);
    // printf("%d %d\n", p, q);

    return 0;
}