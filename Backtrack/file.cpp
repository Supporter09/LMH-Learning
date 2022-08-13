#include <bits/stdc++.h>
using namespace std;

int N, X[100];

void printResult(){
	for(int i = 1; i <= N; i++){
		cout << X[i];
	}
	cout << endl;
}

void Try(int i){
	// Duyet cac kha nang cua X[i]
	for(int j = 0; j <= 1; j++){
		X[i] = j;
		if(i == N){
			printResult();
		} else {
			Try(i+1);
		}
	}
}

int main(){
	// freopen('input.txt', 'r', stdin);
	// freopen('output.txt', 'w', stdout)
	cin >> N;
	Try(1);
	return 0;
}