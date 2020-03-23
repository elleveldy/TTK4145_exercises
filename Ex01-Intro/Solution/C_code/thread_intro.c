//haakoneh & erlendvd

#include <pthread.h>
#include <stdio.h>


int i = 0;

void* thread_func_1(){
	unsigned int j;
	for(j = 0; j < 1000000; j++){
		i++;
	}
	return NULL;
}

void* thread_func_2(){
	unsigned int j;
	for(j = 0; j < 1000000; j++){
		i--;
	}
	return NULL;
}

int main(){
    pthread_t thread_1;
    pthread_t thread_2;

    pthread_create(&thread_1, NULL, thread_func_1, NULL);
    pthread_create(&thread_2, NULL, thread_func_2, NULL);

    printf("Before joined threads:  %i\n", i);

    pthread_join(thread_1, NULL);
    pthread_join(thread_2, NULL);

    printf("After joined threads:  %i\n", i);

    return 0;
}
