# include <iostream>
# include <string>

using namespace std;

void test1()
{
    string s;
    string s2(s);
    string s3("hello world");
    string s4(3, 'a');

}

void test2()
{
    string s;
    cout<<"please intput an string!"<<endl;
    cin>>s;
    cout<<s<<endl;
}

void test3()
{   
    string s;
    
    while(getline(cin, s)){
        cout<<s<<endl;
        if(s=="bye")
        {
            break;
        }
    }
    
}

void test4()
{
    string s;
    getline(cin, s);
    cout<<s<<endl;
}

void test5()
{
    string s = "hello world!";
    string s1 = "welcome";

    cout<<s.empty()<<endl;  //是否为空

    int size = s.size();  //字符串大小
    cout<<size<<endl;

    char c = s[1];  //字符串切片
    cout<<c<<endl;

    s = s + s1;  //字符串链接
    cout<<s<<endl;

    cout<<(s1==s)<<endl; //字符串比较
}

int main(int argc, char const *argv[])
{
    
    // test3();
    test5();   
    system("pause");
    return 0;
}
