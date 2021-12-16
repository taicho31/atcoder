#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int N;
    cin >> N;

    vector<int> a(N);

    for (int i=0;i<N; i++){
        cin >> a.at(i);
    }

    int sum = 0;
    for (int i=0;i<N; i++){
        sum += a.at(i);
    }

    int average = sum / N;

    for (int i=0;i<N; i++){
        if (average >= a.at(i)){
            cout << average - a.at(i) << endl;
        }
        else{
            cout << a.at(i) - average << endl;
        } 
    }    
}
