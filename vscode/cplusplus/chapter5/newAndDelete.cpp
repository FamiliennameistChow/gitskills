# include <iostream>
# include <String>

using namespace std;
//new 和delete
class Person 
{
    public:
    int pid;
    int getpid();

};

void test1()
{
    int i;
    int *pi = new int;
    //string s = "Hello World!";
    string *s = new string("Hello World!");
    Person *per = new Person();
    per -> pid = 100;
    per -> getpid();

    delete s;
    s = NULL;  //删除指针后需要重置指针
}

void test2()
{
    const int *p = new int(1024);
    delete p;
}

int main(int argc, char const *argv[])
{
    
    system("pause");
    return 0;
}
