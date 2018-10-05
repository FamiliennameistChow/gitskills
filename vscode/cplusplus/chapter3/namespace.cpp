# include <iostream>
# include <string>
# include <vector>

using namespace std; //系统命名空间

namespace MyNS1
{
    int a;
    int b;
    void f1();
    class Person{
        public:
        void f2();
    };


}

void MyNS1::Person::f2()  //定义命名空间下类中的函数
{
    cout<<"f2"<<endl;
}

void MyNS1::f1()  //定义命名空间下的函数
{
    cout<<MyNS1::a+MyNS1::b<<endl;
}


int main(int argc, char const *argv[])
{
    //调用命名空间的变量
    MyNS1::a = 100;
    MyNS1::b = 20;

    //调用命名空间的函数
    MyNS1::f1();

    //调用命名空间的类
    MyNS1::Person per;
    per.f2();

    system("pause");
    return 0;
}
