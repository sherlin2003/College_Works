#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

#define MAX_UNIT 8 // 8 units

void *patients(void *num1);
void *units(void *num2);
int maxCount();
void wait(int secs);
void randWait(int lower, int upper);

sem_t unit_state[MAX_UNIT]; // Semaphore to using as mutex and keep unit state -empty or busy
sem_t count[MAX_UNIT]; // Semaphore to unit capacity, max 3

int allDone = 0;

int main(int argc, char *argv[])
{
    // Taking input, initiliazing and creating

    int numPatient,x;
    printf("Enter number of patients in multiples of 3:\n");
    scanf("%d",&x); // Input for patient number
    numPatient = x; // Input patient number
    if (numPatient % 3 != 0) {
       printf("Please enter the number of patients in multiples of 3.\n");
       system("PAUSE");
       return 0;
    }

    pthread_t patient[numPatient]; // Patient threads
    pthread_t unit[MAX_UNIT]; // Unit threads

    int i, j, Number1[numPatient]; int Number2[MAX_UNIT];

    for (j = 0; j < MAX_UNIT; j++) { // Firstly create unit semaphores and threads
	Number2[j] = j;
	sem_init(&unit_state[j], 0, 1);  // Empty or busy state for unit
    sem_init(&count[j], 0, 3);
    pthread_create(&unit[j], NULL, units, (void *)&Number2[j]);
    }

    for (i = 0; i < numPatient; i++) { // Secondly create patient semaphores and threads
    randWait(1,3); // Patients come randomly time between 1-3
	Number1[i] = i;
    pthread_create(&patient[i], NULL, patients, (void *)&Number1[i]);
    }

    for (i = 0; i < numPatient; i++) { // Firstly join patient threads
        pthread_join(patient[i],NULL);
    }

    allDone = 1;


    for (j = 0; j < MAX_UNIT; j++) { // After all patients are done, join unit threads
        pthread_join(unit[j],NULL);
    }

    printf("All of the patients are done.\n"); // Finish
    return 0;
}

// Patient's control to entering an unit and unit's states controls
void *patients(void *number1) {
    int num1 = *(int *)number1; // Patients id
    int value_state[8]; // Int value for keeping unit_state semaphore's value
    int value_count[8]; // Int value for keeping count semaphore's value
    printf("\n");
    printf("\n► ► ► ►    Patient %d arrived at Covid-19 units in hospital.\n", num1);
    printf("\n");
    randWait(1,2);
    int unit_id = maxCount(); // Function for finding mmax unit capacity. unit_id is for maxCount func's value.
    while(1){
        sem_getvalue(&unit_state[unit_id],&value_state[unit_id]);
        if(value_state[unit_id] == 1){ // If unit is locked, wait for unlocked unit. value_state must not be 0
            break;
        }
    }
    sem_wait(&count[unit_id]); // If a patient enter an unit, count[unit_id]'value = count[unit_id]'value - 1
    sem_getvalue(&count[unit_id],&value_count[unit_id]); // Get count's value for using in if condition
    sem_getvalue(&unit_state[unit_id],&value_state[unit_id]); // Get unit_state's value for using in if condition
    // Printing units state and counts
    if(value_count[unit_id] == 2 && value_state[unit_id] == 1){ // If unit has 1 patient and the state is 1.
        printf("\n");
        printf("\n");
        printf("\nPatient %d entered unit %d. Unit %d has 1 patient.\n",num1,unit_id,unit_id);
        printf("            ---------\nUNIT %d ---> |   i   |\n            ---------",unit_id);
        sem_getvalue(&unit_state[unit_id],&value_state[unit_id]); // get state values for printing
        printf("\n(Unit %d, State %d)\n",unit_id,value_state[unit_id]);
        printf("\n");
        printf("\n");
    }
    if(value_count[unit_id] == 1 && value_state[unit_id] == 1){ // If unit has 2 patients and the state is 1.
        printf("\n");
        printf("\n");
        printf("\nPatient %d entered unit %d. Unit %d has 2 patients.\n",num1,unit_id,unit_id);
        printf("\nThe last people for unit %d, let's start! Please, pay attention to your social distance and hygiene; use a mask.\n",unit_id);
        printf("            ---------\nUNIT %d ---> |   ii  |\n            ---------",unit_id);
        sem_getvalue(&unit_state[unit_id],&value_state[unit_id]); // get state values for printing
        printf("\n(Unit %d, State %d)\n",unit_id,value_state[unit_id]);
        printf("\n");
        printf("\n");
    }
    if(value_count[unit_id] == 0 && value_state[unit_id] == 1){ // If unit has 3 patients and the state is 1 at the first.
        printf("\n");
        printf("\n");
        printf("\nPatient %d entered unit %d. Unit %d has 3 patients. Unit is busy.\n",num1,unit_id,unit_id);
        printf("            ---------\nUNIT %d ---> |  iii  |\n            ---------",unit_id);

        // If the unit is full, the unit_state will be 0
        sem_wait(&unit_state[unit_id]); // Unit is locked

        sem_getvalue(&unit_state[unit_id],&value_state[unit_id]); // Get state values for printing
        printf("\n(Unit %d, State %d)\n",unit_id,value_state[unit_id]);
        printf("\n♦ ♦ ♦ ♦ ♦ ♦  L O C K E D  ♦ ♦ ♦ ♦ ♦\n");
        printf("\n");
        printf("\n");
        // After this if condition, 3 patients leaved the unit in *units
    }
}

