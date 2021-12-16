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
    int t;
    double l_, r_;
    cin >> n;

    vector <double> l(n);
    vector <double> r(n);

    for (int i=0;i<n;i++){
        cin >> t >> l_ >> r_;
    
        if (t==2){
            l.at(i) = l_;
            r.at(i) = r_-0.5;
        }
        else if (t==3){
            l.at(i) = l_+0.5;
            r.at(i) = r_;
        }
        else if (t==4){
            l.at(i) = l_+0.5;
            r.at(i) = r_-0.5;
        }
        else {
            l.at(i) = l_;
            r.at(i) = r_;
        }
    }

    int ans = 0;

    for (int i=0;i<n;i++){
        for (int j=i+1;j<n;j++){
            if (max(l.at(i), l.at(j)) <= min(r.at(i), r.at(j))){
                ans ++;
            }
        }
    }

    cout << ans << endl;
}
