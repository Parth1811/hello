#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

int main(){

  int n, no_of_three = 0, no_of_two = 0;
  vector<int> out;
  cin >> n;

  if (n == 1){
    cout << "{1}" <<endl;
    return 0;
  }

  switch (n % 3) {
    case 0:
            no_of_three = n / 3;
            break;
    case 1:
            no_of_two = 2;
            no_of_three = (n - 4) / 3;
            break;
    case 2:
            no_of_two = 1;
            no_of_three = (n -2) / 3;
            break;
  }

  for (int i = 0; i < no_of_three; i++) {
    out.push_back(3);
  }
  for (int i = 0; i < no_of_two; i++) {
    out.push_back(2);
  }


  cout << '{';
  for (int i = 0; i < out.size() - 1; i++) {
    cout << out[i] << ',';
  }
  cout << out[out.size() - 1] << '}' << endl;;

  return 0;
}