// Controls to condition for 3 patients leaving the unit at the same time and
// Unit's control to waiting for unlocked state after cleaning the unit
void *units(void *number2){
    int num2 = *(int *)number2; // Unit ids
    int value_state[8]; // Int value for keeping unit_state semaphore's value
    int value_count[8]; // Int value for keeping count semaphore's value
    while(!allDone){
        if(!allDone){ // Until all the patients are gone...
            sem_getvalue(&unit_state[num2],&value_state[num2]); // Get unit_state value for using in if condition
            sem_getvalue(&count[num2],&value_count[num2]); // Get count value for using in if condition
            if(value_state[num2] == 0 && value_count[num2] == 0){ // if the unit is busy and capacity is full
                sem_post(&count[num2]); // First patient is gone with increasing count semaphore
                sem_post(&count[num2]); // Second patient is gone with increasing count semaphore
                sem_post(&count[num2]); // Third patient is gone with increasing count semaphore

                // The unit is empty now

                // Printing states for the unit and patients
                printf("\n");
                printf("\n");
                printf("\nPatients left unit %d. Unit has no patient. Unit is empty.\n",num2);
                printf("            ---------\nUNIT %d ---> |       |\n            ---------",num2);
                printf("\n.......Waiting unit %d for cleaning.......\n",num2);

                printf("\n(The cleaning process will take 30 sleeps. Please don't exit the program.)\n");
                wait(30); // Waiting 30 sleeps for cleaning the unit
                // As the waiting time decreases, the number of units used decreases because
                // With the emptying of the first used units, patients go to these units

                sem_post(&unit_state[num2]); // The unit is empty so increase unit_state semaphore to 1

                sem_getvalue(&unit_state[num2],&value_state[num2]); // Get values for printing the unit states
                printf("\nUnit %d cleaned. Unit is ready.\n",num2);
                printf("            ---------\nUNIT %d ---> |   ❀   |\n            ---------",num2);
                printf("\n(Unit %d, State %d)\n",num2,value_state[num2]);
                printf("\n♦ ♦ ♦ ♦ ♦  U N L O C K E D  ♦ ♦ ♦ ♦ ♦\n");
                printf("\n");
                printf("\n");
            }
        }
        else // When there isn't any patient in hospital
        {
            printf("All patient is done.\n");
        }

    }
}

// Func. for finding the unit with min capacity
int maxCount(){
    int value_count[8],value_state[8],temp,unit_id;
    int min = 3; // Empty room value
    for(int i = 0; i < MAX_UNIT; i++){ // Loop all unit
        sem_getvalue(&count[i],&value_count[i]); // Get semaphore values for using in if condition
        sem_getvalue(&unit_state[i],&value_state[i]); // Get semaphore values for using in if condition
        temp = value_count[i];
        if(value_state[i] == 1 && value_count[i] != 0 && temp <= min){ // Finding min value
            // Because the lower the value, the more full the unit
            min = temp; // Finding min value
            unit_id = i;
        }
    }
    return unit_id; // Unit id for using in *patients
}

// Waiting time
void wait(int secs) {
     int len = secs;
     sleep(len);
}

// Waiting random time for patients to using in creating threads
void randWait(int lower, int upper) {
    int num = (rand() %
        (upper - lower + 1)) + lower;
    sleep(num);
}
