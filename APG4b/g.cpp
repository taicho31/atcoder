//#include <bits/stdc++.h>
#include <stdio.h>
#include <iostream>
#include <cfenv>
#include <cmath>
#include <vector>

using namespace std;
 
int main() {
  vector<int> data(5);
  for (int i = 0; i < 5; i++) {
    cin >> data.at(i);
  }
 
  int flg = 0;
  // dataの中で隣り合う等しい要素が存在するなら"YES"を出力し、そうでなければ"NO"を出力する
  // ここにプログラムを追
  for (int i = 0; i < 4; i++) {
    if (data.at(i) == data.at(i+1)){
        flg = 1;
    }
  }
  
  if(flg){
      cout << "YES" << endl;
  }
  else{
      cout << "NO" << endl;
  }
}
