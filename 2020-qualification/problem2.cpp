#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int tr;
  cin >> tr;
  int tmp = 0;
  for(int qr = 1;qr<=tr;qr++) {
    cout << "Case #" << qr << ": ";
    string s;
    cin >> s;
    for (char& c:s) {
	  int diff = int(c) - int('0');
	  while(tmp<diff) {
		cout << '(';
	    ++tmp;
	  }
	  while(tmp>diff) {
		cout << ')';
	    --tmp;
	  }
      cout << c;
    }
    while (tmp > 0){
      cout << ')';
      --tmp;
    } 
  cout <<"\n";
  }
  return 0;
}
