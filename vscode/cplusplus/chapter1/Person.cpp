# include <iostream>
# include <string>
# include ".\Person.h"


// 成员函数实现  一般写在.cpp源文件里面
// 此处用于实现Person类的成员函数
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
