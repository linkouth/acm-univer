#include <iostream>
#include <vector>
#include <set>

using namespace std;

const int INF = INT32_MAX;

int main()
{
	int n, m;
	cin >> n >> m;
	vector < vector<int> > g(n, vector <int> (n, INF));

	for (int i = 0; i < m; ++i) {
		int a, b, cost;
		cin >> a >> b >> cost;
		a--; b--;
		g[a][b] = cost;
	}

	// алгоритм
	vector<bool> used (n);
	vector<int> min_e (n, INF), sel_e (n, -1);
	min_e[0] = 0;
	for (int i = 0; i < n; ++i) {
		int v = -1;
		for (int j=0; j<n; ++j)
			if (!used[j] && (v == -1 || min_e[j] < min_e[v]))
				v = j;

		used[v] = true;

		for (int to = 0; to < n; ++to)
			if (g[v][to] < min_e[to]) {
				min_e[to] = g[v][to];
				sel_e[to] = v;
			}
	}

	int sum = 0;
	for (size_t i = 0; i < min_e.size(); ++i) {
		if (min_e[i] != INF) {
			sum += min_e[i];
		}
	}
	cout << sum << '\n';

	for (size_t i = 0; i < sel_e.size(); ++i) {
		if (sel_e[i] != -1) {
			cout << sel_e[i] + 1 << " " << i + 1 << endl;
		}
	}

	return 0;
}
