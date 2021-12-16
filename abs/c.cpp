#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n,y;
    cin >> n >> y;

    int value = y/1000-n;

    int flg = 0;
    int ans_x, ans_y;

    for (int i=0;i<=value/9;i++){
        for (int j=0;j<=value/4;j++){
            if (9*i+ 4*j == value & i+j<=n){
                flg = 1;
                ans_x = i;
                ans_y = j;
                break;
            }
        }
        if (flg){
            break;
        }
    }

    if (flg){
        cout << ans_x << " " << ans_y << " " << n - ans_x - ans_y << endl;
    }
    else{
        cout << "-1 -1 -1" << endl;
    }
}
