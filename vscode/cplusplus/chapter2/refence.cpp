# include <iostream>
using namespace std;
//copy
void swap(int a, int b)
{
    int temp;
    temp = a;
    a = b;
    b = temp;
    cout<<a<<","<<b<<endl;
}

//refence
void swap2(int &a, int &b)
{
    int temp;
    temp = a;
    a = b;
    b = temp;
    cout<<a<<","<<b<<endl;
}

int main(int argc, char const *argv[])
{
    // int a = 100;
    // int &r = a; //引用
    int a = 3, b= 5;
    // swap(a, b);
    swap2(a,b);
    cout<<a<<","<<b<<endl;


    system("pause");
    return 0;
}
