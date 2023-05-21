/*
 * @lc app=leetcode id=215 lang=c
 *
 * [215] Kth Largest Element in an Array
 */

// @lc code=start
#include <stdio.h>
#include <stdlib.h>

void swap(int* heap, int indexParent, int indexChild)
{
    int tmp = heap[indexParent];
    heap[indexParent] = heap[indexChild];
    heap[indexChild] = tmp;
}

void heapify(int* heap, int rootSize)
{
    int parent;
    if (rootSize == 0)
    {
        return;
    }
    if (rootSize % 2 == 0 )
    {
        // on the right
        parent = (rootSize - 2) / 2;
    }
    else
    {
        // on the left
        parent = (rootSize - 1) / 2;
    }
    if (heap[parent] < heap[rootSize])
    {
        //need to swap
        // printf("\nNeed to swap %i greater than %i\n",heap[parent],heap[rootSize]);
        swap(heap, parent, rootSize);
        heapify(heap, parent);
    }

}

int getLeft(int index)
{
    return index * 2 + 1;
}

int getRight(int index)
{
    return index * 2 + 2;
}

void delete(int* heap, int* heapSize)
{
    swap(heap, 0, (*heapSize)-1);
    heap[(*heapSize)-1] = NULL;
    (*heapSize)--;
    int currIndex = 0;
    int leftIndex = getLeft(currIndex);
    int rightIndex = getRight(currIndex);
    while ((leftIndex < (*heapSize)) && (rightIndex < (*heapSize)))
    {
        //Find which child is largest. if value is larger than that we swap
        if(heap[leftIndex] >= heap[rightIndex])
        {
            if(heap[currIndex] < heap[leftIndex])
            {
                swap(heap, currIndex, leftIndex);
                currIndex = leftIndex;
            }
            else
            {
                // if we arrive here, the left child is greater than or equal to right
                // but also left child is less than the parent. this means we stop
                return;
            }

        }
        else
        {
            // if we arrive here the right index is greater than left
            if(heap[currIndex] < heap[rightIndex])
            {
                swap(heap, currIndex, rightIndex);
                currIndex = rightIndex;
            }
            else
            {
                return;
            }

        }
        leftIndex = getLeft(currIndex);
        rightIndex = getRight(currIndex);
    }
    // one final check
    if (leftIndex < (*heapSize))
    {
        if(heap[currIndex] < heap[leftIndex])
        {
            swap(heap, currIndex, leftIndex);
        }
    }
    

}

int findKthLargest(int* nums, int numsSize, int k){
    int* heap = malloc(numsSize * sizeof(int));
    for(int i = 0; i < numsSize; i++)
    {
        heap[i] = nums[i];
        heapify(heap, i);

    }
    
    // printTree(heap, numsSize);
    for(int i = 0; i < k-1; i++)
    {
        delete(heap, &numsSize);
        // printTree(heap, numsSize);

    }
    return heap[0];
}

void printTree(int* heap, int numsSize)
{
    for(int i = 0; i < numsSize; i++)
    {
        printf("%i", heap[i]);
    }
    printf("\n");
}


// @lc code=end

