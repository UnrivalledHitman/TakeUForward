// Check whether someone is an adult or not
// Name = Indrajeet Mondal; Date = 3rd July 2024
// SourceCode

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int age;

    cout << "Enter your age:- ";
    cin >> age;

    if (age >=  18)
    {
        cout << "You are an adult." << endl;
    }
    else
    {
        cout << "You are not an adult." << endl;
    }

    return 0;
}