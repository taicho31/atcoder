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
#include <numeric>  
#include <climits>
using namespace std;

int main(){
    int N; cin >> N;
    vector<int> C(N);
    for(int i =0; i<N; i++) cin >> C[i];
    sort(C.begin(), C.end());
    long long ans = 1;
    for(int i=0; i<N; i++) ans = ans * max(0, C[i] - i) % 1000000007;
    cout << ans << endl;
}
