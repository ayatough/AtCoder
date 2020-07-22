long r;a[26];main(n){scanf("%d ",&n);for(;n--;)a[getchar()-97]++;for(r=1;n<26;){r*=a[n++]+1;r%=1000000007;}printf("%d",r-1);}

a[26];long long x=1;main(n){for(scanf("%d ",&n);n--;)a[getchar()-97]++;for(;26-n;x=(x*a[n++])%1000000007)a[n]++;printf("%lld\n",x-1);}
