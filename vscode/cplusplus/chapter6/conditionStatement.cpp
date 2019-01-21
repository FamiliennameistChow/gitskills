# include <iostream>
# include <string>

using namespace std;

void test_switch()
{
    int grade = 4;
    
    switch (grade)
    {
        case 4:
            cout<<"good!"<<endl;
            break;
        case 3:
            cout<<"not bad!"<<endl;
            break;
        default:
            break;
    }
}

void test()
{
    int a=1,b=3;
    int max = a>b?a:b;
}

int main(int argc, char const *argv[])
{
    test_switch();
    system("pause");
    return 0;
}
