#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, M;
    cin >> N >> M;
    vector<int> A(M), B(M);
    for (int i =0;i<M; i++){
        cin >> A.at(i) >> B.at(i);
    }

    vector<vector<char>> result(N, vector<char>(N));

    for (int i=0;i<N; i++){
        for (int j=0;j<N;j++){
            result.at(i).at(j) = '-';
        }
    }

    for (int i =0;i<M;i++){
        int a = A.at(i);
        int b = B.at(i);

        result.at(a-1).at(b-1) = 'o';
        result.at(b-1).at(a-1) = 'x';
    }

    for (int i =0;i<N;i++){
        for (int j =0; j<N; j++){
        cout << result.at(i).at(j);
        if (j== N-1){
            cout << endl;
        }
        else {
            cout << " ";
        }
    }
    }

}
