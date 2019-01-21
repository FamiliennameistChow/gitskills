# include <iostream>
# include <vector>
using namespace std;

void test1()
{
    int i = 0, j = 0;
    cout<<i++<<endl;
    cout<<++j<<endl;
}

void test2()
{
    const int length = 5;
    int arr[] = {1,2,3,4,5};
    int *p = arr;  //表示指向数组的首地址
    for (int i = 0;i<length;i++)
    {
        cout<<arr[i]<<endl;
    }
    cout<<"--------------"<<endl;
    for(int i = 0; i<length; i++)
    {
        cout<<*p++<<endl;
    }

    vector<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);

    //迭代器访问
    vector<int>::const_iterator it = v.begin();
    while(it != v.end())
    {
        cout<<*it++<<endl;
    }
}

int main(int argc, char const *argv[])
{
    test2();
    system("pause");
    return 0;
}
