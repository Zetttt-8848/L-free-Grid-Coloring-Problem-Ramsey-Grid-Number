// Exhaustive fixed-boundary test for one/two-cell nonincreasing repairs.
//
// Build: c++ -O3 -std=c++17 search.cpp -o /tmp/cube_pair_search
// Run:   /tmp/cube_pair_search --mark 2 --output /tmp/pair_search.json
//
// Every proper Q coloring is generated without symmetry reduction. Each of
// the 256 assignments to the eight external cells is represented by one bit
// in a four-word bitset. Reverse propagation from Phi_Q=4 targets intersects
// the receiving coloring's legal-boundary set: each propagated bit therefore
// represents paths with one fixed boundary assignment, never mixed boundaries.
// The selected counterexample is checked again by a forward closure.
//
// No solver, external library, or precomputed state file is used. This proves
// only finite statements for Q and the requested added mark. Progress is sent
// to stderr; JSON goes to stdout unless --output is specified.

#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>

namespace {
using Word = std::uint32_t;
using BoundarySet = std::array<std::uint64_t, 4>;
using Cell = std::pair<int, int>;
const std::vector<int> Q{0, 1, 5, 6, 25, 26, 30, 31};
std::vector<Cell> q_cells, a_cells;
std::vector<Word> fibers, states, flip_masks;
std::vector<std::vector<Word>> incident(28);
std::vector<int> search_order, potentials, internal_map, external_map;
std::unordered_map<Word, int> state_index;
std::vector<std::vector<int>> reverse_edges;
std::vector<BoundarySet> allowed, reached;
std::uint64_t reverse_edge_count = 0;

int phi(Word state) {
    int result = 0;
    for (Word fiber : fibers) {
        const int imbalance = __builtin_popcount(fiber)
            - 2 * __builtin_popcount(state & fiber);
        result += imbalance * imbalance;
    }
    return result;
}

bool contains(const BoundarySet& set, int boundary) {
    return ((set[boundary / 64] >> (boundary % 64)) & 1) != 0;
}

void enumerate(int depth, Word assigned, Word state) {
    if (depth == 28) { states.push_back(state); return; }
    const int cell = search_order[depth];
    const Word bit = Word{1} << cell;
    const Word next_assigned = assigned | bit;
    for (int color = 0; color < 2; ++color) {
        const Word next = state | (color ? bit : 0);
        bool proper = true;
        for (Word corner : incident[cell]) {
            if ((corner & next_assigned) != corner) continue;
            if ((corner & next) == 0 || (corner & next) == corner) {
                proper = false;
                break;
            }
        }
        if (proper) enumerate(depth + 1, next_assigned, next);
    }
}

void build_cube_graph() {
    std::map<Cell, int> index;
    for (int v : Q) for (int u : Q) if (u < v) {
        index[{v, u}] = static_cast<int>(q_cells.size());
        q_cells.emplace_back(v, u);
    }
    std::map<int, Word> by_offset;
    // Direct physical L enumeration; no equal-offset pairing is used here.
    for (int p = 0; p < 28; ++p) {
        const auto [x, y] = q_cells[p];
        by_offset[x - y] |= Word{1} << p;
        for (int step = 1; x + step <= Q.back(); ++step) {
            const auto middle = index.find({x + step, y});
            const auto last = index.find({x + step, y + step});
            if (middle == index.end() || last == index.end()) continue;
            const int j = middle->second, k = last->second;
            const Word corner = (Word{1} << p) | (Word{1} << j) | (Word{1} << k);
            for (int i : {p, j, k}) incident[i].push_back(corner);
        }
    }
    for (const auto& entry : by_offset) fibers.push_back(entry.second);
    search_order.resize(28);
    std::iota(search_order.begin(), search_order.end(), 0);
    std::stable_sort(search_order.begin(), search_order.end(), [](int a, int b) {
        return incident[a].size() > incident[b].size();
    });
    enumerate(0, 0, 0);
    std::sort(states.begin(), states.end());
    state_index.reserve(states.size() * 2);
    for (int i = 0; i < static_cast<int>(states.size()); ++i) {
        state_index.emplace(states[i], i);
        potentials.push_back(phi(states[i]));
    }
    for (int i = 0; i < 28; ++i) {
        flip_masks.push_back(Word{1} << i);
        for (int j = 0; j < i; ++j)
            flip_masks.push_back((Word{1} << i) | (Word{1} << j));
    }
    std::vector<std::uint64_t> present((Word{1} << 28) / 64);
    for (Word state : states)
        present[state / 64] |= std::uint64_t{1} << (state % 64);
    reverse_edges.resize(states.size());
    for (int i = 0; i < static_cast<int>(states.size()); ++i) {
        for (Word flip : flip_masks) {
            const Word neighbor = states[i] ^ flip;
            if (((present[neighbor / 64] >> (neighbor % 64)) & 1) == 0) continue;
            const int j = state_index.at(neighbor);
            if (potentials[j] >= potentials[i]) {
                reverse_edges[i].push_back(j);
                ++reverse_edge_count;
            }
        }
    }
}

std::uint64_t full_word(Word state, int boundary) {
    std::uint64_t word = 0;
    for (int i = 0; i < 28; ++i) if ((state >> i) & 1)
        word |= std::uint64_t{1} << internal_map[i];
    for (int i = 0; i < 8; ++i) if ((boundary >> i) & 1)
        word |= std::uint64_t{1} << external_map[i];
    return word;
}

void print_state(std::ostream& out, int state_index_value, int boundary,
                 const std::vector<int>& marks) {
    const Word state = states[state_index_value];
    const std::uint64_t word = full_word(state, boundary);
    out << "{\"q_word\":" << state << ",\"full_word\":" << word
        << ",\"phi_Q\":" << potentials[state_index_value] << ",\"rows\":[";
    for (std::size_t row = 1; row < marks.size(); ++row) {
        if (row != 1) out << ',';
        out << '"';
        for (int i = 0; i < 36; ++i)
            if (a_cells[i].first == marks[row]) out << ((word >> i) & 1);
        out << '"';
    }
    out << "]}";
}

void run(int added_mark, std::ostream& out) {
    const auto start = std::chrono::steady_clock::now();
    std::vector<int> marks = Q;
    if (std::find(marks.begin(), marks.end(), added_mark) != marks.end())
        throw std::invalid_argument("The added mark already belongs to Q");
    marks.push_back(added_mark);
    std::sort(marks.begin(), marks.end());
    build_cube_graph();
    std::cerr << "Q colorings: " << states.size()
              << "; reverse edges: " << reverse_edge_count << '\n';

    std::map<Cell, int> index;
    for (int v : marks) for (int u : marks) if (u < v) {
        index[{v, u}] = static_cast<int>(a_cells.size());
        a_cells.emplace_back(v, u);
    }
    std::map<int, int> internal_bit, external_bit;
    for (int i = 0; i < 28; ++i) {
        const int p = index.at(q_cells[i]);
        internal_map.push_back(p);
        internal_bit[p] = i;
    }
    for (int p = 0; p < 36; ++p) if (!internal_bit.count(p)) {
        external_bit[p] = static_cast<int>(external_map.size());
        external_map.push_back(p);
    }
    struct BoundaryCorner {
        Word internal;
        BoundarySet external_zero{}, external_one{};
    };
    std::vector<BoundaryCorner> boundary_corners;
    int corner_count = 0;
    for (int p = 0; p < 36; ++p) {
        const auto [x, y] = a_cells[p];
        for (int step = 1; x + step <= marks.back(); ++step) {
            const auto middle = index.find({x + step, y});
            const auto last = index.find({x + step, y + step});
            if (middle == index.end() || last == index.end()) continue;
            ++corner_count;
            Word interior = 0, exterior = 0;
            for (int i : {p, middle->second, last->second}) {
                if (internal_bit.count(i)) interior |= Word{1} << internal_bit[i];
                else exterior |= Word{1} << external_bit[i];
            }
            if (exterior == 0) continue;
            BoundaryCorner corner{interior, {}, {}};
            for (int b = 0; b < 256; ++b) {
                const auto bit = std::uint64_t{1} << (b % 64);
                if ((b & exterior) == 0) corner.external_zero[b / 64] |= bit;
                if ((b & exterior) == exterior) corner.external_one[b / 64] |= bit;
            }
            boundary_corners.push_back(corner);
        }
    }
    allowed.resize(states.size());
    reached.resize(states.size());
    BoundarySet target_boundaries{};
    std::array<std::uint64_t, 256> counts{}, target_counts{}, failure_counts{};
    std::uint64_t total = 0;
    for (int i = 0; i < static_cast<int>(states.size()); ++i) {
        BoundarySet valid{~std::uint64_t{0}, ~std::uint64_t{0},
                          ~std::uint64_t{0}, ~std::uint64_t{0}};
        for (const auto& corner : boundary_corners) {
            const Word ones = states[i] & corner.internal;
            for (int k = 0; k < 4; ++k) {
                if (ones == 0) valid[k] &= ~corner.external_zero[k];
                if (ones == corner.internal) valid[k] &= ~corner.external_one[k];
            }
        }
        allowed[i] = valid;
        for (int b = 0; b < 256; ++b) if (contains(valid, b)) {
            ++counts[b];
            ++total;
            if (potentials[i] == 4) ++target_counts[b];
        }
        if (potentials[i] == 4) {
            reached[i] = valid;
            for (int k = 0; k < 4; ++k) target_boundaries[k] |= valid[k];
        }
    }
    std::queue<int> queue;
    std::vector<bool> queued(states.size());
    for (int i = 0; i < static_cast<int>(states.size()); ++i)
        if (potentials[i] == 4 &&
            (reached[i][0] || reached[i][1] || reached[i][2] || reached[i][3])) {
            queue.push(i);
            queued[i] = true;
        }
    std::uint64_t worklist_pops = 0;
    while (!queue.empty()) {
        const int i = queue.front(); queue.pop(); queued[i] = false;
        ++worklist_pops;
        const BoundarySet current = reached[i];
        for (int j : reverse_edges[i]) {
            bool changed = false;
            for (int k = 0; k < 4; ++k) {
                const auto add = current[k] & allowed[j][k] & ~reached[j][k];
                if (add != 0) { reached[j][k] |= add; changed = true; }
            }
            if (changed && !queued[j]) { queue.push(j); queued[j] = true; }
        }
    }
    std::uint64_t failures = 0;
    int best = -1, boundary = -1;
    for (int i = 0; i < static_cast<int>(states.size()); ++i) {
        for (int b = 0; b < 256; ++b) {
            if (!contains(allowed[i], b) || !contains(target_boundaries, b)
                || contains(reached[i], b)) continue;
            ++failure_counts[b];
            ++failures;
            if (best < 0 || potentials[i] < potentials[best]) {
                best = i;
                boundary = b;
            }
        }
    }
    int target = -1;
    std::vector<int> closure;
    if (best >= 0) {
        for (int i = 0; i < static_cast<int>(states.size()); ++i)
            if (potentials[i] == 4 && contains(allowed[i], boundary)) {
                target = i;
                break;
            }
        closure.push_back(best);
        std::vector<bool> seen(states.size());
        seen[best] = true;
        for (std::size_t head = 0; head < closure.size(); ++head) {
            const int i = closure[head];
            for (Word flip : flip_masks) {
                const auto found = state_index.find(states[i] ^ flip);
                if (found == state_index.end()) continue;
                const int j = found->second;
                if (!seen[j] && potentials[j] <= potentials[i]
                    && contains(allowed[j], boundary)) {
                    seen[j] = true;
                    closure.push_back(j);
                }
            }
        }
        for (int i : closure) if (potentials[i] == 4)
            throw std::logic_error("Forward closure contradicts reverse reachability");
        std::sort(closure.begin(), closure.end());
    }
    int proper_groups = 0, balanced_groups = 0;
    for (int b = 0; b < 256; ++b) {
        proper_groups += counts[b] != 0;
        balanced_groups += target_counts[b] != 0;
    }
    const double elapsed = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - start).count();
    out << "{\n  \"status\":\"FINITE-CHECKED\",\n"
        << "  \"scope\":\"All 256 fixed boundaries of the displayed nine-mark source\",\n"
        << "  \"move_definition\":\"Simultaneous one/two internal-cell flips, preserving full properness and nonincreasing Phi_Q\",\n"
        << "  \"added_mark\":" << added_mark
        << ",\n  \"Q\":[0,1,5,6,25,26,30,31],\n  \"marks\":[";
    for (std::size_t i = 0; i < marks.size(); ++i) {
        if (i) out << ',';
        out << marks[i];
    }
    out << "],\n  \"q_proper_coloring_count\":" << states.size()
        << ",\n  \"q_reverse_edge_count\":" << reverse_edge_count
        << ",\n  \"source_corner_count\":" << corner_count
        << ",\n  \"boundary_corner_count\":" << boundary_corners.size()
        << ",\n  \"source_proper_coloring_count\":" << total
        << ",\n  \"proper_boundary_group_count\":" << proper_groups
        << ",\n  \"balanced_boundary_group_count\":" << balanced_groups
        << ",\n  \"unreachable_states_in_groups_with_balanced_targets\":" << failures
        << ",\n  \"worklist_pops\":" << worklist_pops
        << ",\n  \"elapsed_seconds\":" << elapsed
        << ",\n  \"external_cell_order\":[";
    for (int i = 0; i < 8; ++i) {
        if (i) out << ',';
        const auto [v, u] = a_cells[external_map[i]];
        out << '[' << v << ',' << u << ']';
    }
    out << "],\n  \"boundary_word_convention\":\"Bit i colors external_cell_order[i]\",\n  \"group_counts\":[\n";
    for (int b = 0; b < 256; ++b) {
        if (b) out << ",\n";
        out << "    {\"boundary_word\":" << b << ",\"proper\":" << counts[b]
            << ",\"balanced\":" << target_counts[b]
            << ",\"unreachable_with_balanced_target\":" << failure_counts[b] << '}';
    }
    out << "\n  ],\n  \"counterexample\":";
    if (best < 0) out << "null\n}\n";
    else {
        out << "{\n    \"boundary_word\":" << boundary << ",\n    \"initial\":";
        print_state(out, best, boundary, marks);
        out << ",\n    \"balanced_same_boundary\":";
        print_state(out, target, boundary, marks);
        out << ",\n    \"closure_size\":" << closure.size() << ",\n    \"closure_q_words\":[";
        for (std::size_t i = 0; i < closure.size(); ++i) {
            if (i) out << ',';
            out << states[closure[i]];
        }
        std::map<int, int> histogram;
        for (int i : closure) ++histogram[potentials[i]];
        out << "],\n    \"closure_phi_histogram\":{";
        bool first = true;
        for (const auto& [value, count] : histogram) {
            if (!first) out << ',';
            first = false;
            out << '"' << value << "\":" << count;
        }
        out << "}\n  }\n}\n";
    }
    std::cerr << "Source colorings: " << total << "; failures with balanced targets: "
              << failures << "; elapsed: " << elapsed << " seconds\n";
}
}  // namespace

int main(int argc, char** argv) {
    try {
        int mark = 2;
        std::string output;
        for (int i = 1; i < argc; ++i) {
            const std::string option = argv[i];
            if (option == "--mark" && i + 1 < argc) {
                const std::string text = argv[++i];
                std::size_t used = 0;
                mark = std::stoi(text, &used);
                if (used != text.size() || mark < -100000 || mark > 100000)
                    throw std::invalid_argument("--mark requires an integer in [-100000,100000]");
            } else if (option == "--output" && i + 1 < argc) output = argv[++i];
            else throw std::invalid_argument("Usage: search [--mark INTEGER] [--output FILE]");
        }
        if (output.empty()) run(mark, std::cout);
        else {
            std::ofstream file(output);
            if (!file) throw std::runtime_error("Cannot open output file");
            run(mark, file);
            if (!file) throw std::runtime_error("Cannot write output file");
        }
    } catch (const std::exception& error) {
        std::cerr << error.what() << '\n';
        return 1;
    }
}
