#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define REP(n) for (int i=0; i<(n); i++)

typedef struct Vector_tag
{
    int *data;
    int len;
    int alloc_len;
} Vector;

void appendElement(Vector* vec, int a)
{
    if (vec->len < vec->alloc_len)
    {
        memcpy(vec->data + vec->len++, &a, sizeof(int));
    }
}

int getElement(Vector* vec, int pos)
{
    return vec->data[pos];
}

int popBackElement(Vector* vec)
{
    vec->len--;
    return vec->data[vec->len+1];
}

Vector* createVector(int num)
{
    Vector *vec = (Vector*)malloc(sizeof(Vector));
    vec->data = (int*)malloc(sizeof(int)*num);
    // memset(vec->data, 0, vec->len * sizeof(int));
    vec->alloc_len = num;
    vec->len = 0;
    return vec;
}

void reallocateVector(Vector* vec)
{

}

int main(void)
{
    int q;

    scanf("%d", &q);

    Vector* v = createVector(q);

    REP(q)
    {
        int com, value;
        scanf("%d", &com);
        switch (com)
        {
        case 0:
            scanf("%d", &value);
            appendElement(v, value);
            break;
        case 1:
            scanf("%d", &value);
            printf("%d\n", getElement(v, value));
            break;
        case 2:
            popBackElement(v);
            break;
        default:
            break;
        }
    }

    return 0;
}