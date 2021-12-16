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
#include <numeric>  
#include <climits>
using namespace std;

int main(){
    int a, b;
    cin >> a >> b;

    int ans = b - a + 1;

    cout << max(ans, 0) << endl;
}
