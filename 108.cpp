#include <iostream>
#include <vector>

using namespace std;

const int INF = INT32_MAX;

int main()
{
	int N, M, v1, v2;
	cin >> N >> M >> v1 >> v2;
	v1--; v2--;

	vector < vector < pair<int, int> > > g(N);
	
	for (int i = 0; i < M; ++i) {
		int start, end, length;
		cin >> start >> end >> length;
		start--; end--;
		g[start].push_back(make_pair(end, length));
		g[end].push_back(make_pair(start, length));
	}

	vector<int> d(N, INF);
	d[v1] = 0;
	vector<char> u(N);
	for (int i = 0; i < N; ++i) {
		int v = -1;
		for (int j = 0; j < N; ++j)
			if (!u[j] && (v == -1 || d[j] < d[v]))
				v = j;
		if (d[v] == INF)
			break;
		u[v] = true;

		for (size_t j = 0; j<g[v].size(); ++j) {
			int to = g[v][j].first,
				len = g[v][j].second;
			if (d[v] + len < d[to]) {
				d[to] = d[v] + len;
			}
		}
	}

	if (d[v2] < INF) {
		cout << d[v2] << '\n';
	}
	else {
		cout << -1 << '\n';
	}

	/*for (int i = 0; i < N; ++i) {
		cout << i << ": ";
		for (auto pair : g[i]) {
			cout << pair.first << ' ' << pair.second;
		}
		cout << '\n';
	}*/

}
