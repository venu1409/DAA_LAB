#include <stdio.h>

int Linear_Search(int arr[], int size, int key)
{
    for(int i = 0; i < size; i++)
    {
        if(arr[i] == key)
        {
            return i;
        }
    }
    return -1;
}

int main()
{
    int size, key, result;

    printf("Enter number of elements: ");
    scanf("%d", &size);

    int arr[size];

    printf("Enter %d elements:\n", size);
    for(int i = 0; i < size; i++)
    {
        scanf("%d", &arr[i]);
    }

    printf("Enter element to search: ");
    scanf("%d", &key);

    result = Linear_Search(arr, size, key);

    if(result == -1)
        printf("Element not found.\n");
    else
        printf("Element found at position %d (index %d).\n", result + 1, result);

    return 0;
}
