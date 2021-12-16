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
    int n ,x;
    int ans = 0;

    cin >> n >> x;

    for (int i =1;i<=n;i++){
        int item;
        cin >> item;
        if (i % 2 ==0){
            ans += (item - 1);
        }
        else{
            ans += item;
        }
    }

    if (x >= ans){
        cout << "Yes" << endl;
    }
    else{
        cout << "No" << endl;
    }

}
