#include <bits/stdc++.h>

#define FOR(i,n) for(int (i) = 0; (i) < (n); (i)++)
using namespace std;

int main()
{
    int N, W, C;
    cin >> N >> W >> C;
    vector<vector<int>> B(N, vector<int>(3));
    FOR(i,N) {
        int w, v, c;
        cin >> w >> v >> c;
        B[i][0] = c;
        B[i][1] = w;
        B[i][2] = v;
    }
    return 0;
}
