# include <iostream>

using namespace std;

class Person 
{

};

void statement()
{
    //声明数组,int类型
    const int size = 10;
    int a[size];

    //赋值
    for(int i=0;i<size;i++)
    {
        a[i]=i+1;
    }

    cout<<a[0]<<endl;

    //声明数组，类
    const int size1 = 2;
    Person pers[size1];
    Person p1;
    Person p2;
    pers[0] = p1;
    pers[1] = p2;
}

void init()
{
    //init the array
    int arr[] = {1,2,3,4,5}; //初始化赋值

    //数组不能直接复制或者赋值


}

int main(int argc, char const *argv[])
{
    statement();

    system("pause");
    return 0;
}
