 # include <iostream>
 # include "Sales_item.h"

main(int argc, char const *argv[])
{
    Sales_item book;
    // 读入ISBN号、售出册数、以及销售价格
    std::cin>>book;
    //写入ISBN、售出册数、总销售额和平均价格
    std::cout<< book<<std::endl;
    system("pause");
    return 0;
}
