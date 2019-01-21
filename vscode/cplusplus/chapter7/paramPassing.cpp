# include <iostream>

using namespace std;

// ******参数传递********************** //
//	2. 形参的初始化与变量的初始化一样，如果形参具有非引用类型，则复制实参的值；如果形参为引用类型，则他只是实参的别名。（值联动）
//	3. 非引用形参调用时，函数不会修改实参的值。
//   值传递与引用传递
// *********************************** //

void swap(int a, int b){
    int temp = 0;
    temp = a;
    a = b;
    b = temp;
}

void swap2(int *a, int *b){
    int temp = 0;
    temp = *a;
    *a = *b;
    *b = temp;
    cout<<*a<<" "<<*b<<endl;
}

//如果函数将形参定义为const类型，则在函数中，不能改变实参的局部副本
void test(const int a, const int b){
    return (a+b)/2;
}


int main(int argc, char const *argv[])
{
    int i = 1, j = 2;
    
    swap(i, j);
    cout<<i<<" "<<j<<endl;
    cout<<"----------------------"<<endl;
    swap2(&i, &j);
    cout<<i<<" "<<j<<endl;
    system("pause");
    return 0;
}
