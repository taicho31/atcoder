#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int ans = 0;
    int N;
    cin >> N;

    for (int i=0; i < N; i++){
        int tmp;
        cin >> tmp;
        if (tmp > 10){
            ans += (tmp-10);
        }
    }
    cout << ans << endl;
}
