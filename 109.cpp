#include <iostream>
#include <queue>
#include <vector>

using namespace std;

void dfs(int v, int finish, int from, vector<bool>& used, vector<int>& path, vector<vector<int>>& g) {
	if (used[v]) {
		return;
	}
	used[v] = true;
	path[v] = from;
	if (v == finish) {
		return;
	}
	for (vector<int>::iterator i = g[v].begin(); i != g[v].end(); ++i)
		dfs(*i, finish, v, used, path, g);
}

int main()
{
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

	vector<bool> used(N);
	vector<int> path(N);
	
	dfs(v1, v2, v1, used, path, g);

	if (!used[v2]) {
		cout << "-1";
		return 0;
	}
	


	vector<int> ans;
	for (int v = v2; v != v1; v = path[v])  // Ïðîõîäèì ïî ïóòè èç êîíöà â íà÷àëî
	{
		ans.push_back(v);  // Çàïîìèíàåì âåðøèíó
	}
	ans.push_back(v1);
	reverse(ans.begin(), ans.end());  // Ïåðåâîðà÷èâàåì ïóòü
	cout << ans.size() - 1 << '\n';
	for (int i = 0; i < ans.size(); ++i) {
		cout << ans[i] + 1 << ' ';
	}
	cout << '\n';

	return 0;
}
