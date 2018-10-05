# include <iostream>
using namespace std;

enum direction
{
    UP,
    DOWN,
    LEFT=10,
    RIGHT
};
void change(direction d)
{
    switch (d)
    {
        case UP:
        cout<<"up"<<endl;
        break;
        case DOWN:
        cout<<"down"<<endl;
        break;
        case LEFT:
        cout<<"left"<<endl;
        break;
        case RIGHT:
        cout<<"right"<<endl;
        break;
    }
}


int main(int argc, char const *argv[])
{
    //默认枚举值是从0开始
    cout<<UP<<endl;
    cout<<DOWN<<endl;
    cout<<LEFT<<endl;
    cout<<RIGHT<<endl;

    change(DOWN);


    system("pause");
    
    return 0;
}
