# include <iostream>
using namespace std;
int out;
int main(int argc, char const *argv[])
{
    //变量
    int age = 20; 
    //变量的命名
    string custumer_name;
    string custumerName;
    string _name;
    int _age;
    //init
    int pid = 1;//拷贝初始化
   // int pid(2); //直接初始化
    //初始化规则
    int in;
    extern int out;
    cout<<out<<endl;
    cout<<in<<endl;
    //变量的定义与声明
    int x = 100;//定义
    extern int y;//声明


    system("pause");
    return 0;
}
