#include<stdio.h>
#define MAX 500000
int queue[MAX];
int head=0,tail=0;
void push(int,int);
int randomAccess(int);
void pop(int);
int main(void)
{
  int i,q,x1,x2,x3;
  scanf("%d",&q);
  for(i=0;i<q;i++)
    {
      scanf("%d",&x1);
      switch(x1)
        {
        case 0:
          scanf("%d%d",&x2,&x3);
          push(x2,x3);
          break;
        case 1:
          scanf("%d",&x2);
          printf("%d\n",randomAccess(x2));
          break;
        case 2:
          scanf("%d",&x2);
          pop(x2);
          break;
        }
    }
  return 0;
}

void push(int d,int x)
{
  switch(d)
    {
    case 0:
      head=(head-1+MAX)%MAX;
      queue[head]=x;
      break;
    case 1:
      queue[tail]=x;
      tail=(tail+1)%MAX;
    }
}
int randomAccess(int p)
{
  return queue[(p+head)%MAX];
}
void pop(int p)
{
  switch(p)
    {
    case 0:
      head=(head+1)%MAX;
      break;
    case 1:
      tail=(tail-1+MAX)%MAX;
      break;
    }
}