#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <sstream>
#include <iomanip>
#include <set>
#include <cmath>
#include <bitset>
#include <queue>
#include <climits>
using namespace std;


struct UnionFind {
    vector<int> par, si;

    void init(int n){
        par.resize(n,-1);
        si.resize(n,1);
    }


    int root(int x){
        if (par[x] == -1) return x;
        return par[x] = root(par[x]);
    }

    void unite(int x, int y){
        int rx = root(x);
        int ry = root(y);
        if (rx == ry) return ;
        si[rx] += si[ry];
        par[rx] = ry;
    }

    bool same(int x, int y){
        int rx = root(x);
        int ry = root(y);
        return rx == ry;
    }

};

int main(){
    int N;
    cin >> N;

    vector<int> A(N);
    for (int i=0; i<N; i++){cin >> A.at(i);}

    UnionFind tree;
    tree.init(200005);

    for(int i=0; i<N; i++){
        tree.unite(A.at(i),A.at(N-i-1));
    }

    int ans = 0;

    for (int i=0; i<200005; i++) {
        if (tree.root(i)==-1) continue;
        ans += tree.si[i]- 1;
        }

    cout << ans << endl;
}
