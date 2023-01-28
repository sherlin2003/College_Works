#include<iostream>
using namespace std;
int fail(int s)
{
    if(s>=0 && s<=45)
    {
        return 46;
    }
    else if(s>=46 && s<=48)
    {
        return 49;
    }
    else if(s>=49 && s<=51)
    {
        return 52;
    }
    else if(s>=52 && s<=57)
    {
        return 58;
    }
}
int main()
{
    int state=0;
    char a[50];
    cin>>a;
    int i=0;
    while(1)
    {
        switch(state)
        {
        case 0:
            if(a[i]=='c')
            {
                state=1;
                i++;
            }
            else if(a[i]=='g')
            {
                state=12;
                i++;
            }
            else if(a[i]=='f')
            {
                state=17;
                i++;
            }
            else if(a[i]=='d')
            {
                state=27;
                i++;
            }
            else if(a[i]=='t')
            {
                state=35;
                i++;
            }
            else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 1:
            if(a[i]=='a')
            {
                state=2;
                i++;
            }
            else if(a[i]=='o')
            {
                state=7;
                i++;
            }
            else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 2:
            if(a[i]=='t')
            {
                state=3;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 3:
            if(a[i]=='c')
            {
                state=4;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 4:
            if(a[i]=='h')
            {
                state=5;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 5:
            if(a[i]==' ' || a[i]=='\0')
            {
                state=6;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 6:
            cout<<"catch is a keyword"<<endl;
            return 0;
        case 7:
            if(a[i]=='n')
            {
                state=8;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 8:
            if(a[i]=='s')
            {
                state=9;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 9:
            if(a[i]=='t')
            {
                state=10;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 10:
            if(a[i]==' ' || a[i]=='\0')
            {
                state=11;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 11:
            cout<<"const is a keyword"<<endl;
            return 0;
        case 12:
            if(a[i]=='o')
            {
                state=13;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 13:
            if(a[i]=='t')
            {
                state=14;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 14:
            if(a[i]=='0')
            {
                state=15;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 15:
            if(a[i]==' ' || a[i]=='\0')
            {
                state=16;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 16:
            cout<<"goto is a keyword"<<endl;
            return 0;
        case 17:
            if(a[i]=='o')
            {
                state=18;
                i++;
            }
            else if(a[i]=='r')
            {
                state=21;
                i++;
            }
            else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 18:
            if(a[i]=='r')
            {
                state=19;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 19:
            if(a[i]==' ' || a[i]=='\0')
            {
                state=20;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 20:
            cout<<"for is a keyword"<<endl;
            return 0;
        case 21:
            if(a[i]=='i')
            {
                state=22;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 22:
            if(a[i]=='e')
            {
                state=23;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 23:
            if(a[i]=='n')
            {
                state=24;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 24:
            if(a[i]=='d')
            {
                state=25;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
         case 25:
            if(a[i]==' ' || a[i]=='\0')
            {
                state=26;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
         case 26:
            cout<<"friend is a keyword"<<endl;
            return 0;
        case 27:
            if(a[i]=='o')
            {
                state=28;
                i++;
            }
            else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 28:
            if(a[i]==' ' || a[i]=='\0')
            {
                state=29;
                i++;
            }
            else if(a[i]=='u')
            {
                state=30;
                i++;
            }
            else
            {
                state=fail(state);
                i=0;
            }
            break;
         case 29:
            cout<<"goto is a keyword"<<endl;
            return 0;
        case 30:
            if(a[i]=='b')
            {
                state=31;
                i++;
            }
            else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 31:
            if(a[i]=='l')
            {
                state=32;
                i++;
            }
            else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 32:
            if(a[i]=='e')
            {
                state=33;
                i++;
            }
            else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 33:
            if(a[i]==' ' || a[i]=='\0')
            {
                state=34;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 34:
            cout<<"double is a keyword"<<endl;
            return 0;
        case 35:
            if(a[i]=='r')
            {
                state=36;
                i++;
            }
            else if(a[i]=='h')
            {
                state=42;
                i++;
            }
            else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 36:
            if(a[i]=='y')
            {
                state=37;
                i++;
            }
            else if(a[i]=='u')
            {
                state=39;
                i++;
            }
            else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 37:
            if(a[i]==' ' || a[i]=='\0')
            {
                state=34;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 38:
            cout<<"try is a keyword"<<endl;
            return 0;
        case 39:
            if(a[i]=='e')
            {
                state=40;
                i++;
            }
            else
            {
                state=fail(state);
                i=0;
            }
            break;
       case 40:
            if(a[i]==' ' || a[i]=='\0')
            {
                state=41;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 41:
            cout<<"true is a keyword"<<endl;
            return 0;
        case 42:
            if(a[i]=='i')
            {
                state=43;
                i++;
            }
            else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 43:
            if(a[i]=='s')
            {
                state=44;
                i++;
            }
            else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 44:
            if(a[i]==' ' || a[i]=='\0')
            {
                state=45;
                i++;
            }
             else
            {
                state=fail(state);
                i=0;
            }
            break;
        case 45:
            cout<<"this is a keyword"<<endl;
            return 0;
        case 46:
                if (isalpha(a[i]) || a[i]=='_')
                {
                    state = 47;
                    i++;
                }
                else
                {
                    state = fail(state);
                    i = 0;
                }
                break;
        case 47:
                if (isalpha(a[i]) || isdigit(a[i]) || a[i]=='_')
                {
                    i++;
                }
                else if (a[i] == '\0')
                {
                    state = 48;
                    i++;
                }
                else
                {
                    state = fail(state);
                    i = 0;
                }
                break;
            case 48:
                cout << "It is an identifier" << endl;
                return 0;

            case 49:
                if (isdigit(a[i]))
                {
                    state = 50;
                    i++;
                }
                else
                {
                    state = fail(state);
                    i = 0;
                }
                break;
            case 50:
                if (isdigit(a[i]))
                {
                    i++;
                }
                else if (a[i] == '\0')
                {
                    state = 51;
                    i++;
                }
                else
                {
                    state = fail(state);
                    i = 0;
                }
                break;
            case 51:
                cout << "It is a constant" << endl;
                return 0;

            case 52:
                if (a[i] == '<')
                {
                    state = 53;
                    i++;
                }
                else if (a[i] == '>')
                {
                    state = 53;
                    i++;
                }
                else if (a[i] == '=')
                {
                    state = 53;
                    i++;
                }
                else if (a[i] == '!')
                {
                    state = 53;
                    i++;
                }
                else if (a[i] == '&')
                {
                    state = 54;
                    i++;
                }
                else if (a[i] == '|')
                {
                    state = 55;
                    i++;
                }
                else if (a[i] == '+')
                {
                    state = 53;
                    i++;
                }
                else if (a[i] == '-')
                {
                    state = 53;
                    i++;
                }
                else if (a[i] == '*')
                {
                    state = 53;
                    i++;
                }
                else if (a[i] == '/')
                {
                    state = 53;
                    i++;
                }
                else if (a[i] == '%')
                {
                    state = 53;
                    i++;
                }
                else
                {
                    state = fail(state);
                    i = 0;
                }
                break;
            case 53:
                if (a[i] == '\0')
                {
                    state = 57;
                    i++;
                }
                else if (a[i] == '=')
                {
                    state = 56;
                    i++;
                }
                else
                {
                    state = fail(state);
                    i = 0;
                }
                break;
            case 54:
                if (a[i] == '&')
                {
                    state = 56;
                    i++;
                }
                else if(a[i] == '\0')
                {
                    state = 57;
                    i++;
                }
                else
                {
                    state = fail(state);
                    i = 0;
                }
                break;
            case 55:
                if (a[i] == '|')
                {
                    state = 56;
                    i++;
                }
                else if(a[i] == '\0')
                {
                    state = 57;
                    i++;
                }
                else
                {
                    state = fail(state);
                    i = 0;
                }
                break;
            case 56:
                if (a[i]=='\0') {
                    state = 57;
                    i++;
                }
                else
                {
                    state = fail(state);
                }
                break;
            case 57:
                cout << "It is an operator" << endl;
                return 0;
            case 58:
                cout << "It is not a token" << endl;
                return 0;
        }
    }
}
