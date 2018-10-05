# include <iostream>
# include <string>
# include ".\Person.h"

using namespace std;

int main(int argc, char const *argv[])
{
    //***************引用的方式**********
    Person per;

    per.setpid(1);
    per.setname("simon");
    per.setage(18);

    int pid = per.getpid();
    string name = per.getname();
    int age = per.getage();

    cout<<"the person named "<<name<<" ,which id is "<<pid<<" ,is at the age of "<<age<<endl;


    // //****指针调用********
    // Person *per = new Person();
    // per->setage(18);
    // per->setname("simon");
    // per->setpid(1);

    // int pid = per->getpid();
    // int age = per->getage();
    // string name = per->getname(); 

    // cout<<"the person named "<<name<<" ,which id is "<<pid<<" ,is at the age of "<<age<<endl;

    // delete per;  //指针调用后需要delete

    system("pause");
    return 0;
}