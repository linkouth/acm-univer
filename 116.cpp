#include <iostream>
#include <vector>

using namespace std;

const int INF = INT32_MAX;

struct edge {
	int a, b, cost;
};

int min(int lhs, int rhs) {
	if (lhs < rhs) { return lhs; }
	return rhs;
}

vector< int > solve(int n, int m, vector< edge > e, int v = 0) {
	vector<int> d(n, INF);
	d[v] = 0;
	for (int i = 0; i < n - 1; ++i) {
		for (int j = 0; j < m; ++j)
			if (d[e[j].a] < INF)
				if (d[e[j].b] > d[e[j].a] + e[j].cost) {
					d[e[j].b] = min(d[e[j].b], d[e[j].a] + e[j].cost);
				}
	}

	return d;
}

int main()
{
	int n, m;
	cin >> n >> m;
	vector<edge> e;

	for (int i = 0; i < m; ++i) {
		edge edge;
		int a, b;
		cin >> a;
		cin >> b;
		edge.a = --a;
		edge.b = --b;
		cin >> edge.cost;
		e.push_back(edge);
	}

	vector< int > d = solve(n, m, e);

	for (size_t i = 1; i < d.size(); ++i) {
		if (d[i] == INF) {
			cout << "NO" << '\n';
		}
		else {
			cout << d[i] << '\n';
		}
	}

	return 0;
}
