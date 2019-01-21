# include <iostream>
# include <string>
# include <vector>

using namespace std;

void test()
{
    string s;
    cout<<"please input a string:"<<endl;
    while(cin>>s&&s != "bye");  //第一种写法 使用空语句;

    /* 第二种写法
    while(cin>>s)
    {
        if (s == "bye")
        break;
    }
    */
}

void test2()
{
    vector<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);

    vector<int>::const_iterator it = v.begin();
    while(it != v.end())
        cout<<*it++<<endl;
}

int main(int argc, char const *argv[])
{
    // int i = 1;
    // int j = 2;
    // int sum = i + j;
    // cout<<sum<<endl;
    test2();

    system("pause");
    return 0;
}
