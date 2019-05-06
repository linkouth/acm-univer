#include <iostream>
#include <queue>
#include <vector>

using namespace std;

void dfs(int v, vector<bool>& used, vector< vector <int> >& g, vector<int>& ans) {
	used[v] = true;
	for (size_t i = 0; i<g[v].size(); ++i) {
		int to = g[v][i];
		if (!used[to])
			dfs(to, used, g, ans);
	}
	ans.push_back(v);
}

void topological_sort(int n, vector<bool>& used, vector< vector <int> >& g, vector<int>& ans) {
	for (int i = 0; i < n; ++i)
		used[i] = false;
	ans.clear();
	for (int i = 0; i<n; ++i)
		if (!used[i])
			dfs(i, used, g, ans);
	reverse(ans.begin(), ans.end());
}

int main()
{
	int N;
	cin >> N;
	vector< vector <int> > g(N, vector<int>());

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			int tmp;
			cin >> tmp;
			if (tmp) {
				g[i].push_back(j);
			}
		}
	}

	vector<bool> used(N);
	vector<int> path(N);
	vector<int> ans;

	topological_sort(N, used, g, ans);
	for (int i = 0; i < ans.size(); ++i) {
		cout << ans[i] + 1 << ' ';
	}
	cout << '\n';

	return 0;
}
