#include "array.h"

int main()
{
    int sum = 0;
    for (int i = 0; i < ARRAY_SIZE; ++i)
        if (arr1[i] > 0)
            sum += arr1[i];

    return sum;
}
