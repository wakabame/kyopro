
#include <bits/stdc++.h>
using namespace std;

int main(void)
{
    int N;
    cin >> N;
    vector<pair<int, int>> p(N);
    for (auto& [x, y] : p) {
        cin >> x >> y;
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < i; j++) {
            for (int k = 0; k < j; k++) {
                auto [x1, y1] = p[i];
                auto [x2, y2] = p[j];
                auto [x3, y3] = p[k];
                x2 -= x1;
                y2 -= y1;
                x3 -= x1;
                y3 -= y1;
                if (x2 * y3 == x3 * y2){
                    cout << "Yes" << endl;
                    return 0;
                }
            }
        }
    }

    cout << "No" << endl;
    return 0;
}