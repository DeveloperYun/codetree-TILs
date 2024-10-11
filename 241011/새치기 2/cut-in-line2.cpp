#include <iostream>
#include <vector>
#include <deque>
#include <unordered_map>

using namespace std;

int main() {
    int N, M, Q;
    cin >> N >> M >> Q;

    vector<deque<string>> lines(M); // 각 줄을 관리할 deque
    unordered_map<string, int> person_line; // 사람 이름과 그가 속한 줄을 매핑

    vector<string> people(N);
    for (int i = 0; i < N; ++i) {
        cin >> people[i];
        int line_idx = i / (N / M); // 각 사람을 적절한 줄에 분배
        lines[line_idx].push_back(people[i]);
        person_line[people[i]] = line_idx;
    }

    for (int i = 0; i < Q; ++i) {
        int type;
        cin >> type;

        if (type == 1) {
            string a, b;
            cin >> a >> b;
            int line_a = person_line[a];
            int line_b = person_line[b];

            if (line_a != line_b) {
                // a를 제거하고 b 앞에 삽입
                for (auto it = lines[line_a].begin(); it != lines[line_a].end(); ++it) {
                    if (*it == a) {
                        lines[line_a].erase(it);
                        break;
                    }
                }
                for (auto it = lines[line_b].begin(); it != lines[line_b].end(); ++it) {
                    if (*it == b) {
                        lines[line_b].insert(it, a);
                        break;
                    }
                }
                person_line[a] = line_b;
            }
        } else if (type == 2) {
            string a;
            cin >> a;
            int line_a = person_line[a];

            // a를 줄에서 제거
            for (auto it = lines[line_a].begin(); it != lines[line_a].end(); ++it) {
                if (*it == a) {
                    lines[line_a].erase(it);
                    break;
                }
            }
            person_line.erase(a); // person_line 에서도 제거
        } else if (type == 3) {
            string a, b, c;
            cin >> a >> b >> c;
            int line_a = person_line[a];
            int line_c = person_line[c];

            // a부터 b까지 통째로 c 앞에 이동
            deque<string> moving_people;
            bool collect = false;
            for (auto it = lines[line_a].begin(); it != lines[line_a].end();) {
                if (*it == a) collect = true;
                if (collect) {
                    moving_people.push_back(*it);
                    it = lines[line_a].erase(it);
                    if (*it == b) break;
                } else {
                    ++it;
                }
            }

            for (auto it = lines[line_c].begin(); it != lines[line_c].end(); ++it) {
                if (*it == c) {
                    for (auto &person : moving_people) {
                        lines[line_c].insert(it, person);
                        person_line[person] = line_c;
                    }
                    break;
                }
            }
        }
    }

    // 결과 출력
    for (int i = 0; i < M; ++i) {
        if (lines[i].empty()) {
            cout << "-1" << endl;
        } else {
            for (auto &person : lines[i]) {
                cout << person << " ";
            }
            cout << endl;
        }
    }

    return 0;
}