# include <iostream>
# include <string>
using namespace std;

 // 类的定义写在.h头文件里面
 // 此处定义类Person
class Person
{
    //私有的变量声明
private:
    int _pid;
    string _name;
    int _age;
    //公共的方法声明
public:
    Person();  //构造函数   每次创建类的新对象时执行
    ~Person();  //析构函数  每次删除所创建的对象时执行

    void setpid(int pid);
    int getpid();

    void setname(string name);
    string getname();

    void setage(int age);
    int getage();
};
