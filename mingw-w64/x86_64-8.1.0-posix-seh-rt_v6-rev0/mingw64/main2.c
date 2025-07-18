#include <stdio.h>
#include <stdlib.h>

int buffer1[10] = { 0, };
int index1 = 0;
int buffer2[10] = { 0, };
int index2 = 0;
int totalSum = 0;

int getAverage1(int input) {
    int sum = 0;
    buffer1[index1] = input;
    index1++;

    //index 범위 안 넘게
    if (index1 >= 10) index1 = 0;

     for (int i = 0; i < 10; i++)
        sum = sum + buffer1[i];
    return sum / 10;
}

int getAverage2(int input) {
    totalSum = totalSum - buffer2[index2];
    buffer2[index2] = input;
    totalSum = totalSum + buffer2[index2];
    index2++;
    if (index2 >= 10)
         index2 = 0;
    return totalSum / 10;
}

void main() {
    for (int i = 0; i < 20; i++)
        printf("%d\n", getAverage1(10));
    for (int i = 0; i < 20; i++)
        printf("%d\n", getAverage2(10));
    system("pause");
}



