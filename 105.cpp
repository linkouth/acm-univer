#include <iostream>
#include <vector>
#include <pair>

using namespace std;

const int INF = INT32_MAX;

const int MAXN = 1000;
vector < vector < int > > g(MAXN, vector<int> ());
vector < pair<int, int> > ans;
bool used[MAXN];
int timer, tin[MAXN], fup[MAXN];

void dfs (int v, int p = -1) {
	used[v] = true;
	tin[v] = fup[v] = timer++;
	for (size_t i=0; i<g[v].size(); ++i) {
		int to = g[v][i];
		if (to == p)  continue;
		if (used[to])
			fup[v] = min (fup[v], tin[to]);
		else {
			dfs (to, v);
			fup[v] = min (fup[v], fup[to]);
			if (fup[to] > tin[v])
				IS_BRIDGE(v,to);
		}
	}
}

void find_bridges() {
	timer = 0;
	for (int i=0; i<n; ++i)
		used[i] = false;
	for (int i=0; i<n; ++i)
		if (!used[i])
			dfs (i);
}

int int main() {
	int n, m;
	cin >> n >> m;

	for (size_t i = 0; i < n; i++) {
		int a, b;
		cin >> a >> b;
		a--; b--;
		g[a].push_back(b);
		g[b].push_back(a);
	}

	for (size_t i = 0; i < n; i++) {
		for (size_t j = 0; j < g[i].size(); j++) {
			cout << g[i][j] << ' ';
		}
		cout << '\n';
	}

	return 0;
}
