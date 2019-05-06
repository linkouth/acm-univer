#include <iostream>
#include <vector>

using namespace std;

int INF = 10000;

int min(int lhs, int rhs) {
	if (lhs < rhs) {
		return lhs;
	}
	return rhs;
}

int main()
{
	int N;
	cin >> N;
	/*vector< vector < int > > g(N, vector <int>(N));
	for (size_t i = 0; i < g.size(); ++i) {
		for (size_t j = 0; j < g[i].size(); ++j) {
			int tmp;
			cin >> tmp;
			g[i][j] = tmp;
		}
	}*/

	vector< vector < int > > d(N, vector <int>(N, INF));
	for (size_t i = 0; i < N; ++i) {
		for (size_t j = 0; j < N; ++j) {
			int tmp;
			cin >> tmp;
			if (tmp) { d[i][j] = tmp; }
		}
	}

	for (int k = 0; k < N; ++k)
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < N; ++j)
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);

	for (size_t i = 0; i < d.size(); ++i, cout << endl) {
		for (size_t j = 0; j < d[i].size(); ++j) {
			if (d[i][j] == INF) {
				cout << 0 << ' ';
			}
			else {
				cout << d[i][j] << ' ';
			}
		}
	}
}
