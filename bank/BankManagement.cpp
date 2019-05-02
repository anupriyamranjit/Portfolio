#include <iostream>
#include <string>
using namespace std;

class User{
public:
  User(int aB):accountBalance(aB){
    serviceCharge = 10;
    cout << "Which account would you like to access 's' for saving and 'c' for checkings"<<endl;
    cin >> accountType;
    if(accountType == 'c'){
      cout << "You are in checking account"<< endl;
    }
    else{
      cout << "You are in the savings account"<< endl;
    }
    cout << "What would you like to do next"<<endl;

  }
  ~User(){
    cout <<"Thank you for your time"<< endl;
  }
  void takeService(){
    if(accountBalance< 100){
      accountBalance = accountBalance - serviceCharge;
      cout << "Service charge was taken your new balance is:"<< accountBalance << endl;
    }
  }


  void Deposit(){
    cout << "How much would you like to deposit"<<endl;
    cin >> depositAmount;
    accountBalance = accountBalance + depositAmount;
    MakeMenu();


  }

  void Withdraw(){
    cout << "How much would you like to withdraw"<<endl;
    cin >> withdrawAmount;
    accountBalance = accountBalance - withdrawAmount;
    cout << accountBalance << endl;
    takeService();
    MakeMenu();

  }

  void checkBalance(){
    cout << "Your Balance is: $"<<accountBalance<<endl;
    MakeMenu();
  }
  int exitMenu(){
    return 0;


  }

  void MakeMenu(){
    cout << "1.Deposit"<<endl;
    cout << "2.Withdraw"<<endl;
    cout << "3.Check Balance"<<endl;
    cout << "4.Exit"<<endl;
    cout << "Input number Below:"<<endl;
    int m;
    cin >> m;
    actionPicked(m);

  }
  void actionPicked(int m){
    if(m == 1){
      Deposit();
    }
    else if(m == 2){
      Withdraw();
    }
    else if(m == 3){
      checkBalance();
    }
    else if(m==4){
      exitMenu();
    }

  }


private:
  int nextAction;
  int accountBalance;
  int withdrawAmount;
  char accountType;
  int depositAmount;
  int minimumAmount;
  int serviceCharge;


};

int main(){
  User Anupriyam(1000);
  Anupriyam.MakeMenu();


}
