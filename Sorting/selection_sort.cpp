#include <iostream>

using namespace std;

void selectionSort(int array[], int length) {
    for (int i = 0; i < length; ++i) {
        
        int indexMin = i;

        for (int j = i + 1; j < length; ++j) {
            if (array[j] < array[indexMin]) indexMin = j;
        }

        swap(array[i], array[indexMin]);
    }
}

int main() {

    int N;
    cin >> N;

    int array[N];
    for (int i = 0; i < N; ++i) {
        cin >> array[i];
    }

    selectionSort(array, N);
    for (int i = 0; i < N; ++i) {
        cout << array[i] << " ";
    }

    return 0;
}
