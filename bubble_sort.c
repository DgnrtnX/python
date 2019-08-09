#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}


void bubbleSort(int arr[], int n)
{
   int i, j;
   for (i = 0; i < n-1; i++)

       for (j = 0; j < n-i-1; j++)
           if (arr[j] > arr[j+1])
              swap(&arr[j], &arr[j+1]);
}

int main(int argc, char const *argv[]) {
  int stat=10;
  int a[]={5,9,2,0,3,4,1,8};
  int size= sizeof(a)/sizeof(a[0]);
  int id= fork();


  if (id > 0) {
    printf("parent process\n");
    bubbleSort(a,size);
    printf("sorted array is: \n");
    for (int i = 0; i < size; i++) {
      printf("\t%d\n",a[i]);
    }
  } else {
    printf("Child process \n");

        printf("numbers to be sorted are: \n");
        wait(&stat);
        for (int i = 0; i < size; i++)
          printf("\t%d\n",a[i]);
  }
  return 0;
}
