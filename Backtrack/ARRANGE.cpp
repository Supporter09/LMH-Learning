#include <bits/stdc++.h>
using namespace std;

int N, X[100], check[100];

void printResult(){
	for(int i =1; i <= N; i++){
		cout << X[i] << " ";
	}
	cout << '\n';
}

void Try(int i) {
	// Duyet tat ca kha nang co the cua X[i]
	for(int j = 1; j <= N; j++) {
		// Kiem tra xem X[i] gan duoc gia tri j khong
		if(check[j] == 0){
			check[j] = 1;
			X[i] = j;
			if( i == N) {
				printResult();
			} else {
				Try(i+1);
			}
			// backtrack
			check[j] = 0;
		}
	}
}

int main() {
	// freopen("input.txt","r",stdin);
	// freopen("output.txt", "w", stdout);
	cin >> N;
	X[0] = 0;
	memset(check,0,sizeof(check));
	Try(1);
	return 0;
}