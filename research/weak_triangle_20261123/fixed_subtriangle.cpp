// Test every extension of a fixed subtriangle, charging each L at its last cell.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using Edge = std::array<int, 3>;
using Pair = std::array<int, 2>;

int index_at(int x, int y) {
    return x * (x - 1) / 2 + y;
}

class ExtensionSearch {
    int budget;
    std::vector<int> slots;
    std::vector<int> order;
    std::vector<Edge> fixed_edges;
    std::vector<std::vector<Pair>> newly_completed;

    bool extend(size_t depth, int score) {
        ++nodes;
        if (depth == order.size()) return true;

        std::array<int, 3> gained{};
        for (const Pair& pair : newly_completed[depth]) {
            int a = coloring[pair[0]] - '0';
            int b = coloring[pair[1]] - '0';
            if (a == b) {
                gained[a] = budget + 1;
            } else {
                // The third color completes a rainbow. The other two give a bichromatic L.
                ++gained[3 - a - b];
            }
        }
        for (int c = 0; c < 3; ++c) {
            if (score + gained[c] > budget) continue;
            coloring[order[depth]] = char('0' + c);
            if (extend(depth + 1, score + gained[c])) return true;
        }
        return false;
    }

public:
    std::string coloring;
    std::uint64_t nodes = 0;

    ExtensionSearch(int n, int m, int a, int b, int limit)
        : budget(limit), coloring(index_at(n, 0), '?') {
        // Ranks -2 and -1 denote an unordered cell and a fixed cell, respectively.
        std::vector<int> rank(coloring.size(), -2);
        for (int x = 1; x < m; ++x) {
            for (int y = 0; y < x; ++y) {
                int cell = index_at(x + a + b, y + b);
                slots.push_back(cell);
                rank[cell] = -1;
            }
        }

        std::vector<Edge> edges;
        std::vector<std::vector<Pair>> incident(coloring.size());
        for (int x = 1; x < n; ++x) {
            for (int y = 0; y < x; ++y) {
                for (int d = 1; x + d < n; ++d) {
                    Edge edge{index_at(x, y), index_at(x + d, y), index_at(x + d, y + d)};
                    edges.push_back(edge);
                    for (int j = 0; j < 3; ++j) {
                        incident[edge[j]].push_back({edge[(j + 1) % 3], edge[(j + 2) % 3]});
                    }
                }
            }
        }

        while (order.size() + slots.size() < coloring.size()) {
            int chosen = -1;
            int highest = -1;
            for (size_t v = 0; v < coloring.size(); ++v) {
                if (rank[v] != -2) continue;
                int priority = 0;
                for (const Pair& pair : incident[v]) {
                    int assigned = (rank[pair[0]] != -2) + (rank[pair[1]] != -2);
                    priority += assigned == 2 ? 1000 : assigned;
                }
                if (priority > highest) {
                    highest = priority;
                    chosen = static_cast<int>(v);
                }
            }
            rank[chosen] = static_cast<int>(order.size());
            order.push_back(chosen);
        }

        newly_completed.resize(order.size());
        for (Edge edge : edges) {
            std::sort(edge.begin(), edge.end(), [&](int u, int v) { return rank[u] < rank[v]; });
            int last = rank[edge[2]];
            if (last < 0) fixed_edges.push_back(edge);
            else newly_completed[last].push_back({edge[0], edge[1]});
        }
    }

    bool contains_extension(const std::string& word, int declared_score) {
        if (word.size() != slots.size() || word.find_first_not_of("012") != std::string::npos) {
            throw std::invalid_argument("Malformed triangle word");
        }
        for (size_t i = 0; i < slots.size(); ++i) coloring[slots[i]] = word[i];

        int score = 0;
        for (const Edge& e : fixed_edges) {
            char a = coloring[e[0]], b = coloring[e[1]], c = coloring[e[2]];
            if (a == b && b == c) throw std::invalid_argument("Improper fixed triangle");
            score += a != b && b != c && c != a;
        }
        if (score != declared_score) throw std::invalid_argument("Wrong source rainbow count");
        return score <= budget && extend(0, score);
    }
};

int main(int argc, char** argv) {
    if (argc != 6) {
        std::cerr << "Usage: fixed_subtriangle HOST SOURCE CUTOFF HOST_BUDGET WORDS\n";
        return 2;
    }
    int host = std::stoi(argv[1]), source = std::stoi(argv[2]);
    int cutoff = std::stoi(argv[3]), budget = std::stoi(argv[4]);
    std::ifstream words(argv[5]);
    if (!words || source < 3 || host <= source || host > 18 || cutoff < 0 || budget < 0) return 2;
    std::vector<ExtensionSearch> placements;
    int gap = host - source;
    for (int a = 0; 3 * a <= gap; ++a) {
        for (int b = a; 2 * b <= gap - a; ++b) {
            placements.emplace_back(host, source, a, b, budget);
        }
    }

    std::uint64_t tested = 0;
    int cost;
    std::string word;
    while (words >> cost >> word) {
        if (cost > cutoff) continue;
        for (auto& layout : placements) {
            if (layout.contains_extension(word, cost)) {
                std::cout << "WITNESS " << layout.coloring << '\n';
                return 0;
            }
        }
        ++tested;
    }
    if (!words.eof() || tested == 0) return 2;
    std::uint64_t nodes = 0;
    for (const auto& layout : placements) nodes += layout.nodes;
    std::cout << "EXCLUDED " << tested << " " << placements.size() << " " << nodes << '\n';
}
