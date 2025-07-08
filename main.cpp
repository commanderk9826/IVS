#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int h, w;
    int arr[1001][1001];
    cin >> h >> w;

    for(int i=0; i<h;i++){
        for(int j=0; j<w; j++){
            cin >> arr[i][j];
        }
    }

    int bh, bw;
    int barr[1001][1001];
    cin >> bh >> bw;

    for(int i=0; i<bh;i++){
        for(int j=0; j<bw; j++){
            cin >> barr[i][j];
        }
    }

    int dat[1000001]={0};

    int count =0;
    for(int i=0; i<bh;i++){
        for(int j=0; j<bw; j++){
            // 블랙리스트의 값을 dat배열의 인덱스로 counting
            dat[barr[i][j]]+=1;
        }
    }

    int criminal=0;
    int person=0;

    for(int i=0; i<h;i++){
        for(int j=0; j<w; j++){
            if(dat[arr[i][j]]>0){
                criminal+=1;// DAT배열에 기록되어 있으면 블랙리스트
            }
            else person+=1;// 기록되어 있지 않으면 일반시민
        }
    }

    printf("%d %d\n", person, criminal);

    return 0;
}