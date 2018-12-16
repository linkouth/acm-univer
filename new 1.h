248
#include <iostream> 
#include <vector> 
using namespace std; 

vector<int> res; 

void CountingSort(vector<pair<long, long>> a) 
{ 
	vector<long> c(200000, -1); 
	for (int i = 0; i < a.size(); i++) 	{ 
		c[a[i].first + 100000] = a[i].second; 
	} 
	for (int j = 0; j < c.size(); j++) { 
		if (c[j] != -1) { 
			res.push_back(c[j]); 
		} 
	} 
} 


int main() 
{ 
	long x, y; 
	int n; 
	cin » n; 
	vector<vector<pair<long, long>> a(200000); 

	for (int i = 1; i <= n; i++) { 
		cin » x » y; 
		a[x + 100000].push_back(make_pair(y, i)); 
	} 
	for (int i = 0; i < 200000; i++) { 
		if (!a[i].empty()) { 
			CountingSort(a[i]); 
			for (int j = 0; j < res.size(); j++) 
				cout << res[j] << " "; 
			res.clear(); 
		} 
	} 
	return 0; 
}

249
 
#include<iostream> 
#include<vector> 

using namespace std; 

void quickSort(vector<int>& a, int l, int r) { 
	int x, i = l, j = r; 
	x = a[(l + r) / 2]; 
	while (i <= j) { 
		while (a[i] < x) i++; 
		while (x < a[j]) j--; 
		if (i <= j) { 
			swap(a[i], a[j]); 
			i++; j--; 
		} 
	} 
	if (l<j) quickSort(a, l, j); 
	if (i<r) quickSort(a, i, r); 
}
 
bool sum(vector<int> a, vector<int> b, int x) { 
	int i = 0, j = b.size() - 1; 
	while (a[i] + b[j] != x && i != a.size() - 1 && j != 0) { 
		while (j > 0 && a[i] + b[j] > x) j--; 
		while (i < a.size() - 1 && a[i] + b[j] < x) i++; 
	} 
	while (j > 0 && a[i] + b[j] > x) j--; 
	while (i < a.size() - 1 && a[i] + b[j] < x) i++; 
	if (a[i] + b[j] == x) 
		return true; 
	return false; 
} 
int main() { 
	int n, m, k; 
	scanf_s("%d", &n); 
	vector<int>a(n); 
	for (int i = 0; i < n; i++) 
		scanf_s("%d", &a[i]); 
	scanf_s("%d", &m); 
	vector<int>b(m); 
	for (int i = 0; i < m; i++) 
		scanf_s("%d", &b[i]); 
	scanf_s("%d", &k); 
	if (k == 0) 
		return 0; 
	if (n == 0 || m == 0) { 
		for(int i = 0; i<k; i++) 
			printf("%s\n", "NO"); 
		return 0; 
	} 
	vector<int>c(k); 
	for (int i = 0; i < k; i++) 
		scanf_s("%d", &c[i]); 
	quickSort(a, 0, n-1); 
	quickSort(b, 0, m-1); 
	cout « endl; 
	for (int i = 0; i < k; i++) 
		if (sum(a, b, c[i])) 
			printf("%s\n", "YES"); 
		else
			printf("%s\n", "NO"); 
	return 0; 
}
 
250
 
#include <iostream» 
#include <vector> 
#include <algorithm> 



using namespace std; 
vector <pair<int, int>> merge(vector <pair<int, int>> a, vector <pair<int, int>> b, vector <pair<int, int>> &c)
 { 
	int n = a.size(), m = b.size(), ita = 0, itb = 0; 
	for (int itc = 0; itc < n + m; itc++) { 
		if (ita < n && (itb == m || a[ita].first < b[itb].first)) { 
			c[itc].first = a[ita].first; 
			c[itc].second = a[ita++].second; 
		} 
		else if (ita < n && (itb == m || (a[ita].first == b[itb].first && a[ita].second < b[itb].second))) { 
			c[itc].first = a[ita].first; 
			c[itc].second = a[ita++].second; 
		} 
		else { 
			c[itc].first = b[itb].first; 
			c[itc].second = b[itb++].second; 
		} 
	} 
	return c; 
} 

vector <pair<int, int» merge_sort(vector <pair<int, int» &a)
{ 
	if (a.size() <= 1)
		return a; 
	vector <pair<int, int>> l, r; 
	for (int i = 0; i < a.size() / 2; i++) 
		l.push_back(a[i]); 
	for (int i = a.size() / 2; i < a.size(); i++) 
		r.push_back(a[i]); 
	l = merge_sort(l); 
	r = merge_sort(r); 
	return merge(l, r, a); 
} 


int main() 
{ 
	int n; 
	cin >> n; 
	vector <pair <int, int>> a(n); 
	for (int i = 0; i < n; i++) 
		cin >> a[i].first >> a[i].second; 
	vector <pair<int, int» c; 
	for (int i = 0; i < n; i++) { 
		c.push_back(make_pair(a[i].first, 0)); 
		c.push_back(make_pair(a[i].second, 1)); 
	} 
	merge_sort(c); 
	int k = 0, count = 0; 
	for (int i = 0; i < 2 * n; i++) { 
		if (c[i].second == 0) 
			count++; 
		if (count > k) 
			k = count; 
		if (c[i].second == 1) 
			count--; 
	} 

	count = 0; 
	int result = 0; 
	int f = 0, d = 0; 
	for (int i = 0; i < 2 * n; i++) { 
		if (c[i].second == 0) 
			count++; 
		if (k == count) { 
			if (c[i].second == 0) 
				f = c[i].first; 
		} 
		if (k == count) { 
			if (c[i].second == 1) { 
				d = c[i].first; 
				result += d - f + 1; 
			} 
		} 
		if (c[i].second == 1) 
			count--; 
	} 
	cout << result << endl; 

	return 0; 
}
 
406
 
#include <iostream> 
#include <iomanip> 

using namespace std; 

double s, m, p, i = 0; 

double f(double s, double m, double p, double x) 
{ 
	for (int i = 0; i < m; i++) 
		s += s * p / 100 - x; 
	return s; 
} 

double bsearch(double s, double m, double p, double l, double r) 
{ 
	while (i < 100) { 
		double mid = (l + r) / 2; 
		if(f(s, m, p, mid) >= 0) 
			l = mid; 
		else 
			r = mid; 
		i++; 
	} 
	return (l + r) / 2; 
} 

int main() 
{ 
	cin >> s >> m >> p; 
	double l = 0, r = (s * p / 100) + s; 
	cout << fixed << setprecision(5) << bsearch(s, m, p, l, r) << endl; 
	return 0; 
}
 
407
 
#include <iostream> 
#include <iomanip> 
#include <cmath> 

using namespace std; 

double c, t; 
int i = 0; 

bool f(int c, int t, double x) 
{ 
	double time = c * x * log(x) / log(2.0); 
	return time <= t; 
} 

double bsearch(double c, double t) 
{ 
	double l = 0, r = 1000000; 
	while (i < 100) { 
		double mid = (l + r) / 2; 
		if (f(c, t, mid)) 
			l = mid; 
		else 
			r = mid; 
		i++; 
	} 
	return (l + r) /2; 
} 

int main() 
{ 
	cin » c » t; 
	cout « fixed « setprecision(9) « bsearch(c, t) « endl; 
	return 0; 
}