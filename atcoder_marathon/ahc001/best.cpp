#include <bits/stdc++.h>

using namespace std;
using namespace chrono;

// デバッグマクロここから
#define repi(itr, ds) for (auto itr = ds.begin(); itr != ds.end(); itr++)

// vector
template <typename T>
istream &operator>>(istream &is, vector<T> &vec) {
    for (T &x : vec) is >> x;
    return is;
}
// pair
template <typename T, typename U>
ostream &operator<<(ostream &os, pair<T, U> &pair_var) {
    os << "(" << pair_var.first << ", " << pair_var.second << ")";
    return os;
}
// vector
template <typename T>
ostream &operator<<(ostream &os, const vector<T> &vec) {
    os << "{";
    for (int i = 0; i < vec.size(); i++) {
        os << vec[i] << (i + 1 == vec.size() ? "" : ", ");
    }
    os << "}";
    return os;
}
// map
template <typename T, typename U>
ostream &operator<<(ostream &os, map<T, U> &map_var) {
    os << "{";
    repi(itr, map_var) {
        os << *itr;
        itr++;
        if (itr != map_var.end()) os << ", ";
        itr--;
    }
    os << "}";
    return os;
}
// set
template <typename T>
ostream &operator<<(ostream &os, set<T> &set_var) {
    os << "{";
    repi(itr, set_var) {
        os << *itr;
        itr++;
        if (itr != set_var.end()) os << ", ";
        itr--;
    }
    os << "}";
    return os;
}

#define DUMPOUT cerr

void dump_func() {
    DUMPOUT << endl;
}
template <class Head, class... Tail>
void dump_func(Head &&head, Tail &&... tail) {
    DUMPOUT << head;
    if (sizeof...(Tail) > 0) {
        DUMPOUT << ", ";
    }
    dump_func(std::move(tail)...);
}
#ifdef DEBUG_
#define DEB
#define dump(...)                                                              \
    DUMPOUT << "  " << string(#__VA_ARGS__) << ": "                            \
            << "[" << to_string(__LINE__) << ":" << __FUNCTION__ << "]"        \
            << endl                                                            \
            << "    ",                                                         \
        dump_func(__VA_ARGS__)
#else
#define DEB if (false)
#define dump(...)
#endif
// デバッグマクロここまで



uint32_t xor128() {
    static uint32_t x = 123456789;
    static uint32_t y = 362436069;
    static uint32_t z = 521288629;
    static uint32_t w = 88675123;
    uint32_t t;

    t = x ^ (x << 11);
    x = y; y = z; z = w;
    return w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));
}

double nextDouble() {
    return (xor128() + 0.5) * (1.0 / 4294967296.0);
}

class rectangle {
    public:
    int index, a, b, c, d;
    int x, y, r;
    long long score;
    rectangle(int index, int x, int y, int r);
};

struct modification {
    int operation_type;
    long long delta_score;
    bool need_validation;
};

rectangle::rectangle(int index,int x, int y, int r) :
    index(index), x(x), y(y), r(r),
    a(x), b(y), c(x+1), d(y+1) {}


bool valid_rectangle(rectangle& rect){
    if (rect.a < 0 || rect.a > rect.c || rect.c > 10000 || rect.b < 0 || rect.b > rect.d || rect.d > 10000){
        return false;
    }

    // 広告点を含まない場合が生じないようにする
    if(rect.a <= rect.x && rect.x < rect.c && rect.b <= rect.y && rect.y < rect.d) {
        return true;
    } else {
        return false;
    }

    return true;
}

bool has_intersect_rectangles(rectangle& rect1, rectangle& rect2){
    return max(rect1.a, rect2.a) <= min(rect1.c, rect2.c) && max(rect1.b, rect2.b) <= min(rect1.d, rect2.d);
}

bool valid_solution(vector<rectangle>& solution) {
    // それぞれのrectangleが面積正かつ画面外にはみ出していない
    for (int i = 0; i < solution.size(); i++) {
        if (valid_rectangle(solution[i]) == false){
            return false;
        }
    }

    // それぞれのrectangle同士が重なっていない
    for (int j = 0; j < solution.size(); j++) {
        for (int k = 0; k < j; k++) {
            if(has_intersect_rectangles(solution[j], solution[k]) == true){
                return false;
            }
        }
    }

    return true;
}

bool valid_overlap_changelog(vector<rectangle>& solution, vector<pair<int, rectangle>>& changelog){
    // changelog に含まれるrectangle が他の rectangle と overlap していないことを確認する
    for (auto& c : changelog) {
        for (int k = 0; k < solution.size(); k++) {
            if(c.first != k && has_intersect_rectangles(solution[c.first], solution[k]) == true){
                return false;
            }
        }
    }
    return true;
}

int overlap_number(vector<rectangle>& solution, int& rectangle_index, rectangle& rect){
    // rectangle が他の rectangle と overlap していないことを確認する
    for (int k = 0; k < solution.size(); k++) {
        if(rectangle_index != k && has_intersect_rectangles(solution[k], rect) == true){
            return k;
        }
    }
    return -1;
}

