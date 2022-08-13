#include <bits/stdc++.h>
using namespace std;

int N, X[100], col[100], down[100], up[100];
int a[100][100];

void printResult(){
	memset(a, 0, sizeof(a));

	for(int i = 1; i <= N; i++){
		a[i][X[i]] = 1;
		cout<< "Con hau o hang " << i << " cot " << X[i] << " "; 
		cout<< '\n';
	}
	for(int i = 1; i <=N; i++){
		for(int j = 1; j <= N; j++){
			cout << a[i][j] << " ";
		}
		cout << endl;
	}
	cout<<'\n';
	cout<<'\n';
}

void Try(int i) {
	// Duyet tat ca vi tri co the dat queen tren 1 row
	for(int j = 1; j <= N; j++){
		// Kiem tra col, 2 duong cheo xem co thoa man khong
		if(col[j] == 1 && down[i-j+N] == 1 && up[i+j-1] == 1){
			X[i] = j;
			col[j] = down[i-j+N] = up[i+j-1] = 0;
			if(i == N) {
				printResult();
			} else {
				Try(i+1);
			}
			// back track
			col[j] = down[i-j+N] = up[i+j-1] = 1;
 		}
	}
}

int main(){
	// freopen("input.txt","r",stdin);
	// freopen("output.txt", "w", stdout);
	cin  >> N;
	X[0] = 0;
	for(int i=1; i <= 100; i++){
		col[i] = down[i] = up[i] = 1;
	}
	Try(1);
	return 0;
}