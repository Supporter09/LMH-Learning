#include <bits/stdc++.h>
using namespace std;

int N, K, X[100];

void printResult() {
	for(int i=1; i <= K; i++){
		cout << X[i] << " ";
	};
	cout << '\n';
}

void Try(int i) {
	for(int j = X[i-1] + 1; j <= N-K+i ; j ++) {
		X[i] = j;
		if ( i == K ) {
			printResult();
		} else {
			Try(i + 1);
		}
	}
}

int main() {
	cin >> N >> K;
	X[0] = 0;
	Try(1);
}