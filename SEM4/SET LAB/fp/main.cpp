#include<iostream>
using namespace std;

int main()
{
    int a ,b, c, d ,e ;
    int x[15];
    char X1,X2,X3,X4,X5 ,S , A, C;
    int Ei,Eo,Ein,Ef,intf,UFC,TCF,FP;
    int Sum=0;
    cout<<"Enter External input :";
    cin>>a;
    cout<<"Enter if Simple[S] , average[A] or complex[C]:";
    cin>>X1;

    cout<<"Enter External output :";
    cin>>b;
    cout<<"Enter if Simple[S] , average[A] or complex[C]:";
    cin>>X2;

    cout<<"Enter External inquires :";
    cin>>c;
    cout<<"Enter if Simple[S] , average[A] or complex[C]:";
    cin>>X3;

    cout<<"Enter External files :";
    cin>>d;
    cout<<"Enter if Simple[S] , average[A] or complex[C]:";
    cin>>X4;

    cout<<"Enter Internal files :";
    cin>>e;
    cout<<"Enter if Simple[S] , average[A] or complex[C]:";
    cin>>X5;

    if(X1=='s') Ei=a*3;
    else if (X1=='a') Ei=a*4;
    else Ei=a*6;

    if(X2=='s') Eo=b*4;
    else if (X2=='a') Eo=b*5;
    else Eo=b*7;

    if(X3=='s') Ein=c*3;
    else if (X3=='a') Ein=c*4;
    else Ein=c*6;

    if(X4=='s') Ef=d*7;
    else if (X4=='a') Ef=d*10;
    else Ef=d*15;

    if(X5=='s') intf=e*5;
    else if (X5=='a') intf=e*7;
    else intf=e*10;

    UFC= Ei + Eo + Ein + Ef + intf;
    cout<<"UFC:"<<UFC<<"\n";

    for (int i=1 ; i<15 ;i++)
    {
        cout<<"F"<<i<<":";
        cin>>x[i];
        Sum=Sum+x[i];
    }

    TCF = 0.65 + 0.01*Sum;
    cout<<"TCF:"<<TCF<<"\n";

    FP=TCF*UFC;
    cout<<"FP:"<<FP;
}
