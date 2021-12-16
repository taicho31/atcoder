//#include <bits/stdc++.h>
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

int main(){
    
    vector<int> a(10);
    int elem = 1;
    a.at(0) = elem;
    for (int i=2;i<=10; i++){
        elem *= i;
        a.at(i-1) = elem;
    }
    int p;
    cin >> p;
    int ans = 0;

    for (int i=9;i>=0; i--){
        if (p / a.at(i) >0){
            ans += p / a.at(i);
            p %= a.at(i);
        }
        else{
            ;
        }
    }   
    cout << ans << endl;

}
