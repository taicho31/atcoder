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
    int a, b, c, d;
    cin >> a >> b >> c >> d;

    int right = c * d - b;

    if (right <=0){
        cout << -1 << endl;
    }
    else{
        float thresh = double(a) / right;
        int ans = ceil(thresh);
        cout << ans << endl;
    }
}
