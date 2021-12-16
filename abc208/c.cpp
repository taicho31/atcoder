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
    
    int n;
    long long k;
    cin >> n >> k;

    vector<long long> a(n);
    vector<long long> ans(n);
    vector<long long> V(n);

    for (auto &elem: a){
        cin >> elem;
    }

    long long remain = k % n;
    long long avg_allocation = k / n;

    if (remain != 0){
        
        iota(V.begin(),V.end(),0); //Initializing
        sort(V.begin(),V.end(), [&](int i,int j){return a[i]<a[j];} );
    }

    for (int i=0;i<remain; i++){
        ans.at(V.at(i)) += 1;
    }

    for (int i=0;i<n;i++){
        cout << ans.at(i) + avg_allocation << endl;
    }
}
