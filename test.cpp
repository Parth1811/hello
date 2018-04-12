#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

class game{

    int a[3][3] ;
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
    int a=1,b=0,c=-1;
    bool q,w,e,r;
    q = false;
    w = !q;
    e = !c;
    r = !a;
   cout<<q<<" "<<w<<" "<<e<<" "<<r<<endl;

}
