#include<iostream>
using namespace std;
int total_cost(int n, int k, int* h_bid,int* s_bid, int* state, int total);

int main(){
  cout<<"starting this after a long time\n";

  int n;
  cin >> n;

  int h_bid[n], s_bid[n];
  for (int i=0; i<n; i++ )
    cin>>h_bid[i]>>s_bid[i];

  int state[n];

  int outp = total_cost(n, 0, h_bid, s_bid, state, 0);

  return 0;
}

int total_cost(int n, int k, int* h_bid,int* s_bid, int* state, int total){

  if (k == n){
    int max = 0;
    for(int i=0; i<n; i++)
      if (max < state[i]) max = state[i];

    total += max;
    return total;
  }
  else{

    state[k] = h_bid[k];
    total = total_cost(n, k+1, h_bid, s_bid, state, total);

    state[k] = s_bid[k];
    total = total_cost(n, k+1, h_bid, s_bid, state, total);

    return total;
  }


}
