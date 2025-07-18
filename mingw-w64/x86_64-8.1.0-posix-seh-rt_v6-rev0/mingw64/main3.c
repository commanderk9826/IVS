#include <stdio.h>
#include <stdlib.h>
int main()
{
    int numArr[3][4] = {
        { 11, 22, 33, 44 },
        { 55, 66, 77, 88 },
        { 99, 110, 121, 132 }
    };
    //printf("%d\n", numArr[0][0]);
    //printf("%d\n", numArr[1][2]);
    //printf("%d\n", numArr[2][0]);
    //printf("%d\n", numArr[2][3]);
    printf("%d\n", 0[(0[numArr])]); // 11
    // [1][2], [2][0] [2][3] 를 위와같은 표현으로 표기하라
    printf("%d\n", 2[(1[numArr])]); // 77
    printf("%d\n", 0[(2[numArr])]); // 99
    printf("%d\n", 3[(2[numArr])]); // 132
    system("pause");
    return 0;
}
