# include <iostream>

using namespace std;
int main(int argc, char const *argv[])
{
    int i = 5; //0101
    int j = 9; //1001
    int a = 2; //0010

    int b = 8; //1000
    int k = 0;

    k = i&j; //0001
    cout<<k<<endl;

    k = i|j;  //1101
    cout<<k<<endl;

    k = ~i; //1010 ,换成补码输出 0101 + 1 = 0110
    cout<<k<<endl;

    k = a<<2; //1000 按位右移
    cout<<k<<endl;

    k = a>>2; // 按位左移
    cout<<k<<endl;


    system("pause");
    return 0;
}
