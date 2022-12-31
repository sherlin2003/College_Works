#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <semaphore.h>
#include <errno.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <pthread.h>
#include <string.h>
#include <time.h>

#define LED_R	3
#define LED_Y	2
#define LED_G	0
#define SW_R	6
#define SW_Y	5
#define SW_G	4
#define SW_W	27

void init();
void off();
void lightOn(int RYG);
void startAndSuccess();
void fail();

void whiteBtnClicked();
void redBtnClicked();
void yellowBtnClicked();
void greenBtnClicked();

int randomBox[5];
int input[5];
int inputIndex;
int semValue;
int currentIndex;

sem_t* stageSem;
int id;
int status;
pthread_t btnThread[4];

int main()
{
    sem_unlink("stageSem");
    if((stageSem = sem_open("stageSem", O_CREAT, 0644, 0)) == SEM_FAILED) {
	perror("Sem failed");
	exit(1);
    }

    init();

    return 0;
}

void init() {
    int i,j;

    if(wiringPiSetup() == -1) {
	exit(1);
    }

    pinMode(SW_R, INPUT);
    pinMode(SW_Y, INPUT);
    pinMode(SW_G, INPUT);
    pinMode(SW_W, INPUT);
    pinMode(LED_R, OUTPUT);
    pinMode(LED_Y, OUTPUT);
    pinMode(LED_G, OUTPUT);

    startAndSuccess();

    // Generating Random number
    printf("Generating random number...\n");
    srand(time(NULL));
    for(i=0; i<5; i++) {
	randomBox[i] = (rand() % 3) + 1;
	printf("randomBox[%d] : %d\n",i,randomBox[i]);
    }

    printf("\n\nGame Start!!\n\n");
    id = pthread_create(&btnThread[0], NULL, (void*)&whiteBtnClicked, NULL);
    id = pthread_create(&btnThread[1], NULL, (void*)&redBtnClicked, NULL);
    id = pthread_create(&btnThread[2], NULL, (void*)&yellowBtnClicked, NULL);
    id = pthread_create(&btnThread[3], NULL, (void*)&greenBtnClicked, NULL);

    for(i=0; i<5; i++) {

	// Initialize game
	memset(input,0,sizeof(input));
	inputIndex = 0;
	currentIndex = i;

	printf("\nStage %d\n\n",i+1);
	delay(500);

	for(j=0; j<=i; j++) {
	    lightOn(randomBox[j]);
	}

	sem_wait(stageSem);

	// Compare input and random array
	for(j=0; j<=i; j++) {
	    if(input[j] != randomBox[j]) {
		fail();
		return;
	    }
	}

	printf("\nStage %d Clear!! \n",i+1);
	delay(500);
    }

    printf("\nAll Clear!!\n");
    startAndSuccess();
}

void off() {
    digitalWrite(LED_R, 0);
    digitalWrite(LED_Y, 0);
    digitalWrite(LED_G, 0);
}

void lightOn(int RYG) {
    if(RYG == 1) {
	digitalWrite(LED_R, 1);
	delay(300);
	digitalWrite(LED_R, 0);
    } else if(RYG == 2) {
	digitalWrite(LED_Y, 1);
	delay(300);
	digitalWrite(LED_Y, 0);
    } else if(RYG == 3) {
	digitalWrite(LED_G, 1);
	delay(300);
	digitalWrite(LED_G, 0);
    }
    delay(200);
}

void startAndSuccess() {
    int i=3;

    while(i--) {
	digitalWrite(LED_R, 1);
	delay(250);
	digitalWrite(LED_R, 0);

	digitalWrite(LED_Y, 1);
	delay(250);
	digitalWrite(LED_Y, 0);

	digitalWrite(LED_G, 1);
	delay(250);
	digitalWrite(LED_G, 0);
    }
}

void fail() {
    int i=3;

    printf("\nWrong answer !!\n");
    printf("Game Over..\n\n");

    while(i--) {
	digitalWrite(LED_R, 1);
	digitalWrite(LED_Y, 1);
	digitalWrite(LED_G, 1);
	delay(250);
	digitalWrite(LED_R, 0);
	digitalWrite(LED_Y, 0);
	digitalWrite(LED_G, 0);
	delay(250);
    }
}

void whiteBtnClicked() {
    while(1) {
	if(digitalRead(SW_W) == 0) {
	    printf("\n========================\n");
	    printf("White button clicked!\n");
	    printf("========================\n");
	    sem_post(stageSem);
	    delay(500);
	}
    }
}

void redBtnClicked() {
    while(1) {
	if(digitalRead(SW_R) == 0) {
	    if(inputIndex > currentIndex) {
		input[0] = 0;
		delay(250);
		sem_post(stageSem);
		break;
	    }

	    digitalWrite(LED_R, 1);
	    delay(500);
	    digitalWrite(LED_R, 0);

	    printf("\n========================\n");
	    printf("Red button clicked!\n");
	    input[inputIndex] = 1;
	    printf("input[%d] = %d\n",inputIndex,input[inputIndex]);
	    inputIndex++;
	    printf("========================\n");
	}
    }
}

void yellowBtnClicked() {
    while(1) {
	if(digitalRead(SW_Y) == 0) {
	    if(inputIndex > currentIndex) {
		input[0] = 0;
		delay(250);
		sem_post(stageSem);
		break;
	    }

	    digitalWrite(LED_Y, 1);
	    delay(500);
	    digitalWrite(LED_Y, 0);

	    printf("\n========================\n");
	    printf("Yellow button clicked!\n");
	    input[inputIndex] = 2;
	    printf("input[%d] = %d\n",inputIndex,input[inputIndex]);
	    inputIndex++;
	    printf("========================\n");
	}
    }
}

void greenBtnClicked() {
    while(1) {
	if(digitalRead(SW_G) == 0) {
	    if(inputIndex > currentIndex) {
		input[0] = 0;
		delay(250);
		sem_post(stageSem);
		break;
	    }

	    digitalWrite(LED_G, 1);
	    delay(500);
	    digitalWrite(LED_G, 0);

	    printf("\n========================\n");
	    printf("Green button clicked!\n");
	    input[inputIndex] = 3;
	    printf("input[%d] = %d\n",inputIndex,input[inputIndex]);
	    inputIndex++;
	    printf("========================\n");
	}
    }
}

