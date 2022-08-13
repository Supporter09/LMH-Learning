// Bai 2: Tim so nguyen duong nho nhat chua xuat hien trong mang

// #include <bits/stdc++.h>
// using namespace std;

// int cnt[1000002];

// int main(){
// 	int TC; cin >> TC;
// 	while(TC--){
// 		int n; cin >> n;
// 		memset(cnt,0,sizeof(cnt));
// 		for(int i=0; i<n; i++){
// 			int x; cin >> x;
// 			if(x > 0) cnt[x] = 1;
// 		}
// 		for(int i = 1 ; i <= 1000001; i++){
// 			if(cnt[i] == 0){
// 				cout << i << endl;
// 				break;
// 			}
// 		}
// 	}
// 	return 0;
// }


// Bai 3: Khoang cach nho nhat giua 2 so trong mang

#include <bits/stdc++.h>
using namespace std;

int main(){
	int TC; cin >> TC;
	while(TC--){
		int n; cin >> n;
		int a[n];
		for(int i = 0; i < n; i++){
			cin >> a[i];
		}
		sort(a, a+n)
	}
	return 0;
}