# include <iostream>
using namespace std;

// /*
//     while循环
// */
// int main(int argc, char const *argv[])
// {
//     int sum = 0, val = 1;
//     while(val <= 10){
//         sum += val;
//         ++val;
//     }
//     std::cout<<"The sum of 1 to 10 is: "<<sum<<std::endl;
//     system("pause");
//     return 0;
// }


// // ************************for循环
// int main(int argc, char const *argv[])
// {
//     int sum = 0;
//     for (int val = 1; val <= 10; ++val){
//         sum += val;
//     }
//     std::cout<<"The sum of 1 to 10 is: "<<sum<<std::endl;
//     system("pause");
//     return 0;
// }

// // *************读取数量不定的输入数据************** //
// int main(int argc, char const *argv[])
// {
//     /*
//     val设为int类型，检测到输入为int时为True；
//     检测到非int（字母，标点）和文件结束符（end of file）时为False；
//     win下文件结束符为ctrl+Z，然后按Enter;
//     linux下为：ctrl+D
//     */
//     int sum = 0, val = 0;
//     // 读取数据直到遇到文件尾，计算所有读入的值的和
//     while(std::cin>>val)
//     sum += val;
//     std::cout<<"The sum is: "<<sum <<endl;
//     system("pause");
//     return 0;
// }

// ***************if 语句**************
// int main(int argc, char const *argv[])
// {
//     // currVal 是我们正在统计的数，我们将读入的新值存入val
//     int currVal = 0 , val = 0;
//         if(std::cin >> currVal){
//         int cnt = 1;
//         while(std::cin>>val){
//             if (val == currVal)
//             ++ cnt;
//             else{
//                 std::cout << currVal << "occurs" 
//                 << cnt << "times" << std::endl;
//                 currVal = val;
//                 cnt = 1;
//             } 
//         }
//         // 打印文件中最后一个值的数
//         std::cout<<currVal<<"occurs"<<cnt<<"times"<<std::endl;
//     }
//     system("pause");
//     return 0;
// }

// //例子
// int main(int argc, char const *argv[])
// {
//     int pwd, count=0;
//     std::cout<<"please watch out! then input your password!"<<std::endl;
//     std::cin>>pwd;
//     if(pwd==123)
//     {
//         std::cout<<"get the money"<<endl;
//     }
//     else
//     {
//         std::cout<<"the password is error! you have "<<3-count<<" times to modify!"<<std::endl;
//         while(++count<=3)
//         {
//             std::cin>>pwd;
//             if(pwd==123)
//             {
//                 std::cout<<"get the money"<<std::endl;
//                 break;
//             }
//             else
//             {
//                 if(count<3)
//                 {
//                     std::cout<<"the passwaord is wrong! you have "<<3-count<<" times to modify it!"<<std::endl;
//                 }
//                 else
//                 {
//                     std::cout<<"warning! your card is locked!  please contanct with the staff!"<<std::endl;
//                 }
//             }
//         }
//     }
//     system("pause");
//     return 0;
// }

int main(int argc, char const *argv[])
{
    //三元运算
    int a, b, max;
    std::cin>>a>>b;
    max = a>b?a:b;
    std::cout<<"the max between "<<a<<" and "<<b<<" is "<<max<<std::endl;
    system("pause");
    return 0;
}
