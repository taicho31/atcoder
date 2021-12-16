#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int N, A;
    cin >> N >> A;

    for (int i=0; i< N; i++){
        string o;
        int num;
        cin >> o >> num;
        if (o =="+"){
            A += num;
        }
        else if (o=="-"){
            A -= num;
        }
        else if (o=="*"){
            A *= num;
        }
        else{
            if (num ==0){
                cout << "error" << endl;
                break;
            }
            A /= num;
        }
        cout << i+1 << ":" << A << endl;
    }
}
