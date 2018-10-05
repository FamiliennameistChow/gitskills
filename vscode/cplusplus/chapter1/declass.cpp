# include <iostream>
# include <string>

using namespace std;
 
  // 一般定义写在.h头文件里面
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

// 成员函数实现  一般写在.cpp源文件里面
Person::Person()
{
    cout<<"构造函数"<<endl;   //构造函数可以用于某些成员变量设置初始值
}
Person::~Person()
{
    cout<<"析构函数"<<endl;
}

void Person::setpid(int pid)
{
    this->_pid = pid;  //this-> 指的是当前对象的pid
}
int Person::getpid()
{
    return this->_pid;
}


void Person::setname(string name)
{
    this->_name = name;
}
string Person::getname()
{
    return this->_name;
}


void Person::setage(int age)
{
    _age = age;
}
int Person::getage()
{
    return _age;
}




int main(int argc, char const *argv[])
{
    // //***************引用的方式**********
    // Person per;

    // per.setpid(1);
    // per.setname("simon");
    // per.setage(18);

    // int pid = per.getpid();
    // string name = per.getname();
    // int age = per.getage();

    //****指针调用********
    Person *per = new Person();
    per->setage(18);
    per->setname("simon");
    per->setpid(1);

    int pid = per->getpid();
    int age = per->getage();
    string name = per->getname(); 

    cout<<"the person named "<<name<<" ,which id is "<<pid<<" ,is at the age of "<<age<<endl;

    delete per;  //指针调用后需要delete

    system("pause");
    return 0;
}
