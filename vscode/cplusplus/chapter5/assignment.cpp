# include <iostream>

using namespace std;

void test1()
{
    //赋值运算的左值必须是非const的左值
    int i,j;
    const int ci = 1; //声明，不是赋值
    // 1024 = i； //字面量是左值
    // i+j = 100; //表达式是左值
    // ci = 200; //常量不能修改
}

void test2()
{
    //赋值操作返回右值，多个相同的类型的变量可以同时被赋值
    int a = 1, x, y;
    x = y = a;
}

void test3()
{
    //注意在条件式中使用比较和赋值
    int a = 200;
    //a 被赋值为200，the result is true
    if(a=200)
    {

    }

    //judge whether a equals 100
    if(a==100)
    {

    }
}

void test4()
{
    //pointer's assignment
    int a = 100, b = 200;
    int *pa = &a, *pb=&b;


    pa = pb; //pa指向Pb指向的地址
    (*pa)++;
    (*pb)++;
    cout<<a<<endl;
    cout<<b<<endl;
}

int main(int argc, char const *argv[])
{
    test4();
    system("pause");
    return 0;
}
