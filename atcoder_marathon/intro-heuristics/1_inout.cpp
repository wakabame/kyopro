#include<bits/stdc++.h>
using namespace std;

const static int NUM_TYPE = 26;

int getFullScore(int D, const vector<int>& C, const vector<int>& T, const vector<vector<int>>& S) {
    int ret = 0;
    vector<int> last(NUM_TYPE, -1);
    for (int d = 0; d < D; d++) {
        const int j = T[d];
        last[j] = d ;
        for (int i = 0; i < NUM_TYPE; i++) {
            ret -= (d - last[i]) * C[i];
        }
        ret += S[d][j];
 
    // B 問題用の出力
    cout << ret << endl;
    }
    return ret;
}

int main(){
    int D;
    cin >> D;
    vector<int> C(NUM_TYPE);
    for (int &c : C) {
        cin >> c;
    }
    vector<vector<int>> S(D, vector<int>(NUM_TYPE));
    for (auto &s : S) {
        for (auto &x : s) {
            cin >> x;
        }
    }
    vector<int> T(D, -1);

    // B 問題用の初期解
    for (auto &t :T) {
        cin >> t;
        t--;
    }

    int fullscore = getFullScore(D, C, T, S);
    
    return 0;
}