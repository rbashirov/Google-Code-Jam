#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int tr;
  cin >> tr;
  for(int qr = 1;qr<=tr;qr++) {
    cout << "Case #" << qr << ": ";
    int n;
    cin >> n;
    vector<vector<int>> a(n, vector<int>(n));
        for(int i = 0; i < n; i++) {
          for(int j = 0; j < n; j++) {
            cin >> a[i][j];
            --a[i][j];
          }
        }
    int trace = 0;
    for (int i = 0; i < n; i++) {
      trace += a[i][i] + 1;
    }
    vector<int> check(n);
    int rows = 0;
    for (int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if(check[a[i][j]] == i+1) {
                ++rows;
                break;
            }
            check[a[i][j]] = i+1;        
        }
    }
    int cols = 0;
    for (int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if(check[a[j][i]] == n+i+2) {
                ++cols;
                break;
            }
            check[a[i][j]] = n+i+2;        
        }
    }  
    cout << trace << " " << rows << " " << cols << '\n';  
  }

    return 0;
}
