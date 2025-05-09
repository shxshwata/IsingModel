#include <iostream>
#include <vector>
#include <numeric>
#include <random>
#include <chrono>
#include <cmath>
using namespace std;

void printLattice(const vector<vector<int>>& lattice) {
    for (const auto& row:lattice) {
        for (int val:row) {
            cout<<val<<" ";
        }
        cout<<endl;
    }
    cout<<endl;
}

int sumLattice(const vector<vector<int>>& lattice) {
    int sum=0;
    for (const auto& row:lattice) {
        sum+=accumulate(row.begin(),row.end(),0);
    }
    return sum;
}

int main() {
    int n;
    cout<<"Enter Lattice Size:"<<endl;
    cin>>n;

    vector<vector<int>> lattice_random(n,vector<int>(n));
    unsigned seed=chrono::system_clock::now().time_since_epoch().count();
    default_random_engine generator(seed);
    uniform_int_distribution<int> distribution(0,1);

    for (int i=0;i<n;++i) {
        for (int j=0;j<n;++j) {
            lattice_random[i][j]=2*distribution(generator)-1;
        }
    }

    cout<<"Initial Lattice:"<<endl;
    printLattice(lattice_random);
    int initialSum=sumLattice(lattice_random);
    cout<<"Initial Sum: "<<initialSum<<endl;

    const double KT=10.0;
    int totalSteps=100;

    for (int step=1;step<=totalSteps;++step) {
        uniform_int_distribution<int> indexDist(0,n-1);
        int ri=indexDist(generator);
        int rj=indexDist(generator);

        int beforeFlip=sumLattice(lattice_random);
        lattice_random[ri][rj]*=-1;
        int afterFlip=sumLattice(lattice_random);

        double deltaE=abs(afterFlip-initialSum);
        double P=exp(-deltaE/KT);

        cout<<"Step "<<step<<":"<<endl;
        cout<<"Flipped element at ("<<ri<<","<<rj<<")"<<endl;
        cout<<"Sum before flip: "<<beforeFlip<<endl;
        cout<<"Sum after flip: "<<afterFlip<<endl;
        cout<<"deltaE (absolute): "<<deltaE<<endl;
        cout<<"Probability P: "<<P<<endl;

        if (P>0.5) {
            cout<<"Flip accepted"<<endl;
        } else {
            cout<<"Flip rejected"<<endl;
        }

        cout<<endl;
    }

    cout<<"Final Lattice:"<<endl;
    printLattice(lattice_random);
    cout<<"Final Sum: "<<sumLattice(lattice_random)<<endl;

    return 0;
}