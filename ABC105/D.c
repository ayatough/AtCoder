#define ll long long

void qsort_(int* ary, int l, int r)
{
    int sl=l, sr=r, c=0;
    if (r-l < 2) return;
    int p = ary[l] > ary[l+1] ? ary[l] : ary[l+1];
    while (l<=r)
    {
        while (l<=r && ary[l]<p)++l;
        while (l<=r && ary[r]>=p)--r;
        if (l>r) break;
        int tmp = ary[l];
        ary[l] = ary[r];
        ary[r] = tmp;
        ++l; --r; ++c;
    }
    if (c>0)
    {
        qsort_(ary, sl, l); qsort_(ary, r, sr);
    }
}

int cmp(int *a,int *b){return *a-*b;}

int main(void){
    int N, M;
    ll ans = 0;
    scanf("%d",&N); scanf("%d",&M);

    int A[N+1]; A[0]=0;
    for (int i=0, a=0; i<N && scanf("%d",&a); ++i)
        A[i+1] = (a+A[i]) % M;
    
    qsort_(A, 0, N);
    // qsort(A, N+1, 4, cmp);

    int i=0, j=1;
    while (i<N)
    {
        if (A[i] == A[i+1]) j++;
        else
        {
            ans += j * (j-1); j=1;
        }
        ++i;
    }
    ans += j * (j-1); ans /= 2;

    printf("%lld",ans);
    return 0;
}