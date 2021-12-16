#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> t_vec(n+1);
    vector<int> x_vec(n+1);
    vector<int> y_vec(n+1);

    t_vec.at(0) = 0;
    x_vec.at(0) = 0;
    y_vec.at(0) = 0;

    for (int i=1; i<n+1; i++){
        int t, x, y;
        cin >> t >> x >> y;
        t_vec.at(i) = t;
        x_vec.at(i) = x;
        y_vec.at(i) = y;
    }

    int flg =0;
    for (int i=1; i<n+1; i++){
        int dt = t_vec.at(i) - t_vec.at(i-1);
        int dx = abs(x_vec.at(i) - x_vec.at(i-1));
        int dy = abs(y_vec.at(i) - y_vec.at(i-1));

        if (dx+dy > dt || (dt-dx-dy) %2 != 0){
            flg = 1;
            break;
        }
    }

    if (flg==0){
        cout << "Yes" << endl;
    }
    else{
        cout << "No" << endl;
    }
}
