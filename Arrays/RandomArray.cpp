#include <iostream>;
using namespace std;

/*A program that takes an array and generates random values within*/

void randomArray(int array[], int size)
{
 	int aRandVar;
	for(int i = 0; i < size; i++ )
	{
     aRandVar = rand() % size;

     array[i] = aRandVar;
	}
}

int main(){
  int sample_array[100];
  randomArray(sample_array, 100);
  return 0;
}
