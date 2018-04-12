#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

class game{
    int board_state[9][4];
    bool player1_turn;

    public:
    game(){
        for (int i = 0; i < 9; i++){
            for (int j = 0; j < 4; j++){
                board_state[i][j] = 0;
            }
        }
        player1_turn = true;
    }

    void run(){
        bool running = true;
        int intial = 1;
        while (running){
            int input1, input2;
            cin>>input1;
            if(input1 == -1){
                running = false;
                cout<<"Encountered -1 exiting the game\nHope to see you again :)\n";
                break;
            }

            else
                cin>>input2;

            if(player1_turn){
                player1_playmove(input1, input2);
            }
            else {
                player2_playmove(input1, input2);
            }
        if(intial >2)
            running = !(is_gameover());
        else
            intial++;
        }

        if(intial>2){
            if(is_gameover() == 1)
                cout<<"Player1 WINS!!!!!!\n";
            if(is_gameover()== -1)
                cout<<"Player2 WINS!!!!!!\n";
        }
    }

    void player1_playmove(int x, int y){
        if(board_state[x][y] >= 0){
            this->chain_reaction_at(1,x,y);
            player1_turn = false;
            print_board();
            cout<<"Player1 plays at ("<<x<<","<<y<<")\n\n";
            return;
        }
        else{
            cout<<"Player1 illegal move\nIts Player1's turn again\n";
            return;
        }
    }

    void player2_playmove(int x, int y){
        if(board_state[x][y] <= 0){
            this->chain_reaction_at(-1,x,y);
            player1_turn = true;
            print_board();
            cout<<"Player2 plays at ("<<x<<","<<y<<")\n\n";
            return;
        }
        else{
            cout<<"Player2 illegal move\nIts Player2's turn again\n";
            return;
        }
    }

    void chain_reaction_at(int player_sign, int x, int y){
        if(abs(board_state[x][y]) < critical_mass(x,y)-1){
            board_state[x][y] = player_sign*abs(board_state[x][y]) + player_sign;
            return ;
        }
        else if (abs(board_state[x][y]) == critical_mass(x,y)-1){
            board_state[x][y] = 0;
            int* ortho_list = get_ortho_list(x,y);
            int no_of_ortho_cells = ortho_list[0];
            int index = 1;
            for (int i = 0; i < no_of_ortho_cells; i++){
                chain_reaction_at(player_sign,ortho_list[index],ortho_list[index+1]);
                index = index + 2;
            }
        }
    }

    int critical_mass(int x, int y){
        int mass = 4;
        if(x == 0||x == 8)
            mass--;
        if(y == 0||y == 3)
            mass--;
        return mass;
    }

    int* get_ortho_list(int x, int y){
       int *list;
       int cm = critical_mass(x,y);
       list = new int[cm*2+1];
       list[0] =  cm;
       int index = 1;

       if(x != 0){
        //storing the upper cell
           list[index] = x-1;
           list[index+1] = y;
           index = index + 2;
       }
       if(y != 3){
        //storing the right cell
           list[index] = x;
           list[index+1] = y+1;
           index = index + 2;
       }
       if(x != 8){
        //storing the bottom cell
           list[index] = x + 1;
           list[index+1] = y;
           index = index + 2;
       }
       if(y != 0){
        //storing the left cell
           list[index] = x;
           list[index+1] = y-1;
           index = index + 2;
       }

       return list;
    }

    int is_gameover(){
        bool zero_flag = true;
        bool player1_flag = true;
        bool player2_flag = true;
        for (int i = 0; i < 9; i++){
            for (int j = 0; j < 4; j++){
                int board_entry = board_state[i][j];
                if(board_entry > 0)
                    player2_flag = false;
                if(board_entry < 0)
                    player1_flag = false;
                if(board_entry!= 0)
                    zero_flag = false;
            }
        }

        if(zero_flag)
            return false;
        else if(player1_flag)
            return 1;
        else if (player2_flag)
            return -1;
        else
            return false;
    }

    void print_board(){
        cout<<"    0  1  2  3\n";
        for (int i = 0; i < 9; i++){
        cout<<i<<"   ";
            for (int j = 0; j < 4; j++){
                cout<<board_state[i][j] <<"  ";
            }
        cout<<endl;
        }
    }

};

int main(){

    game g;
    g.print_board();
    cout<<endl;
    g.run();

    return 0;
}
