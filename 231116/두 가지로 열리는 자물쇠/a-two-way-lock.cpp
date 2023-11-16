#include <stdio.h>
#include <algorithm>
using namespace std;

int n, a[6];

int main() {
    //in
    scanf("%d", &n);
    int i, j, k, cnt = 0;
    for(i = 0; i < 6; i++){
        scanf("%d", &a[i]);
    }
    //pro
    for(i = 1; i <= n; i++){
        for(j = 1; j <= n; j++){
            for(k = 1; k <= n; k++){
                if((abs(a[0] - i) <= 2 || abs(a[0] - i) >= n-2)&&
                (abs(a[1] - j) <= 2 || abs(a[1] - j) >= n-2) &&
                (abs(a[2] - k) <= 2 || abs(a[2] - k) >= n-2)) cnt++;
                else if((abs(a[3] - i) <= 2 || abs(a[3] - i) >= n-2)&&
                (abs(a[4] - j) <= 2 || abs(a[4] - j) >= n-2)&&
                (abs(a[5] - k) <= 2 || abs(a[5] - k) >= n-2)) cnt++;
            }
        }
    }
    //out
    printf("%d", cnt);

    return 0;
}