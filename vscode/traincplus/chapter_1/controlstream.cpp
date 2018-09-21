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
int main(int argc, char const *argv[])
{
    // currVal 是我们正在统计的数，我们将读入的新值存入val
    int currVal = 0 , val = 0;
        if(std::cin >> currVal){
        int cnt = 1;
        while(std::cin>>val){
            if (val == currVal)
            ++ cnt;
            else{
                std::cout << currVal << "occurs" 
                << cnt << "times" << std::endl;
                currVal = val;
                cnt = 1;
            } 
        }
        // 打印文件中最后一个值的数
        std::cout<<currVal<<"occurs"<<cnt<<"times"<<std::endl;
    }
    system("pause");
    return 0;
}
