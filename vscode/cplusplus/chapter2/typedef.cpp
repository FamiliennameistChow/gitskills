# include <iostream>
# include <string>

using namespace std;
//结构体
typedef struct Mystruct
{
    int x;
    int y;
} point;

//类
typedef class Person 
{
public:
    int pid;
} customer;

int main(int argc, char const *argv[])
{
    //内置类型
    //结构体
    typedef int myint;
    myint age;
    point p;
    p.x=1;
    p.y=2;
    cout<<p.x<<","<<p.y<<endl;

    customer c1;
    c1.pid=1;
    cout<<c1.pid<<endl;

    system("pause");

    return 0;
}