long long get_each_score(rectangle& rect, bool final_flag=false, int phase=1){
    int s = (rect.c - rect.a) * (rect.d - rect.b);
    long long M = max(rect.r, s);
    long long m = min(rect.r, s);
    long long bunbo = M*M;
    long long bunshi = m *(2*M -m);
    long long ans = 1e9 * bunshi/bunbo;

    rect.score = ans;
    return ans;
}

long long get_full_score(vector<rectangle>& solution, bool final_flag=false){
    long long total_score = 0;

    for (int i = 0; i < solution.size(); i++) {
        total_score += get_each_score(solution[i], final_flag);
    }

    return total_score;
}

void sort_solution_by_r(vector<rectangle>& solution){
    auto compare_by_r = [&](const rectangle& rect1, const rectangle& rect2) -> bool{
        return (rect1.r < rect2.r);
    };
    stable_sort(solution.begin(), solution.end(), [&](const rectangle& rect1, const rectangle& rect2) -> bool { return compare_by_r(rect1, rect2);});
}
void sort_solution_by_score(vector<rectangle>& solution){
    auto compare_by_score = [&](const rectangle& rect1, const rectangle& rect2) -> bool{
        return (rect1.score < rect2.score);
    };
    stable_sort(solution.begin(), solution.end(), [&](const rectangle& rect1, const rectangle& rect2) -> bool { return compare_by_score(rect1, rect2);});
}

void sort_solution_by_index(vector<rectangle>& solution){
    auto compare_by_index = [&](const rectangle& rect1, const rectangle& rect2) -> bool{
        return (rect1.index < rect2.index);
    };
    stable_sort(solution.begin(), solution.end(), [&](const rectangle& rect1, const rectangle& rect2) -> bool { return compare_by_index(rect1, rect2);});
}
vector<rectangle> initialize_solution(int& n, vector<int>& x, vector<int>& y, vector<int>& r, vector<pair<int, rectangle>>& changelog) {
    vector<rectangle> solution;
    changelog.clear();

    for(int i = 0; i < n; i++) {
        rectangle rect = rectangle(i, x.at(i), y.at(i), r.at(i));
        solution.push_back(rect);
    }

    return solution;
}

void modify_rectangle(rectangle& rect, int& direction, int width){
    if (direction == 0){
        rect.a -= width;
    } else if (direction == 1){
        rect.b -= width;
    } else if (direction == 2){
        rect.c += width;
    } else if (direction == 3){
        rect.d += width;
    }

}
modification try_modify_solution(vector<rectangle>& solution, vector<pair<int, rectangle>>& changelog, int& phase, int force_index=-1,bool worst_ten_flag=false, int previous_operation_type=-1) {
    bool need_validation = false; // 長方形のoverlapが生じえる変更なら、trueにする
    int operation_valiety = 1 + phase * 4;
    int operation_type = operation_valiety * nextDouble();
    long long delta_score = 0;
    int rectangle_index = xor128() % solution.size();
    if(worst_ten_flag) {
        rectangle_index = xor128() %10;
    }
    if(force_index > -1){
        rectangle_index = force_index;
    }
    if(previous_operation_type == 4){
        operation_type = 4;
    }
    rectangle modified_rectangle = solution[rectangle_index];

    if( operation_type == 0){
        int rng = 4 * nextDouble();
        modify_rectangle(modified_rectangle, rng, +1);
        need_validation = true;
    } else if ( operation_type == 1){
        int rng = 4 * nextDouble();
        modify_rectangle(modified_rectangle, rng, -1);
    } else if ( operation_type == 2){
        // 広告が四隅に来るようにする
        int rng = 4 * nextDouble();
        if (rng == 0){
            // 左端に広告が来る
            int w = modified_rectangle.x - modified_rectangle.a;
            modified_rectangle.b += w;
            modified_rectangle.d += w;
        } else if (rng == 1){
            // 上端に広告が来る
            int h = modified_rectangle.y - modified_rectangle.b;
            modified_rectangle.a += h;
            modified_rectangle.c += h;
        } else if (rng == 2){
            // 右端に広告が来る
            int w = modified_rectangle.x - modified_rectangle.c + 1;
            modified_rectangle.b += w;
            modified_rectangle.d += w;
        } else if (rng == 3){
            // 下端に広告が来る
            int h = modified_rectangle.y - modified_rectangle.d + 1;
            modified_rectangle.a += h;
            modified_rectangle.c += h;
        }
        need_validation = true;
    } else if ( operation_type == 3){
        // どこかに伸びて、どこかに縮む
        int rng1 = 4 * nextDouble();
        int rng2 = 4 * nextDouble();
        if(rng1 == rng2) {
            return {3, 0, false};
        }
        modify_rectangle(modified_rectangle, rng1, +1);
        modify_rectangle(modified_rectangle, rng2, -1);
        need_validation = true;
    } else if ( operation_type == 4){
        // やけくそその１
        int radius = 2 * sqrt(modified_rectangle.r);
        modified_rectangle.a = modified_rectangle.x;
        modified_rectangle.b = modified_rectangle.y;
        modified_rectangle.c = modified_rectangle.x + 1;
        modified_rectangle.d = modified_rectangle.y + 1;
        if(nextDouble() < 0.5) {
            modified_rectangle.a -= radius * nextDouble();
        } else {
            modified_rectangle.c += radius * nextDouble();
        }
        if(nextDouble() < 0.5) {
            modified_rectangle.b -= radius * nextDouble();
        } else {
            modified_rectangle.d += radius * nextDouble();
        }
        need_validation = true;
    }

    if(valid_rectangle(modified_rectangle) == false) {
        return {-1, 0, false};
    }
        // スコア変動の計算
        delta_score += get_each_score(modified_rectangle, phase);
        delta_score -= solution[rectangle_index].score;
    changelog.push_back({rectangle_index, modified_rectangle});
    return {operation_type, delta_score, need_validation};

}
modification modify_solution(vector<rectangle>& solution, vector<pair<int, rectangle>>& changelog, int&phase) {
    changelog.clear();

    if (nextDouble() < 0.9) { // この値をチューニングするだけで向上しそう
        modification modi = try_modify_solution(solution, changelog, phase);
        return modi;
    } else {
        // modi1は成績悪いヤツ（やけくそする）。modi2は変動によってoverlapするもの
        modification modi1 = try_modify_solution(solution, changelog, phase, -1, true, 4);
        int overlap_index = overlap_number(solution, changelog[0].first, changelog[0].second);
        if (overlap_index == -1){
            return modi1;
        }
        modification modi2 = try_modify_solution(solution, changelog, phase, overlap_index, false, modi1.operation_type);
        return {min(modi1.operation_type, modi2.operation_type),
        modi1.delta_score + modi2.delta_score, modi1.need_validation || modi2.need_validation};
    }
}


