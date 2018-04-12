#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

static const int ROWS = 9;  //number of rows of board
static const int COLUMNS = 4; //number of coloumns of board

class game{
    int **board_state;
    bool player1_turn; //if true its player1's turn or else player2's

    public:
    game(){
        board_state = new int*[ROWS];
        for (int i = 0; i < ROWS; i++)
            //allocating the space in heap memory
            board_state[i] = new int[COLUMNS];

        for (int i = 0; i < ROWS; i++){
            for (int j = 0; j < COLUMNS; j++){
                //initalizing all cells to zero
                board_state[i][j] = 0;
            }
        }

        //starting the game with player1 playing first
        player1_turn = true;
    }

    void run(){
        /*
            This is the run function. It takes the input from the user
            and passes it on to player1_playmove/player2_playmove
            depending on who's move it is and exits the game it -1 is
            encoutered. Also exit if the player wins
        */
        bool running = true;
        int intial = 1; //avoids the intial false win of player1
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
                running = !(is_gameover()); //checks if any of player is winning after playing atleast 1 move
            else
                intial++;
        }

        if(intial>2){
            if(is_gameover() == 1)  //if is_gameover() returns 1 player 1 wins
                cout<<"Player1 WINS!!!!!!\n";
            if(is_gameover()== -1)  //if is_gameover() returns -1 player 2 wins
                cout<<"Player2 WINS!!!!!!\n";
        }
    }

    void player1_playmove(int x, int y){
        /*
            This function makes the move for player1
            Also checks whether the move is leagal  or not
        */
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
        /*
            This function makes the move for player2
            Also checks whether the move is leagal  or not
        */
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
        /*
            This is a recurrsive function
            it takes the sign of player i.e. 1 for player1
            and -1 for player2 , and adds 1 to cell if its value
            is less than critical value or explodes the cell if it becomes
            equal to critical value
        */
        if(abs(board_state[x][y]) < critical_mass(x,y)-1){
            board_state[x][y] = player_sign*abs(board_state[x][y]) + player_sign;
            return ;
        }
        else if (abs(board_state[x][y]) == critical_mass(x,y)-1){
            board_state[x][y] = 0;  //empties the current cell after explosion
            int* ortho_list = get_ortho_list(x,y); //recieves a list of co-ordinates of orthogonal cells
            int no_of_ortho_cells = critical_mass(x,y); //sets the no of orthognal cells
            int index = 0;
            for (int i = 0; i < no_of_ortho_cells; i++){
                //starts a chain reaction at every orthogonal cell
                chain_reaction_at(player_sign,ortho_list[index],ortho_list[index+1]);
                index = index + 2;
            }
        }
    }

    int critical_mass(int x, int y){
        /*
            This functions calculates the critical mass of the cell
            i.e. the number of adajacent orthogonal cells
        */
        int mass = 4;
        if(x == 0||x == ROWS-1)
            mass--;
        if(y == 0||y == COLUMNS-1)
            mass--;
        return mass;
    }

    int* get_ortho_list(int x, int y){
        /*
            This function returns a list of cordinates of orthogonal cells
            in the format [x1,y1,x2,y2....]
            number of elements in the list = 2*critical_mass
        */
       int *list;
       list = new int[critical_mass(x,y)*2+1];
       int index = 0;

       if(x != 0){
        //storing the upper cell
           list[index] = x-1;
           list[index+1] = y;
           index = index + 2;
       }
       if(y != COLUMNS-1){
        //storing the right cell
           list[index] = x;
           list[index+1] = y+1;
           index = index + 2;
       }
       if(x != ROWS-1){
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
        /*
            This function check whether either of the player has
            won the game i.e. it essentially checks if the game is over
            or not and returns false if game is not over , 1 if player 1 wins,
            -1 if player 2 wins
        */
        bool zero_flag = true;
        bool player1_flag = true;
        bool player2_flag = true;
        for (int i = 0; i < ROWS; i++){
            for (int j = 0; j < COLUMNS; j++){
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
        /*
            This functions prints the board
        */
        cout<<"    0  1  2  3\n";
        for (int i = 0; i < ROWS; i++){
        cout<<i<<"   ";
            for (int j = 0; j < COLUMNS; j++){
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
