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
    int a, b, c;
    cin >> a >> b >> c;

    int ans1 = a + b;
    int ans2 = a + c;
    int ans3 = b + c;

    int maxi = max(ans1, ans2);
    maxi = max(maxi, ans3);

    cout << maxi << endl;
}
