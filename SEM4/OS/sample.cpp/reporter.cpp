#include <iostream>
#include <stdlib.h>
#include <vector>
#include <map>
#include <pthread.h>
#include <semaphore.h>
using namespace std;

sem_t read_mutex, write_mutex;

map<int, int> accepted_files;
map<int, vector<int>> rejected_files;
map<int, int>::iterator it;

void *reader_util(void *)
{
}

void *writer_util(void *)
{
}

int main(int argc, char *argv[])
{
    // cout<<argc;
    if (argc != 3)
    {
        printf("Wrong set of arguments.. Please enter two numbers as arguments\n");
        printf("\nPrgram exiting...\n");
        exit(0);
    }
    int n, m;

    n = atoi(argv[1]); // n  --->  number of editors;
    m = atoi(argv[2]); //  m  --->  number of reports/aricles

    // Initialization
    for (int i = 0; i < m; i++)
    {
        accepted_files[i] = -1;
    }

    int random = rand() % 2;

    pthread_t readers[n];
    pthread_t writers[n];

    for (int i = 0; i < n; i++)
    {
        pthread_create(&readers[i], NULL, reader_util, NULL);
        pthread_create(&writers[i], NULL, writer_util, NULL);
    }

    for (int i = 0; i < n; i++)
    {
        pthread_join(readers[i], NULL);
        pthread_join(writers[i], NULL);
    }

    return 0;
}