void output_result(vector<rectangle>& solution){
    for (int i = 0; i < solution.size(); i++) {
        cout << solution[i].a << " " << solution[i].b << " " << solution[i].c << " " << solution[i].d << endl;
        // dump(solution[i].r, get_each_score(solution[i]));
    }
    return;
}

int main() {
    auto start = system_clock::now();
    vector<pair<int, rectangle>> changelog;

    //  入力
    int n;
    cin >> n;
    vector<int> x(n);
    vector<int> y(n);
    vector<int> r(n);

    for (int i = 0; i < n; i++) {
        cin >> x.at(i) >> y.at(i) >> r.at(i);
    }

    // 初期解の作成
    vector<rectangle> solution = initialize_solution(n, x, y, r, changelog);
    #ifdef DEBUG_
    sort_solution_by_index(solution);
    start = system_clock::now();
    output_result(solution);
    cout << "score: " << get_full_score(solution, true) << endl;
    #endif

    long long score = get_full_score(solution);
    long long old_score;
    long long score_desent;
    dump(score);
    double time = 0.0;
    double old_time = duration_cast<microseconds>(system_clock::now() - start).count() * 1e-6;
    double duration;
    double anneal_limit_time = 4.9;
    double limit_time = 4.99;
    int phase = 0;
    const double BEGIN_TEMP = 500000;
    const double END_TEMP = 10;
    double temp = BEGIN_TEMP;

    bool update; // 解の変更を受け入れるか

    long long step;
    for (step = 0; time < limit_time; step++) {
        if (step % 16384 == 0) {
            time = duration_cast<microseconds>(system_clock::now() - start).count() * 1e-6;
            score_desent = score - old_score;
            duration = time - old_time;
            // 次のループで時間を超過しそうなら終了させる
            if(time + 1.5 * duration > limit_time){
                break;
            }

            dump(time, step, score/n);
            if(phase == 0 && time > 1){
                phase = 1;
            }
            old_score = score;
            old_time = time;
            const double progressRatio = min(time / anneal_limit_time, 1.0);
            temp = BEGIN_TEMP + (END_TEMP - BEGIN_TEMP) * progressRatio;
            sort_solution_by_score(solution);
        }

        modification modi = modify_solution(solution, changelog, phase);

        update = (modi.operation_type!=-1) && (exp(modi.delta_score / temp) > nextDouble());

        if (update) {
            // 実際に変更する
            for(auto& c : changelog) {
                swap(solution[c.first], c.second);
            }

            if (modi.need_validation && !valid_overlap_changelog(solution, changelog)){
                for(auto& c : changelog) {
                    swap(solution[c.first], c.second);

                }
            } else {
                score += modi.delta_score;
            }
        }
    }


    sort_solution_by_score(solution);
    for(int i=0; i<solution.size(); i++){
        dump(solution[i].index, solution[i].score);
    }
    sort_solution_by_index(solution);
    output_result(solution);
    dump(time, step, get_full_score(solution, true)/n);
    cerr << "score: " << score/n << endl;
    cerr << "step: " << step << endl;
    cerr << "last score decent: " << score_desent << endl;
    cerr << "last interval duration: " << duration << endl;

    return 0;
}
