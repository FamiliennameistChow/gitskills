# include <iostream>

// *************循环语句******************
// 	循环语句包括：
//  1. while循环
// 	2. do while循环
// 	3. for 循环
//  4. 三个关键字break、continue和go
// *****************************************

using namespace std;

// while循环
void test_while()
{
    int i = 1;
    while(i<=10){
        cout<<"i = "<<i<<endl;
        i++;
    }
}

void test_while2()
{
    int sum = 0, i = 1;
    
    while(i<=10){
        sum += i;
        i++;
    }  
    cout<<"sum = "<<sum<<endl;  
}

// do while循环
// 先执行循环体,再判断
void test_do_while()
{
    int i = 1;
    int sum = 0;
    
    do{
        sum += i;
        i++;
    } while (i<=10);
    cout<<"sum = "<<sum<<endl;    
}

// for 循环
void test_for(){
    for(int i = 0; i<=10; i++){
        cout<<"i = "<<i<<endl;
    }
}

//循环嵌套，乘法口诀
void test_for2(){
    for(int i=1; i<=9; i++){
         for(int j=1; j<=i; j++){
              cout<<i<<"*"<<j<<"="<<i*j<<" ";
         }
        cout<<endl;   
    }
}

int main(int argc, char const *argv[])
{
    test_for2();
    system("pause");
    return 0;
}
