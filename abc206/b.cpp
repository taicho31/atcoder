#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n;
    cin >> n;

    int ans;
    for (int i = 1;i<100000;i++){
        if (i*i + i >= 2*n){
            ans = i;
            break;
        }
    }

    cout << ans << endl;
}
