#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

static const int row = 3;


class game{

    int a[global::row][3] ;
    public:
    game(){
     for (int i=0 ;i<3;i++){
        for (int j = 0; j< 3; j++){
        a[i][j]=10;}
    }
    }
    void print_a(){
      for (int i=0 ;i<3;i++){
        for (int j = 0; j< 3; j++){
        cout<<a[i][j]<<" ";}
    cout<<endl;
    }
    }
};

int main(){
    game g;
    g.print_a()
}
