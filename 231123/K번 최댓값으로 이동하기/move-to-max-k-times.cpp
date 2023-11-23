#include <iostream>
#include <queue>
using namespace std;
#define max_nk 100

int n, k;
int si, sj;
int cur_max;
int cur_num;
int di[4] = { 1, 0, -1, 0 };
int dj[4] = { 0,1, 0, -1 };
int matrix[max_nk][max_nk];
bool visited[max_nk][max_nk];
queue<pair<int, int>> q;

void clear() {
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			visited[i][j] = false;
		}
	}
}
bool InRange(int i, int j) {
	return 0 <= i && i < n && 0 <= j && j < n;
}

bool CanGo(int i, int j) {
	if (InRange(i, j) && !visited[i][j]) {
		return true;
	}
	return false;
}

void BFS(int i, int j) {
	q.push({ i, j });
	cur_max = 0;
	int sum = 0;

	while (!q.empty()) {

		pair<int, int> p = q.front();
		int cur_i = p.first;
		int cur_j = p.second;
		++sum;
		q.pop();
		if (matrix[cur_i][cur_j] > cur_max && sum != 1) {
			cur_max = matrix[cur_i][cur_j];
			si = cur_i;
			sj = cur_j;
		}
		else if (matrix[cur_i][cur_j] == cur_max) {
			if (cur_i < si) {
				si = cur_i;
				sj = cur_j;
			}
			else if (cur_i == si) {
				if (cur_j < sj) {
					si = cur_i;
					sj = cur_j;
				}
			}
		}

		for (int z = 0; z < 4; ++z) {
			int ni = cur_i + di[z];
			int nj = cur_j + dj[z];
			if (CanGo(ni, nj) && cur_num>matrix[ni][nj]) {
				q.push({ni, nj});
                visited[cur_i][cur_j] = true;

			}
		}
	}
}
int main() {
	cin >> n >> k;

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			cin >> matrix[i][j];
		}
	}

	cin >> si >> sj;
	si--; sj--;
	for (int i = 0; i < k; ++i) {
		cur_num = matrix[si][sj];
		BFS(si, sj);
		clear();
	}
	cout << si+1 << " " << sj+1;
}