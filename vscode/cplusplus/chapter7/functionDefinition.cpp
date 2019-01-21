# include <iostream>

using namespace std;

class Per
{

};

Per& getInstance(){
    Per p;
    return p;

}

int max(int a, int b){
    return a>b?a:b;
}

int main(int argc, char const *argv[])
{

    int x = max(1, 2);  //实参传递给形参 int a=1; int b=2;
    cout<<x<<endl;
    system("pause");
    return 0;
}
