#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main()
{
	/*int N = 5, v1 = 0, v2 = 4;
	vector< vector <int> > g = {
		{1, 2, 4},
		{0, 3, 4},
		{0, 4},
		{1, 4},
		{0, 1, 2, 3}
	};*/

	int N, v1, v2;
	cin >> N >> v1 >> v2;
	vector< vector <int> > g(N, vector<int>());
	v1--;
	v2--;

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			int tmp;
			cin >> tmp;
			if (tmp) {
				g[i].push_back(j);
			}
		}
	}

	queue<int> q;
	q.push(v1);
	vector<bool> used(N);
	vector<int> d(N), p(N);
	used[v1] = true;
	p[v1] = -1;
	while (!q.empty()) {
		int v = q.front();
		q.pop();
		for (size_t i = 0; i<g[v].size(); ++i) {
			int to = g[v][i];
			if (!used[to]) {
				used[to] = true;
				q.push(to);
				d[to] = d[v] + 1;
				p[to] = v;
			}
		}
	}

	if (!used[v2]) {
		cout << "-1";
		return 0;
	}
	cout << d[v2] << '\n';

	
		vector<int> path;
		for (int v = v2; v != -1; v = p[v])
			path.push_back(v);
		reverse(path.begin(), path.end());
		for (size_t i = 0; i<path.size(); ++i)
			cout << path[i] + 1 << " ";
	
	cout << '\n';

	return 0;
}
