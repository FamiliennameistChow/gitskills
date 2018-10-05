# include <iostream>

using namespace std;

void test1()
{
    int i = 100;
    int *ip = &i;  //*解引用  &取地址  指针声明   *ip指针的值，， ip指针的地址
    cout<<i<<endl;   //对象
    cout<<*ip<<endl; //指针指向地址的对象

    cout<<&i<<endl; //取地址
    cout<<ip<<endl; //ip指针指向的地址  ip+1 指的是下一个地址

    int *p = 0;
    int *q = NULL;   //赋空值

    // const int x = 0;  //x 是常量
    // int *px = x; //使用常量给指针赋值

    int y = 0;  //y是变量
    // int *py = y; //不能使用变量对其赋值

    int arr[3]={1,2,3};
    int *pa = arr; //指针指向数组的首地址
    // int *pa = &arr[0];
   
    int *pa1 = pa + 1; //指针向后移动一位
    cout<<*pa1<<endl;

}


//void* 用法
void test3()
{
    int i = 100;
    void* p = &i;  //void *指针，可以保存任何类型对象的地址

    double d = 3.14;
    void* q = &d;
}

// void* test4()
// {
//     int i = 100;
//     return &i;   
// }

void test5(void* v)
{

}

class Person 
{

};


//比较指针与引用
void test6()
{
    int i = 100;
    int j = 200;
    int &q = i; //定义引用需要声明，声明之后不能再更换值


    int *p;  //定义指针不需要声明
    p = &i; //赋值
    p = &j;  //可以再次赋值
}

void test7()
{ 
   int i = 1, j = 2;
   int *pi = &i, *pj=&j; //pi指向i；pj指向j
   pi = pj; //将pj的地址给pi ，pi、pj都指向j
   cout<<i<<endl;
   cout<<j<<endl;
   cout<<"-------"<<endl;
   cout<<*pi<<endl;
   cout<<*pj<<endl;

   cout<<"--------------"<<endl;
   //引用的赋值
   int &ri = i;
   int &rj = j;
   ri = rj;
   cout<<i<<endl;
   cout<<j<<endl;
   cout<<"-------"<<endl;
   cout<<ri<<endl; 
   cout<<rj<<endl;

}

//二级指针是指针的地址
void test8()
{
    int i = 100;
    int *p = &i;
    int **q = &p; //二级指针是指针的地址
    cout<<p<<endl;
    cout<<*q<<endl;
}

void test9()
{
    const unsigned array_size = 5;
    int arr[array_size] = {1,2,3,4,5};
    //数组名称默认是数组的首地址
    int *p = arr; //int *p = &arr[0];
    for(int i=0;i<array_size;i++)
    {
        cout<<arr[i]<<endl;
    }

    cout<<"-------"<<endl;
    for(int i=0;i<array_size;i++)
    {
        cout<<*(p++)<<endl;
    }
    cout<<"---end----"<<endl;
    //指针算术运算
    int *q = arr;
    int *x = q + 2;
    cout<<*x<<endl;
    int *y = x-1;
    cout<<*y<<endl;
}


int main(int argc, char const *argv[])
{
    // Person *per = new Person();
    // test5(per);

    // test1();
    test9();

    system("pause");
    return 0;
}
