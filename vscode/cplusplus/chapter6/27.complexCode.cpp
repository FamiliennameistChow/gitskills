# include <iostream>

// ******************************************* 
// 复合语句（块语句）
// 块语句中变量的作用域在块内有效、块语句通常是一个函数体，或者条件判断语句块或循环体语句块。
// ******************************************* 
using namespace std;

void test()
{
    cout<<"please input an int:"<<endl;
    int i;
    
    while(cin>>i&&i != -1){

        int a = 100; //作用域在while中
        
        if (i%2 != 0) {
            int b = 200; //作用域在if{}中
            cout<<"奇数"<<endl;
        
        }else {
            int c = 300;  //作用域在else{}中
            cout<<"偶数"<<endl;
        }
        
    }
    

}

int main(int argc, char const *argv[])
{
    test();
    system("pause");
    return 0;
}
