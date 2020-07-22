#include <stdio.h>

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

void pushElement(Vector* vec, int a)
{
    if (vec->len < vec->alloc_len)
    {
        memcpy(vec->data + 1, vec->data, sizeof(int) * vec->len++);
        memcpy(vec->data, &a, sizeof(int));
    }
}

int getElement(Vector* vec, int pos)
{
    return vec->data[pos];
}

int popBackElement(Vector* vec)
{
    return vec->data[--vec->len + 1];
}

int popElement(Vector* vec)
{
    int ret = vec->data[0];
    memcpy(vec->data, vec->data + 1, sizeof(int) * --vec->len);
    return ret;
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

    Vector* v = createVector(q*2);
    Vector* ans = createVector(q*2);

    REP(q)
    {
        int com, d, value;
        scanf("%d", &com);
        switch (com)
        {
        case 0:
            scanf("%d%d", &d, &value);
            if (d == 0) pushElement(v, value);
            else appendElement(v, value);
            break;
        case 1:
            scanf("%d", &value);
            appendElement(ans, getElement(v, value));
            break;
        case 2:
            scanf("%d", &d);
            if (d == 0) popElement(v);
            else popBackElement(v);
            break;
        default:
            break;
        }
    }

    REP(ans->len)
    {
        printf("%d\n", getElement(ans, i));
    }

    return 0;
}