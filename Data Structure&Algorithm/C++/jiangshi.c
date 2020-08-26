#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
int main()
{
    printf("pid=%d",getpid());
    pid_t pid=fork();
    if(pid<0){
        printf("fork error");
        return -1;
    }else if(pid==0){
        printf("This is parent");
        sleep(5);
        exit(0);
    }else{
        printf("This child");
    }
    while(1){
        printf("-------------pid = %d\n",getpid());
        sleep(1);
    }
    return 0;
}