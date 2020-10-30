#include <iostream>
/* An alternative method to implement binary search is based on an efficient way to
*  iterate through the elements of the array. The idea is to make jumps and slow
*  the speed when we get closer to the target element. This method is very useful
*  for competitive programming.
*/
using namespace std;

int main() {
    int k = 0;
    int arr[] = {2, 3, 4, 10, 40};
    int x = 3;
    int n = 5;
    for (int b = n/2; b >= 1; b /= 2) {
        while (k+b < n && arr[k+b] <= x) k += b;
    }
    if (arr[k] == x) {
        cout << k;
    }
}
