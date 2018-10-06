# include <iostream>
# include <vector>

using namespace std;

class Person 
{

};

int main(int argc, char const *argv[])
{
    //向量的声明
    //vector是模板类，声明时需要指定类型
    vector<int> v;
    vector<double> v1;
    vector<string> v2;
    vector<Person> v3; 

    //添加
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);  //在末尾添加

    //获取某位元素
    int x = v.at(2);
	cout << "2nd is:" << x << endl;

    //插入元素
    v.insert(v.begin(), 3);

    // //遍历--循环
    // int size = v.size();
    // for (int i=0; i<size; i++)
    // {
    //     cout<<v[i]<<endl;
    // }

    //遍历--迭代器iterator
    vector<int>::const_iterator it = v.begin();
    
    while(it != v.end()){
        cout<<*it++<<endl;  //++的优先级比*高
    }

    cout<<"the size is "<<v.size()<<endl;

    cout<<"-------------------"<<endl;
    cout<<v.front()<<endl;  //最前面的元素
    cout<<v.back()<<endl;  //最后面的元素
    
    cout<<"----erase------"<<endl;
    it = v.begin();
    v.erase(it + 1); //需要用到迭代器  it表示第一个元素， it + 1表示第二个元素 ....
    // v.insert(it + 1, 5); //在第二个索引处插入
    cout<<"after erase the 2nd param, the size is: "<<v.size()<<endl;

    cout<<"-------------------"<<endl;
    while(it != v.end()){
        cout<<*it++<<endl;  //++的优先级比*高
    }
     
    system("pause");
    return 0;
}
