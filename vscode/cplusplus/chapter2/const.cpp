# include <iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    // const int age = 20;//the age can not be modified
    int age = 20;
    cout<<age<<endl;
    age =21;
    cout<<age<<endl;

    //声明常量
    const int size = 4*6;
    int arr[size];

    system("pause");
    // return 0;
}
