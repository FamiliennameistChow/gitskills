# include <iostream>
using namespace std;
int main(int argc, char const *argv[])
{
//1、整型字面常量
int i = 100; //十进制
int j = 024; //8进制
int k = 0x16;//十六进制
long l = 12345L;//L表示长整型字面常量
unsigned int ui = 100u;//无符号
//2、浮点数
float f = 3.14f;
long double ld = 3.1415L;
float fl = 1.38e5; 
//3、布尔字面常量
bool flag = true;
flag = false;
//4、字符字面常量
char c = 'A';
//5、转义字符
string str = "Hello\tWorld!";
cout<<str.c_str()<<endl;
//6、字符串字面常量
string strl = "www.geek99.com";

system("pause");
return 0;

}
