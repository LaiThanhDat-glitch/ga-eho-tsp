# ĐỒ ÁN MÔN HỌC: TRÍ TUỆ NHÂN TẠO

## ỨNG DỤNG THUẬT TOÁN GENETIC ALGORITHM VÀ ELEPHANT HERDING OPTIMIZATION CHO BÀI TOÁN NGƯỜI DU LỊCH (TSP)

**Nhóm thực hiện:**
- TRƯƠNG THÀNH ĐẠT
- NGUYỄN TẤN KHIÊM  
- NGUYỄN PHƯƠNG CHINH
- LẠI THÀNH ĐẠT

**Giảng viên hướng dẫn:** TS. Đặng Ngọc Hoàng Thành

---

## MỤC LỤC

1. [TỔNG QUAN](#chương-1-tổng-quan)
2. [GIẢI THUẬT DI TRUYỀN (GA)](#chương-2-giải-thuật-di-truyền)
3. [THUẬT TOÁN ELEPHANT HERDING OPTIMIZATION (EHO)](#chương-3-thuật-toán-elephant-herding-optimization)
4. [KẾT QUẢ THỰC NGHIỆM](#chương-4-kết-quả-thực-nghiệm)
5. [KẾT LUẬN](#chương-5-kết-luận)

---

## CHƯƠNG 1. TỔNG QUAN

### 1.1. Giới thiệu bài toán người du lịch

Bài toán người du lịch (Traveling Salesman Problem - TSP) là một trong những bài toán tối ưu tổ hợp được nghiên cứu nhiều nhất trong khoa học máy tính và toán học rời rạc. Bài toán mô tả tình huống một người cần đi thăm một tập thành phố, mỗi thành phố được thăm đúng một lần, bắt đầu và kết thúc tại cùng một điểm xuất phát. Mục tiêu là xác định thứ tự thăm sao cho tổng chi phí di chuyển của toàn bộ chuyến đi là nhỏ nhất.

TSP có ứng dụng thực tiễn rộng rãi:
- Lập lịch phân phối hàng hóa
- Định tuyến mạch in điện tử (PCB drilling)
- Lập kế hoạch sản xuất
- Định tuyến robot công nghiệp
- Nhiều bài toán quy hoạch khác

### 1.2. Phát biểu bài toán

**Đầu vào:**
- Tập thành phố: V = {0, 1, ..., n-1}
- Ma trận khoảng cách D kích thước n × n
- D[i][j]: chi phí đi từ thành phố i đến thành phố j

**Điều kiện ma trận D:**
- Vuông: kích thước n × n với n ≥ 3
- Đường chéo bằng 0: D[i][i] = 0
- Đối xứng: D[i][j] = D[j][i] (Symmetric TSP)
- Các phần tử hữu hạn và không âm

**Biểu diễn nghiệm:**
- Một hành trình hợp lệ là hoán vị π của tất cả thành phố
- Quy ước: π[0] = 0 (cố định thành phố 0 làm điểm xuất phát)
- Route được lưu dưới dạng tuple số nguyên 0-based

**Hàm mục tiêu:**

Chi phí của hành trình π:

```
L(π) = Σ(k=0 to n-2) D[π[k], π[k+1]] + D[π[n-1], π[0]]
```

Số hạng cuối là chi phí quay về thành phố xuất phát, tạo thành chu trình khép kín.

**Mục tiêu:** Tìm π* sao cho L(π*) là nhỏ nhất:

```
π* = argmin L(π)
```

### 1.3. Độ phức tạp và lý do sử dụng thuật toán tìm kiếm

TSP thuộc lớp bài toán NP-Hard. Số lượng hành trình phân biệt với n thành phố (khi cố định điểm xuất phát) là (n-1)!.

| Số thành phố (n) | Số hành trình (n-1)! |
|------------------|----------------------|
| 3 | 2 |
| 6 | 120 |
| 10 | 362,880 |
| 15 | 87,178,291,200 |
| 20 | 1.2 × 10¹⁷ |
| 26 | ≈ 1.6 × 10²⁵ |

Liệt kê toàn bộ hành trình để tìm nghiệm tối ưu là điều không khả thi trong thực tế với các bài toán kích thước trung bình trở lên. Vì vậy, các phương pháp heuristic và metaheuristic (Genetic Algorithm và Elephant Herding Optimization) được sử dụng để tìm nghiệm đủ tốt trong thời gian hợp lý.

### 1.4. Hướng tiếp cận giải quyết

Đồ án triển khai hai thuật toán metaheuristic:

**1. Genetic Algorithm (GA):**
- Mô phỏng quá trình tiến hóa tự nhiên
- Duy trì quần thể gồm nhiều hành trình ứng viên
- Chọn lọc các cá thể tốt, kết hợp chúng để tạo thế hệ mới
- Áp dụng đột biến để khám phá vùng tìm kiếm mới

**2. Elephant Herding Optimization (EHO):**
- Mô phỏng hành vi đàn voi
- Chia quần thể thành các clan
- Cập nhật vị trí mỗi voi theo matriarch (cá thể tốt nhất trong clan)
- Tách các voi đực kém nhất khỏi clan

---

## CHƯƠNG 2. GIẢI THUẬT DI TRUYỀN

### 2.1. Giới thiệu về Genetic Algorithm

Genetic Algorithm (GA) là thuật toán tìm kiếm và tối ưu được Holland giới thiệu vào những năm 1970, lấy cảm hứng từ quá trình tiến hóa sinh học theo thuyết chọn lọc tự nhiên của Darwin.

**Quy trình GA:**
1. Đánh giá chất lượng (fitness) của từng cá thể
2. Chọn lọc các cá thể tốt làm cha mẹ (selection)
3. Lai ghép (crossover) để tạo cá thể con kế thừa đặc điểm
4. Đột biến (mutation) để duy trì đa dạng và khám phá vùng mới
5. Hình thành quần thể thế hệ tiếp theo

**Biểu diễn cho TSP:**
- Mỗi cá thể là một tuple chứa đầy đủ n thành phố
- Quy ước thành phố 0 luôn đứng đầu
- Các toán tử chỉ thao tác trên phần tail (từ vị trí 1 trở đi)
- Đảm bảo không làm mất tính hợp lệ của hoán vị

### 2.2. Cách áp dụng GA cho bài toán TSP

#### 2.2.1. Luồng xử lý tổng quát

```python
# Pseudocode vòng lặp GA
kiểm tra problem và config
rng = Random(config.seed)
population = khởi_tạo(population_size, rng)
costs = [route_length(r) for r in population]
best_route, best_distance = best(population, costs)
ghi snapshot iteration=0

for iteration in 1..min(generations, max_iterations):
    kiểm tra stop / time_limit / max_evaluations
    
    next_pop, next_costs = select_elites(population, costs, elite_count)
    selector = prepare_selection(population, costs, method, k)
    rate = effective_mutation_rate(config, stagnation, diversity)
    
    while len(next_pop) < population_size:
        kiểm tra stop
        p1, p2 = selector.pick(rng), selector.pick(rng)
        children = crossover(p1, p2, rng) if rng.random() < crossover_rate else (p1, p2)
        for child in children:
            child = mutate(child, rate, rng, mutation_method)
            cost = route_length(child)  # evaluations++
            cập nhật best_route, best_distance
            if local_search_enabled:
                child, cost = improve(child, cost, ...)
            next_pop.append(child)
    
    commit: population, costs = next_pop, next_costs
    cập nhật stagnation, ghi history
    kiểm tra STAGNATION

ghi snapshot cuối
trả RunResult(best_route, best_distance, ...)
```

#### 2.2.2. Khởi tạo quần thể

**a) Random initialization (mặc định):**
- Mỗi route được sinh bằng cách tạo hoán vị ngẫu nhiên
- Xoay để thành phố 0 đứng đầu
- Dùng rng riêng để đảm bảo tái lập kết quả

**b) Nearest-neighbor initialization:**
- Thuật toán tham lam: chọn thành phố chưa thăm gần nhất
- Nếu bằng nhau thì chọn thành phố có chỉ số nhỏ hơn
- Mỗi route NN được sinh từ điểm bắt đầu khác nhau

**c) Mixed initialization:**
- Kết hợp một phần route NN (25% mặc định)
- Phần còn lại là random
- Đặt nghiệm chất lượng tốt vào quần thể ban đầu

#### 2.2.3. Chọn cha mẹ (Selection)

**a) Tournament Selection (mặc định):**
- Lấy ngẫu nhiên k cá thể (k=3 mặc định)
- Chọn cá thể có chi phí thấp nhất
- Hai lần chọn cha mẹ độc lập nhau

**b) Rank Selection:**
- Sắp xếp cá thể từ tốt đến kém
- Gán trọng số P, P-1, ..., 1 theo thứ hạng
- Làm giảm áp lực chọn lọc, duy trì đa dạng

**c) Roulette Wheel Selection:**
- Chuyển chi phí thành trọng số: weight_i = 1 - cost_i / max_cost
- Cá thể chi phí thấp có xác suất được chọn lớn hơn

#### 2.2.4. Lai ghép (Crossover)

**a) Order Crossover - OX (mặc định):**
- Bảo tồn thứ tự tương đối của các thành phố
- Chọn ngẫu nhiên hai vị trí cắt left, right trên tail
- Sao chép đoạn [left:right] từ cha thứ nhất
- Điền các thành phố còn lại theo thứ tự từ cha thứ hai

```python
def order_crossover(parent1, parent2, rng):
    a, b = parent1[1:], parent2[1:]
    left, right = sorted(rng.sample(range(len(a)), 2))
    right += 1
    
    def child(first, second):
        result = [-1] * len(first)
        result[left:right] = first[left:right]
        used = set(first[left:right])
        values = [city for city in second[right:] + second[:right] if city not in used]
        positions = list(range(right, len(first))) + list(range(left))
        for position, value in zip(positions, values):
            result[position] = value
        return (0, *result)
    
    return child(a, b), child(b, a)
```

**b) Partially Mapped Crossover - PMX:**
- Giữ đoạn [left:right] từ cha thứ nhất
- Dùng ánh xạ giữa đoạn của hai cha mẹ để giải quyết xung đột

#### 2.2.5. Đột biến (Mutation)

**a) Inversion Mutation (mặc định):**
- Chọn ngẫu nhiên hai vị trí trên tail
- Đảo ngược thứ tự của đoạn giữa hai vị trí đó

**b) Swap Mutation:**
- Chọn ngẫu nhiên hai vị trí khác nhau
- Hoán đổi hai thành phố tại hai vị trí đó

**c) Insertion Mutation:**
- Lấy thành phố tại vị trí i ra khỏi route
- Chèn vào vị trí j

**d) Scramble Mutation:**
- Chọn ngẫu nhiên một đoạn trên tail
- Xáo trộn thứ tự các thành phố trong đoạn đó

```python
def mutate(route, rate, rng, method="inversion"):
    if rng.random() >= rate:
        return tuple(route)
    
    result = list(route)
    i, j = rng.sample(range(1, len(route)), 2)
    
    if method == "swap":
        result[i], result[j] = result[j], result[i]
    elif method == "insertion":
        result.insert(j, result.pop(i))
    else:
        i, j = sorted((i, j))
        segment = result[i:j+1]
        if method == "inversion":
            segment.reverse()
        else:  # scramble
            rng.shuffle(segment)
        result[i:j+1] = segment
    
    return tuple(result)
```

#### 2.2.6. Elitism và Global Best

**Elitism:**
- Bảo tồn elite_count cá thể tốt nhất
- Sao chép trực tiếp sang quần thể kế tiếp
- Không đánh giá lại (tái dùng fitness đã biết)

**Global Best Archive:**
- Mỗi lần route con được đánh giá
- Nếu chi phí nhỏ hơn global best hiện tại
- Archive được cập nhật ngay lập tức
- Kết quả cuối cùng là global best của toàn bộ lần chạy

#### 2.2.7. Điều kiện dừng

| Điều kiện | stopping_reason | Mô tả |
|-----------|----------------|-------|
| Hết số generation | MAX_ITERATIONS | Đạt min(generations, max_iterations) thế hệ hoàn chỉnh |
| Hết ngân sách đánh giá | MAX_EVALUATIONS | Tổng lần gọi route_length ≥ max_evaluations |
| Hết thời gian | TIME_LIMIT | Thời gian thực tế ≥ time_limit_seconds |
| Yêu cầu dừng | CANCELLED | stop_requested() trả True |
| Trì trệ | STAGNATION | stagnation_patience thế hệ liên tiếp không cải thiện |

#### 2.2.8. Các phương án nâng cao

**a) Stagnation Stopping:**
- Dừng thuật toán sớm khi không cải thiện
- Reset về 0 mỗi khi global best cải thiện

**b) Adaptive Mutation:**
- Điều chỉnh mutation rate động theo mức trì trệ và diversity
- Tăng tuyến tính theo stagnation
- Diversity ≤ 0.1 đặt pressure tối thiểu 0.5

**c) Bounded 2-opt Local Search:**
- Tìm kiếm cục bộ 2-opt theo chiến lược first-improvement
- Với mỗi cặp (i,j), thử đảo đoạn route[i..j]
- Chấp nhận ngay nếu cải thiện chi phí
- Mỗi probe 2-opt gọi một lần route_length đầy đủ

---

## CHƯƠNG 3. THUẬT TOÁN ELEPHANT HERDING OPTIMIZATION

### 3.1. Tổng quan về Elephant Herding Optimization

#### 3.1.1. Khái niệm EHO

Elephant Herding Optimization (EHO) là thuật toán tối ưu hóa lấy cảm hứng từ hành vi sống theo đàn của loài voi. Quần thể được chia thành nhiều nhóm nhỏ gọi là Clan, trong đó mỗi cá thể đại diện cho một lời giải và được đánh giá bằng hàm mục tiêu.

#### 3.1.2. Nguyên lý hành vi đàn voi

- Mỗi Clan gồm một cá thể dẫn đầu gọi là Matriarch
- Các cá thể trong đàn cập nhật vị trí dựa trên Matriarch
- Matriarch được điều chỉnh theo tâm của Clan
- Cá thể có fitness kém nhất thực hiện cơ chế Separation
- Ba cơ chế này cân bằng khai thác nghiệm tốt và khám phá vùng mới

#### 3.1.3. Các thành phần chính

**Thành phần EHO:**
- **Clan:** Nhóm các cá thể voi trong quần thể
- **Matriarch:** Cá thể có nghiệm tốt nhất trong mỗi clan
- **Clan center:** Tâm đại diện cho các cá thể trong clan
- **Clan updating operator:** Cập nhật cá thể dựa trên matriarch và tâm clan
- **Separating operator:** Thay thế cá thể kém để duy trì đa dạng

**Công thức EHO liên tục:**

Vị trí voi thường:
```
p(t+1)[i,c] = p(t)[i,c] + αr(p(t)[best,c] - p(t)[i,c])
```

Matriarch:
```
p(t+1)[best,c] = βp(t)[center,c]
p(t)[center,c] = (1/m)Σp(t)[i,c]
```

Separation:
```
p(t+1)[worst,c] = pmin,c + r(pmax,c - pmin,c + 1)
```

### 3.2. Áp dụng EHO cho bài toán TSP

| Thành phần EHO | Cách áp dụng trong D-EHO |
|----------------|--------------------------|
| Cá thể | Một tour gồm thứ tự các thành phố, cố định thành phố 0 ở đầu |
| Clan | Nhóm gồm m tour |
| Matriarch | Tour có tổng quãng đường ngắn nhất trong clan |
| Tâm clan | Tour medoid có tổng khoảng cách Hamming nhỏ nhất |
| Cập nhật α | Dùng guided-swap đưa các tour về matriarch |
| Cập nhật β | Dùng guided-swap đưa matriarch về tâm clan |
| Separation | Thay các tour kém nhất bằng hoán vị ngẫu nhiên hợp lệ |
| Elitism | Lưu nghiệm tốt nhất của từng clan và toàn quần thể |

#### 3.2.1. Biểu diễn nghiệm và hàm mục tiêu

Tour được biểu diễn:
```
π = (0, π₁, π₂, ..., πₙ₋₁)
```

Hàm mục tiêu:
```
L(π) = Σ(i=0 to n-2) D[πᵢ, πᵢ₊₁] + D[πₙ₋₁, π₀]
```

#### 3.2.2. Phân chia quần thể thành các Clan

```python
@dataclass(frozen=True)
class Clan:
    members: tuple[Route, ...]
    costs: tuple[float, ...]
    
    def best_index(self) -> int:
        return min(range(self.size), 
                  key=lambda index: (self.costs[index], index))
    
    def center(self) -> Route:
        return self.members[self.center_index()]
```

Matriarch được xác định:
```
T[best,c] = argmin L(Tᵢ) for Tᵢ ∈ Clanc
```

#### 3.2.3. Cập nhật Matriarch

**Khoảng cách Hamming:**
```
dH(π, σ) = Σ(j=1 to n-1) [πⱼ ≠ σⱼ]
```

**Tâm clan (Hamming Medoid):**
```
T[center,c] = argmin Σ dH(π, σ) for π,σ ∈ Clanc
```

Nếu có nhiều tour cùng khoảng cách, ưu tiên tour có chi phí thấp hơn.

```python
def center_index(self) -> int:
    distance_totals = [0] * self.size
    for first in range(self.size):
        for second in range(first + 1, self.size):
            distance = hamming_distance(self.members[first], 
                                       self.members[second])
            distance_totals[first] += distance
            distance_totals[second] += distance
    
    return min(range(self.size),
              key=lambda index: (distance_totals[index], 
                               self.costs[index], index))
```

#### 3.2.4. Di chuyển voi thường (Clan Updating Operator)

Các cá thể voi thường được cập nhật bằng **Guided-Swap**, đưa route hiện tại tiến gần route Matriarch.

**Xác định số lần hoán đổi:**
```
diff = {j | πⱼ ≠ targetⱼ, j ≥ 1}
k = ⌊α · r · |diff|⌋
```

Trong đó: r ~ U[0,1), α ∈ [0,1] là hệ số cập nhật.

**Quy trình Guided-Swap:**
1. Xác định các vị trí khác nhau giữa hai route
2. Xáo trộn danh sách vị trí khác nhau
3. Chọn vị trí cần cập nhật và hoán đổi thành phố
4. Lặp lại cho đến khi đủ số lần hoán đổi

```python
def guided_swap(source, target, strength, rng):
    n = len(source)
    diff = [i for i in range(1, n) if source[i] != target[i]]
    steps = floor(strength * rng.random() * len(diff))
    
    if steps <= 0:
        return tuple(source)
    
    result = list(source)
    pos = [0] * n
    for idx, city in enumerate(result):
        pos[city] = idx
    
    rng.shuffle(diff)
    swaps_done = 0
    
    for i in diff:
        if swaps_done >= steps:
            break
        desired_city = target[i]
        current_city = result[i]
        if current_city == desired_city:
            continue
        j = pos[desired_city]
        result[i], result[j] = desired_city, current_city
        pos[desired_city] = i
        pos[current_city] = j
        swaps_done += 1
    
    return tuple(result)
```

#### 3.2.5. Tách đàn (Separating Operator)

**Mục đích:** Duy trì tính đa dạng của quần thể và hạn chế hội tụ sớm vào nghiệm tối ưu cục bộ.

**Quy trình:**
1. Bảo vệ Matriarch: Loại bỏ chỉ số của cá thể Matriarch khỏi danh sách có thể bị thay thế
2. Xác định cá thể kém nhất: Chọn separation_count_per_clan cá thể có cost cao nhất
3. Giữ lại cá thể không bị tách
4. Tạo cá thể mới: Thay thế bằng hoán vị ngẫu nhiên hợp lệ
5. Tạo clan mới: Kết hợp routes được giữ lại và routes mới

```python
protected = set(protected_indices)
eligible = [index for index in range(clan_size) if index not in protected]
worst_indices = sorted(eligible, 
                      key=lambda i: (-costs[i], i))[:separation_count]

for idx in worst_indices:
    new_clan[idx] = random_permutation(n, rng)
```

#### 3.2.6. Cơ chế bảo tồn nghiệm tốt nhất (Elitism)

**Hai cấp độ lưu trữ:**
- **Clan Archive:** Lưu trữ route tốt nhất từng được tìm thấy của mỗi clan
- **Global Best:** Lưu trữ route có cost nhỏ nhất trong toàn bộ quá trình chạy

**Quá trình cập nhật:**
1. Khởi tạo Archive: Sau khi khởi tạo quần thể, route tốt nhất của mỗi clan được lưu vào Clan Archive
2. Đánh giá candidate: So sánh cost của route với Clan Archive
3. Cập nhật Global Best: Candidate được so sánh với nghiệm tốt nhất toàn cục
4. Khôi phục nghiệm tốt nhất: Nếu route Archive bị mất, đưa route này trở lại clan
5. Commit generation: Generation mới trở thành trạng thái chính thức

```python
def _preserve_clan_best(clan, best_route, best_distance):
    if best_route in clan.members:
        return clan
    
    leader_index = clan.best_index()
    replacement_index = clan.worst_indices(1, 
                                          protected_indices=(leader_index,))[0]
    
    members = list(clan.members)
    costs = list(clan.costs)
    members[replacement_index] = best_route
    costs[replacement_index] = best_distance
    
    return Clan(tuple(members), tuple(costs))
```

### 3.3. Quy trình hoạt động của D-EHO

#### 3.3.1. Pseudocode

```
Input: TSP distance matrix D, clan_count N_c, elephants_per_clan m,
       alpha, beta, separation_count s, stopping limits
Output: best valid tour and its distance

Initialize N_c clans with m random valid tours each
Evaluate all initial tours
For each clan: archive its best tour
Set global_best to the best initial tour

While no stopping condition is met:
    Create an empty next_population
    For each clan:
        Select the lowest-cost tour as matriarch
        Compute the clan Hamming medoid
        Select up to s worst tours, excluding the matriarch
        
        For each member index i:
            If i is the matriarch:
                candidate = guided_swap(matriarch, medoid, beta)
            Else if i is selected for separation:
                candidate = random valid permutation
            Else:
                candidate = guided_swap(member[i], matriarch, alpha)
            
            Evaluate candidate once
            Update clan archive and global_best if improved
            Append candidate to next clan
    
    If every clan was completed:
        Restore archived clan best when needed
    
    If a full generation was completed:
        Commit next_population
    Else:
        Keep the last committed population and stop

Return global_best and run metadata
```

### 3.4. Triển khai thuật toán trong chương trình

#### 3.4.1. Cấu trúc các module

| Module | Trách nhiệm |
|--------|-------------|
| solver.py | Khởi tạo clan, điều khiển vòng lặp, cập nhật archive và trả kết quả |
| clans.py | Quản lý clan, chọn best/worst và tính Hamming Medoid |
| discrete_ops.py | Tính Hamming distance và thực hiện guided-swap |
| separation.py | Chọn route kém và sinh permutation mới |
| objective.py | Kiểm tra route và tính tổng khoảng cách |

#### 3.4.2. Các tham số cấu hình

| Tham số | Giá trị mặc định | Ý nghĩa |
|---------|------------------|---------|
| clan_count | Theo cấu hình | Số lượng clan |
| elephants_per_clan | Theo cấu hình | Số cá thể mỗi clan |
| alpha | 0.7 | Hệ số cập nhật cá thể |
| beta | 0.3 | Hệ số cập nhật Matriarch |
| separation_count_per_clan | 1 | Số cá thể tách mỗi clan |
| seed | Theo cấu hình | Giá trị khởi tạo ngẫu nhiên |
| iterations | Theo cấu hình | Số thế hệ chạy |

**Điều kiện kiểm tra:**
- Mỗi clan có ít nhất 3 cá thể và có tối thiểu 2 clan
- alpha, beta thuộc khoảng [0, 1]
- Số cá thể separation phải nhỏ hơn kích thước clan
- Evaluation budget phải đủ để đánh giá quần thể ban đầu

#### 3.4.3. Điều kiện dừng

Solver có thể dừng khi:
- Đạt giới hạn thế hệ (iterations)
- Đạt max_evaluations
- Đạt time_limit_seconds
- Callback yêu cầu dừng

Nếu chạy đủ G thế hệ, số objective evaluations là:
```
N_c × m × (G + 1)
```

### 3.5. Nhận xét và giới hạn của D-EHO

#### 3.5.1. Ưu điểm

- Giữ các thành phần có ý nghĩa của EHO (clan, matriarch, cập nhật clan và separation)
- Mọi thao tác đều tạo route hợp lệ mà không cần repair
- Archive theo clan và global best hạn chế mất nghiệm tốt
- Hỗ trợ seed, giới hạn số lần đánh giá và giới hạn thời gian

#### 3.5.2. Hạn chế

- Thay phép toán vector bằng guided-swap, Hamming medoid và permutation ngẫu nhiên
- Không phải tương đương đại số với EHO liên tục
- Hamming medoid xét vị trí thành phố, không trực tiếp tối ưu mức tương đồng cạnh
- Chỉ hỗ trợ symmetric TSP
- Heuristic không bảo đảm tìm optimum toàn cục

#### 3.5.3. Khả năng áp dụng cho TSP

Implementation phù hợp với phạm vi đề tài hiện tại:
- TSP đối xứng, có ít nhất ba thành phố
- Ma trận khoảng cách hữu hạn, không âm, đối xứng, đường chéo bằng 0
- Cố định thành phố 0 ở đầu route loại bỏ các biểu diễn quay vòng tương đương

D-EHO đã có thể dùng làm solver rời rạc độc lập để minh họa và thực nghiệm EHO trên TSP đối xứng trong phạm vi dữ liệu của dự án.

---

## CHƯƠNG 4. KẾT QUẢ THỰC NGHIỆM

> **Nguồn số liệu:** Các bảng trong chương này được chép từ output đang lưu trong năm notebook `Experiment_1-2_REVISED.ipynb`, `Experiment_3_REVISED.ipynb`, `Experiment_4_REVISED.ipynb`, `Experiment5-EHO-Params.ipynb` và `Experiment6-EHO-vs-GA.ipynb`. Các code cell đều có execution count; một số cell thiết lập không tạo output, và không thấy output loại traceback trong lần rà soát này. Thời gian là số do notebook ghi trên môi trường đã chạy notebook, không phải cam kết tốc độ trên mọi máy. Những nhận xét Markdown cũ trong notebook chỉ được giữ khi phù hợp với bảng số liệu bên dưới.

### 4.1. Thiết kế thực nghiệm và bộ dữ liệu

Các thí nghiệm sử dụng bảy ma trận khoảng cách có sẵn trong thư mục `data/`:

| Tên file | Số thành phố | Mục đích xuất hiện trong notebook |
|---|---:|---|
| `03Cities-6.txt` | 3 | Đánh giá GA theo quy mô và so sánh GA–EHO |
| `04Cities-189.txt` | 4 | Đánh giá GA theo quy mô và so sánh GA–EHO |
| `06Cities-1248.txt` | 6 | Đánh giá GA theo quy mô và so sánh GA–EHO |
| `15Cities-1194.txt` | 15 | So sánh operator GA, thử tham số EHO, đánh giá theo quy mô và so sánh GA–EHO |
| `26Cities-937.txt` | 26 | Thử khởi tạo Nearest Neighbor, thử tham số EHO, đánh giá theo quy mô và so sánh GA–EHO |
| `42Cities-699.txt` | 42 | Thử selection, đánh giá theo quy mô và so sánh GA–EHO |
| `48Cities-33523.txt` | 48 | Thử adaptive mutation/2-opt, đánh giá theo quy mô và so sánh GA–EHO |

| Notebook | Thiết lập chính | Số lần chạy thực tế trong output |
|---|---|---:|
| Experiment 1–2 | Dataset 15 thành phố; 5 seed `[11, 23, 37, 53, 71]`; population 40; `generations=100`; baseline Tournament `k=3` + OX + inversion; `crossover_rate=0,9`, `mutation_rate=0,01`, `elite_count=2`; tối đa 2.000 evaluations/run. Mỗi lượt chỉ thay một selection/crossover/mutation. | 5 cho mỗi cấu hình được báo cáo |
| Experiment 3 | 7 dataset; cùng 5 seed; population 40; `mutation_rate=0,15`; `generations=max_iterations=4.000`; tối đa 4.000 evaluations và `time_limit=10s` mỗi run; các operator khác dùng GA defaults (Tournament `k=3`, OX, inversion, crossover 0,9, 2 elites). | 35/35 |
| Experiment 4 | NN initialization trên 26 thành phố; Tournament trên 42 thành phố; adaptive mutation và 2-opt trên 48 thành phố; population 40; `mutation_rate=0,15`; `generations=200`; tối đa 8.000 evaluations/run; 5 seed. Các operator nền dùng GA defaults. | 5 run cho mỗi cấu hình được báo cáo |
| Experiment 5 | EHO; baseline 4 clan × 20 voi, 250 iterations, `alpha=0,7`, `beta=0,3`, separation count 1; alpha/beta trên dataset 15 thành phố, clan/separation trên dataset 26; 5 seed; 4.000 evaluations/run; tối đa 10s/run và 120s/notebook. | 75/75 |
| Experiment 6 | 7 dataset × 5 seed × 2 solver; budget 6.000 evaluations/run; GA: population 80, 2.000 generations, Tournament `k=3`, OX/crossover 0,9, inversion/mutation 0,15, 2 elites; EHO: 4 clan × 20 voi, 250 iterations, alpha 0,7, beta 0,3, separation count 1; cap 10s/run và 120s/notebook. | 70/70 |

Trong output hiện tại, cả 35 run của Experiment 3 đều dừng do đạt `MAX_EVALUATIONS` sau 4.000 evaluations. Experiment 5 và 6 hoàn thành toàn bộ run trước giới hạn tổng thời gian 120 giây. Các độ lệch chuẩn của Experiment 3 và Experiment 5–6 được notebook tính theo độ lệch chuẩn mẫu; Experiment 1–2 dùng `numpy.std` mặc định, tức độ lệch chuẩn tổng thể. Vì quy ước khác nhau, không nên so trực tiếp độ lệch chuẩn giữa các notebook như thể chúng được tính cùng một cách.

### 4.2. So sánh selection, crossover và mutation của GA

Experiment 1–2 chạy từng cấu hình trên cùng dataset 15 thành phố với năm seed. Bảng sau lấy mean, median và độ lệch chuẩn được tính trực tiếp từ năm kết quả của từng biến thể trong notebook.

| Nhóm operator | Biến thể | Min/Best | Mean distance | Median | Max/Worst | Độ lệch chuẩn | Số runs |
|---|---|---:|---:|---:|---:|---:|---:|
| Selection | Tournament | 1354,0 | 1642,8 | 1725,0 | 1827,0 | 184,36 | 5 |
| Selection | Rank | 1366,0 | 1498,2 | 1504,0 | 1624,0 | 101,19 | 5 |
| Selection | Roulette wheel | **1377,0** | **1492,6** | 1494,0 | 1678,0 | 106,77 | 5 |
| Crossover | OX (baseline) | 1354,0 | 1642,8 | 1725,0 | 1827,0 | 184,36 | 5 |
| Crossover | PMX | 1348,0 | 1536,6 | 1549,0 | 1659,0 | 104,57 | 5 |
| Mutation | Inversion (baseline) | 1354,0 | 1642,8 | 1725,0 | 1827,0 | 184,36 | 5 |
| Mutation | Swap | 1503,0 | 1743,6 | 1805,0 | 1927,0 | 162,50 | 5 |
| Mutation | Insertion | 1503,0 | 1674,6 | 1586,0 | 1928,0 | 163,58 | 5 |
| Mutation | Scramble | 1407,0 | 1666,6 | 1777,0 | 1846,0 | 188,35 | 5 |

Trong phạm vi năm seed và cấu hình đã chạy, roulette có mean thấp nhất trong ba selection được thử; rank cũng thấp hơn tournament. PMX có mean thấp hơn OX trong cặp cấu hình đã chạy. Trong bốn mutation được so sánh, inversion có mean thấp nhất; swap, insertion và scramble có mean cao hơn. Đây là kết quả của một mẫu nhỏ gồm năm seed, không chứng minh operator tương ứng luôn tốt hơn trên mọi dataset hoặc mọi cấu hình. Cột Min/Best và Max/Worst báo trực tiếp hai giá trị biên trong năm run, còn độ lệch chuẩn ở bảng này là độ lệch chuẩn tổng thể do notebook dùng `numpy.std` mặc định.

**Cần thay hình nếu báo cáo có chèn biểu đồ từ notebook:** các hình đường hội tụ baseline nằm ở cell 4, biểu đồ so sánh selection ở cell 9 và biểu đồ so sánh mutation ở cell 16 của `Experiment_1-2_REVISED.ipynb`. Dùng hình được tạo từ output hiện tại, không dùng hình xuất từ lần chạy cũ. Output cell 9 cần được diễn giải theo số liệu mới: roulette có mean 1492,6, thấp hơn rank 1498,2 và tournament 1642,8; kết luận Markdown cũ nói tournament tốt nhất không còn đúng.

### 4.3. Ổn định của GA theo kích thước TSP

Experiment 3 chạy năm seed cho mỗi dataset, với giới hạn 4.000 objective evaluations/run. Bảng sau lấy từ output tổng hợp của cell 29; runtime là thời gian trung bình của một lần gọi solver được notebook đo.

| Thành phố | Best observed | Mean | Median | Worst | Độ lệch chuẩn mẫu | Evaluations/run | Runtime trung bình (giây) | Runs |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 6 | 6,00 | 6,00 | 6 | 0,00 | 4.000 | 0,0375 | 5 |
| 4 | 189 | 189,00 | 189,00 | 189 | 0,00 | 4.000 | 0,0378 | 5 |
| 6 | 1248 | 1248,00 | 1248,00 | 1248 | 0,00 | 4.000 | 0,0441 | 5 |
| 15 | 1194 | 1200,20 | 1194,00 | 1225 | 13,86 | 4.000 | 0,0545 | 5 |
| 26 | 969 | 1046,00 | 1034,00 | 1186 | 82,85 | 4.000 | 0,0667 | 5 |
| 42 | 1102 | 1151,60 | 1133,00 | 1211 | 49,75 | 4.000 | 0,0753 | 5 |
| 48 | 51215 | 55404,60 | 55339,00 | 59638 | 3031,79 | 4.000 | 0,0953 | 5 |

Ba trường hợp 3, 4 và 6 thành phố có cùng kết quả ở cả năm seed; notebook ghi các mốc tương ứng là nghiệm tối ưu đã kiểm tra bằng liệt kê. Với các bộ lớn hơn, bảng chỉ dùng best observed trong năm seed, không khẳng định đó là optimum toàn cục. Độ phân tán quan sát được lớn hơn ở 26 và 48 thành phố so với các trường hợp nhỏ, nhưng bảy điểm dữ liệu này chưa đủ để kết luận quy luật tăng trưởng tổng quát về độ lệch chuẩn hay runtime.

Các hình phân phối kết quả và chênh lệch nằm tại cell 8, 11, 14, 17, 20, 23 và 26; hình tổng quan xu hướng nằm ở cell 31 của `Experiment_3_REVISED.ipynb`. Nếu lấy ảnh đưa vào báo cáo, hãy xuất lại đúng các hình từ output hiện tại. Các nhận xét về tỷ lệ đạt “min quan sát” cần hiểu là tỷ lệ đạt giá trị thấp nhất của năm run, không phải tỷ lệ tìm thấy nghiệm tối ưu đã biết.

### 4.4. Các thử nghiệm cải tiến GA

Experiment 4 không chạy một bảng benchmark thống nhất trên cùng dataset cho mọi cải tiến. Mỗi tiểu thí nghiệm dùng dataset và cấu hình riêng, nên cần đọc số liệu theo từng nhóm, không gộp các hàng thành một phép so sánh trực tiếp.

**Nearest Neighbor initialization trên dataset 26 thành phố:**

| Biến thể | Best | Mean | Median | Worst | Độ lệch chuẩn mẫu | Runtime trung bình (giây) | Runs |
|---|---:|---:|---:|---:|---:|---:|---:|
| Baseline ngẫu nhiên | 962,00 | 992,40 | 998,00 | 1005,00 | 17,42 | 0,1158 | 5 |
| Nearest Neighbor initialization | 961,00 | 961,00 | 961,00 | 961,00 | 0,00 | 0,1110 | 5 |

Trong năm seed của lần chạy này, NN initialization giảm mean từ 992,40 xuống 961,00. Đây là phép thử trên dataset 26 thành phố; không được dùng hàng này như số liệu riêng của bài 48 thành phố.

**Tournament selection trên dataset 42 thành phố:** kết quả của năm seed được tóm tắt dưới đây.

| Biến thể | Best | Mean | Median | Worst | Độ lệch chuẩn mẫu | Runtime trung bình (giây) | Runs |
|---|---:|---:|---:|---:|---:|---:|---:|
| Tournament | 876,00 | 906,60 | 888,00 | 985,00 | 44,59 | 0,1283 | 5 |

**Fixed và adaptive mutation trên dataset 48 thành phố:**

| Biến thể | Best | Mean | Median | Worst | Độ lệch chuẩn mẫu | Runtime trung bình (giây) | Runs |
|---|---:|---:|---:|---:|---:|---:|---:|
| Mutation cố định 0,15 | 40302,00 | 43279,00 | 44600,00 | 46230,00 | 2652,47 | 0,1713 | 5 |
| Adaptive mutation | 41180,00 | 42709,80 | 42458,00 | 43949,00 | 1155,87 | 0,1550 | 5 |

Adaptive mutation có mean thấp hơn 569,20 (khoảng 1,32%) và độ lệch chuẩn mẫu thấp hơn trong năm run; tuy nhiên best observed của nó là 41180, cao hơn 40302 của mutation cố định. Cần trình bày cả mean lẫn best để không tạo ấn tượng rằng mọi seed đều tốt hơn.

**Bật 2-opt trên dataset 48 thành phố:**

| Biến thể | Best | Mean | Median | Worst | Độ lệch chuẩn mẫu | Runtime trung bình (giây) | Evaluations trung bình | Runs |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Không dùng 2-opt | 40302,00 | 43279,00 | 44600,00 | 46230,00 | 2652,47 | 0,1713 | 7640 | 5 |
| Có dùng 2-opt | 82513,00 | 90549,20 | 91742,00 | 99086,00 | 7079,05 | 0,0913 | 8000 | 5 |

Số liệu đang lưu cho thấy cấu hình có 2-opt cho mean distance cao hơn đáng kể và runtime trung bình ngắn hơn; do đó output này **không chứng minh 2-opt cải thiện chất lượng nghiệm**. Code notebook đã được sửa để diễn giải phần trăm đúng chiều: mean distance tăng 109,22%, còn runtime giảm 46,70% so với baseline trong lần chạy này. Cần kiểm tra nguyên nhân chất lượng nghiệm xấu đi trước khi khuyến nghị 2-opt.

**Cấu hình kết hợp được notebook gọi là Best (All), trên dataset 48 thành phố:**

| Biến thể trên dataset 48 thành phố | Best | Mean | Median | Worst | Độ lệch chuẩn mẫu | Runtime trung bình (giây) | Runs |
|---|---:|---:|---:|---:|---:|---:|---:|
| Baseline | 40302,00 | 43279,00 | 44600,00 | 46230,00 | 2652,47 | 0,1713 | 5 |
| + Adaptive | 41180,00 | 42709,80 | 42458,00 | 43949,00 | 1155,87 | 0,1550 | 5 |
| + 2-opt | 82513,00 | 90549,20 | 91742,00 | 99086,00 | 7079,05 | 0,0913 | 5 |
| Best (All) | 37068,00 | 37443,80 | 37258,00 | 37890,00 | 413,33 | 0,0979 | 5 |

**Ghi chú về phép so sánh kết hợp:** kết quả NN được báo cáo riêng ở thí nghiệm dataset 26 thành phố và không còn được đưa vào bảng/biểu đồ tổng hợp 48 thành phố. Biểu đồ hội tụ ở cell 20 đã được sửa để chỉ so các run cùng dataset 48 thành phố. Best (All) có mean thấp hơn baseline 13,48% trong năm seed này; kết quả 2-opt riêng lẻ lại kém hơn baseline và cần được điều tra trước khi xem như một cải tiến.

Các hình NN initialization, adaptive mutation, 2-opt và Best (All) nằm lần lượt ở cell 8, 14, 17 và 20 của `Experiment_4_REVISED.ipynb`. Kết quả Tournament trên dataset 42 thành phố được xuất ở cell 11.

### 4.5. Độ nhạy tham số EHO

Experiment 5 đã chạy đủ 75/75 lượt trong thời gian notebook ghi là 25,68 giây. Mỗi cấu hình có năm run; bảng báo cáo best, mean, median, worst và độ lệch chuẩn mẫu. Hai sweep alpha/beta dùng dataset 15 thành phố; sweep số clan và separation dùng dataset 26 thành phố.

| Thử nghiệm | Giá trị cấu hình | Runs | Best | Mean distance | Median | Worst | Độ lệch chuẩn mẫu |
|---|---:|---:|---:|---:|---:|---:|---:|
| Alpha (15 thành phố) | 0,1 | 5 | 1804,0 | 1929,4 | 1976,0 | 2028,0 | 100,174 |
|  | 0,3 | 5 | 1448,0 | 1587,8 | 1570,0 | 1716,0 | 102,763 |
|  | 0,5 | 5 | **1430,0** | 1552,2 | 1560,0 | 1660,0 | 85,172 |
|  | 0,7 | 5 | 1539,0 | 1668,8 | 1672,0 | 1796,0 | 90,965 |
|  | 0,9 | 5 | 1678,0 | 1838,0 | 1808,0 | 2014,0 | 131,750 |
| Beta (15 thành phố) | 0,1 | 5 | 1517,0 | 1736,4 | 1735,0 | 1911,0 | 159,981 |
|  | 0,3 | 5 | 1539,0 | **1668,8** | 1672,0 | 1796,0 | 90,965 |
|  | 0,5 | 5 | 1500,0 | 1702,6 | 1752,0 | 1802,0 | 118,236 |
|  | 0,7 | 5 | 1636,0 | 1714,6 | 1698,0 | 1846,0 | 83,149 |
| Clan count, tổng quần thể 80 (26 thành phố) | 2 clan × 40 voi | 5 | **1367,0** | **1570,4** | 1573,0 | 1746,0 | 138,206 |
|  | 4 clan × 20 voi | 5 | 1509,0 | 1672,8 | 1693,0 | 1825,0 | 114,347 |
|  | 8 clan × 10 voi | 5 | 1655,0 | 1810,8 | 1836,0 | 1921,0 | 100,378 |
| Separation count/clan (26 thành phố) | 0 | 5 | 1574,0 | 1692,6 | 1679,0 | 1781,0 | 88,161 |
|  | 1 | 5 | 1509,0 | **1672,8** | 1693,0 | 1825,0 | 114,347 |
|  | 2 | 5 | 1617,0 | 1725,8 | 1724,0 | 1904,0 | 113,467 |

Trong phạm vi sweep này, alpha 0,5 có mean thấp nhất ở nhóm alpha; beta 0,3 có mean thấp nhất ở nhóm beta. Với tổng quần thể cố định là 80, cấu hình hai clan có mean thấp nhất trong các số clan đã thử. Separation count bằng 1 có mean thấp hơn các lựa chọn 0 và 2 trong nhóm này. Đây là quan sát trên đúng dataset, seed và ngân sách nêu trên; không phải kết luận về tham số tối ưu toàn cục. Bốn biểu đồ alpha, beta, clan count và separation count đã được tạo lại trong lần chạy notebook mới nhất, lần lượt ở các cell 5, 7, 9 và 11 của `Experiment5-EHO-Params.ipynb`; nếu báo cáo có ảnh xuất riêng từ lần chạy trước thì thay bằng các hình này.

### 4.6. So sánh GA và EHO

Experiment 6 chạy đủ 70/70 lượt trong 19,11 giây: bảy dataset, năm seed cho mỗi thuật toán, với ngân sách tối đa 6.000 objective evaluations/run. Mỗi cặp dataset/seed được chạy cho cả hai solver. Bảng dưới đây chép số run, best, mean, median, worst và độ lệch chuẩn mẫu từ output của cell 7.

| Dataset | EHO runs | EHO best | EHO mean | EHO median | EHO worst | EHO std | GA runs | GA best | GA mean | GA median | GA worst | GA std |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 03Cities-6 | 5 | 6,0 | 6,0 | 6,0 | 6,0 | 0,0 | 5 | 6,0 | 6,0 | 6,0 | 6,0 | 0,0 |
| 04Cities-189 | 5 | 189,0 | 189,0 | 189,0 | 189,0 | 0,0 | 5 | 189,0 | 189,0 | 189,0 | 189,0 | 0,0 |
| 06Cities-1248 | 5 | 1248,0 | 1248,0 | 1248,0 | 1248,0 | 0,0 | 5 | 1248,0 | 1248,0 | 1248,0 | 1248,0 | 0,0 |
| 15Cities-1194 | 5 | 1539,0 | 1668,8 | 1672,0 | 1796,0 | 90,965 | 5 | 1194,0 | 1200,2 | 1194,0 | 1225,0 | 13,864 |
| 26Cities-937 | 5 | 1509,0 | 1672,8 | 1693,0 | 1825,0 | 114,347 | 5 | 960,0 | 1056,4 | 1045,0 | 1148,0 | 72,844 |
| 42Cities-699 | 5 | 1961,0 | 2015,2 | 2003,0 | 2107,0 | 55,002 | 5 | 1137,0 | 1166,2 | 1163,0 | 1202,0 | 26,281 |
| 48Cities-33523 | 5 | 100054,0 | 103202,6 | 104397,0 | 104711,0 | 2035,519 | 5 | 47650,0 | 54194,4 | 54959,0 | 57933,0 | 3861,499 |

Trên ba dataset nhỏ, hai thuật toán đạt cùng các giá trị trong năm seed. Trên bốn dataset từ 15 đến 48 thành phố, GA có mean và best observed thấp hơn EHO trong batch này. Đây là so sánh của hai cấu hình cụ thể dưới cùng giới hạn objective evaluations, không tách riêng ảnh hưởng của mọi tham số nội bộ; kết quả không đủ để kết luận một thuật toán luôn tốt hơn trong mọi cấu hình. Biểu đồ hội tụ dùng seed 11 trên dataset 48 thành phố: tại 6.000 evaluations, output ghi EHO đạt 104397 và GA đạt 57933. Cần cập nhật hình này từ cell 9 của `Experiment6-EHO-vs-GA.ipynb` nếu báo cáo có chèn ảnh.

### 4.7. Danh sách hình cần cập nhật khi chèn vào bản báo cáo

Notebook đã lưu hình ở lần chạy mới, nhưng các hình đã xuất riêng hoặc chèn vào báo cáo từ lần chạy cũ cần được thay bằng hình hiện tại. Dùng cell được liệt kê dưới đây làm nguồn; không lấy lại ảnh từ bản báo cáo cũ:

| Nội dung hình | Notebook | Cell tạo hình |
|---|---|---:|
| Hội tụ baseline trên 15 thành phố | `Experiment_1-2_REVISED.ipynb` | 4 |
| So sánh selection | `Experiment_1-2_REVISED.ipynb` | 9 |
| So sánh mutation | `Experiment_1-2_REVISED.ipynb` | 16 |
| Phân phối/độ lệch theo từng dataset | `Experiment_3_REVISED.ipynb` | 8, 11, 14, 17, 20, 23, 26 |
| Tổng hợp xu hướng theo kích thước | `Experiment_3_REVISED.ipynb` | 31 |
| Nearest Neighbor initialization | `Experiment_4_REVISED.ipynb` | 8 |
| Adaptive mutation | `Experiment_4_REVISED.ipynb` | 14 |
| 2-opt | `Experiment_4_REVISED.ipynb` | 17 |
| So sánh hội tụ các cấu hình cùng dataset 48 thành phố (đã loại run NN của dataset 26) | `Experiment_4_REVISED.ipynb` | 20 |
| Sweep alpha, beta, số clan, separation | `Experiment5-EHO-Params.ipynb` | 5, 7, 9, 11 |
| Đường hội tụ EHO–GA trên 48 thành phố | `Experiment6-EHO-vs-GA.ipynb` | 9 |

## CHƯƠNG 5. KẾT LUẬN

### 5.1. Các kết quả đạt được

### Ghi chú ảnh giao diện cần bổ sung vào mục 5.1

- **Hình 5.1 - Màn hình chính:** mở `python -m ga_eho_tsp.gui`, chụp form có dataset và nhóm tham số hiển thị.
- **Hình 5.2 - Kết quả tuyến đường:** chạy một dataset thật, chụp route và distance trên GUI. Caption cần ghi dataset, seed và stopping reason.
- **Hình 5.3 - Đồ thị hội tụ:** chụp tab convergence sau khi run kết thúc; giữ rõ nhãn trục và tên thuật toán.
- **Hình 5.4 - Cấu hình/kết quả EHO:** chỉ chụp sau khi chọn EHO và chạy thành công. Không dùng ảnh placeholder hoặc ảnh không tương ứng với output thật.

Lưu ảnh trong `docs/screenshots/`; có thể chèn bằng `![Hình 5.1 - Màn hình chính](screenshots/...)`. Ảnh do nhóm tự chụp từ GUI; phiên rà soát này không chạy chương trình để tạo ảnh.

Đồ án đã triển khai thành công hai thuật toán metaheuristic cho bài toán TSP:

**1. Genetic Algorithm (GA):**
- Cài đặt đầy đủ với nhiều biến thể toán tử
- Hỗ trợ 3 phương pháp selection: Tournament, Rank, Roulette Wheel
- Hỗ trợ 2 phương pháp crossover: Order Crossover (OX), Partially Mapped Crossover (PMX)
- Hỗ trợ 4 phương pháp mutation: Inversion, Swap, Insertion, Scramble
- Hỗ trợ 3 phương pháp khởi tạo: Random, Nearest-Neighbor, Mixed
- Cài đặt Elitism, Global Best Archive, Adaptive Mutation, Bounded 2-opt Local Search
- Hỗ trợ điều kiện dừng linh hoạt: generations, max_evaluations, time_limit, stagnation

**2. Discrete Elephant Herding Optimization (D-EHO):**
- Điều chỉnh EHO cho không gian hoán vị
- Cài đặt Guided-Swap để cập nhật vị trí rời rạc
- Tính Hamming Medoid làm tâm clan
- Cơ chế Separation với permutation ngẫu nhiên
- Elitism hai cấp: Clan Archive và Global Best

**3. Kết quả thực nghiệm:**
- Đã cập nhật kết quả GA từ các notebook: Experiment 3 có 35/35 run trên bảy bộ dữ liệu; Experiment 1–2 khảo sát selection, crossover và mutation; Experiment 4 khảo sát NN initialization, adaptive mutation và 2-opt với các giới hạn đã nêu ở Chương 4.
- Hai notebook EHO đã có output: Experiment 5 hoàn tất 75/75 run khảo sát tham số; Experiment 6 hoàn tất 70/70 run so sánh GA–EHO. Trong batch và cấu hình cụ thể ở Chương 4, GA có mean distance thấp hơn EHO ở bốn dataset từ 15 đến 48 thành phố, còn ba dataset nhỏ cho kết quả bằng nhau.
- Kết luận so sánh chỉ giới hạn trong dataset, seed, ngân sách và cấu hình đã chạy; không khái quát thành ưu thế tuyệt đối của một thuật toán.

**4. Giao diện và công cụ:**
- GUI Tkinter cho phép thử nghiệm dễ dàng
- CLI hỗ trợ validate dữ liệu và chạy benchmark
- Jupyter notebooks cho phân tích chi tiết

### 5.2. Những hạn chế và hướng phát triển

**Hạn chế hiện tại:**

1. **Về thuật toán:**
   - Chỉ hỗ trợ Symmetric TSP
   - Không bảo đảm tìm optimum toàn cục
   - Solver hiện hỗ trợ Tournament, Rank và Roulette Wheel; chưa có Mixed selection, do đó không có kết quả so sánh operator này trong các thực nghiệm
   - Kết quả D-EHO và GA hiện có năm seed cho mỗi cấu hình trong Experiment 6; cần mở rộng seed và cấu hình trước khi xem kết quả là đánh giá tổng quát.

2. **Về dữ liệu:**
   - Chưa có known optimum được xác minh cho các bài lớn
   - Bộ dữ liệu giới hạn (tối đa 48 thành phố)

3. **Về thực nghiệm:**
   - GA+2-opt cần cân bằng lại evaluation budget
   - Adaptive Mutation cần điều chỉnh tham số
   - Chưa có so sánh với các solver khác (OR-Tools, Concorde)

**Hướng phát triển:**

1. **Mở rộng bài toán:**
   - Hỗ trợ Asymmetric TSP
   - Hỗ trợ TSP with Time Windows
   - Hỗ trợ Multiple TSP

2. **Cải tiến thuật toán:**
   - Hybrid GA-EHO kết hợp ưu điểm của cả hai
   - Tích hợp thêm local search hiệu quả (Lin-Kernighan, 3-opt)
   - Parallel/Distributed GA để tăng tốc

3. **Thực nghiệm nâng cao:**
   - So sánh với TSPLIB benchmark instances
   - So sánh với các solver state-of-the-art
   - Phân tích chi tiết complexity và convergence rate

4. **Công cụ:**
   - Visualization tool cho evolution process
   - Auto-tuning tham số bằng Bayesian Optimization
   - Web interface để demo online

---

## TÀI LIỆU THAM KHẢO

[1] Holland, J. H. (1975). *Adaptation in Natural and Artificial Systems*. University of Michigan Press. [Google Books](https://books.google.com/books?id=JE5RAAAAMAAJ).

[2] Goldberg, D. E. (1989). *Genetic Algorithms in Search, Optimization, and Machine Learning*. Addison-Wesley. [Google Books](https://books.google.com/books?vid=ISBN9780201157673).

[3] Applegate, D. L., Bixby, R. E., Chvátal, V., & Cook, W. J. (2006). *The Traveling Salesman Problem: A Computational Study*. Princeton University Press. [Publisher](https://press.princeton.edu/books/ebook/9781400841103/the-traveling-salesman-problem-0).

[4] Dantzig, G. B., Fulkerson, D. R., & Johnson, S. M. (1954). Solution of a large-scale traveling-salesman problem. *Operations Research, 2*(4), 393–410. [DOI](https://doi.org/10.1287/opre.2.4.393).

[5] Reinelt, G. (1991). TSPLIB - A traveling salesman problem library. *ORSA Journal on Computing, 3*(4), 376–384. [DOI](https://doi.org/10.1287/ijoc.3.4.376).

[6] Oliver, I. M., Smith, D. J., & Holland, J. R. C. (1987). A study of permutation crossover operators on the traveling salesman problem. In *Proceedings of the Second International Conference on Genetic Algorithms*, 224–230. [Bibliographic record](https://scispace.com/papers/a-study-of-permutation-crossover-operators-on-the-traveling-1trgqpnkfa).

[7] Whitley, D., Starkweather, T., & Fuquay, D. (1989). Scheduling problems and traveling salesmen: the genetic edge recombination operator. In *Proceedings of the Third International Conference on Genetic Algorithms*. [DBLP](https://dblp.org/rec/conf/icga/WhitleySF89.html).

[8] Wang, G.-G., Deb, S., & dos Santos Coelho, L. (2015). Elephant herding optimization. In *2015 3rd International Symposium on Computational and Business Intelligence*. [DOI](https://doi.org/10.1109/ISCBI.2015.8).

[9] Wang, G.-G., Deb, S., Gao, X.-Z., & dos Santos Coelho, L. (2016). A new metaheuristic optimisation algorithm motivated by elephant herding behaviour. *International Journal of Bio-Inspired Computation, 8*(6), 394–409. [DOI](https://doi.org/10.1504/IJBIC.2016.081335).

[10] Slowik, A. (Ed.). (2020). *Swarm Intelligence Algorithms: A Tutorial*. CRC Press. [Publisher search](https://www.routledge.com/search?kw=Swarm%20Intelligence%20Algorithms%20A%20Tutorial).

[11] Stützle, T. (1998). *Local Search Algorithms for Combinatorial Problems*. PhD dissertation, TU Darmstadt. [Repository](https://tuprints.ulb.tu-darmstadt.de/).

[12] Wolpert, D. H., & Macready, W. G. (1997). No free lunch theorems for optimization. *IEEE Transactions on Evolutionary Computation, 1*(1), 67–82. [DOI](https://doi.org/10.1109/4235.585893).

[13] Python Software Foundation. *random - Generate pseudo-random numbers*. [Official documentation](https://docs.python.org/3/library/random.html).

[14] Python Software Foundation. *tkinter - Python interface to Tcl/Tk*. [Official documentation](https://docs.python.org/3/library/tkinter.html).

[15] Matplotlib Development Team. *Matplotlib documentation*. [Official documentation](https://matplotlib.org/stable/).

[16] Project Jupyter. *Jupyter Notebook documentation*. [Official documentation](https://docs.jupyter.org/en/latest/).

[17] pytest contributors. *pytest documentation*. [Official documentation](https://docs.pytest.org/en/stable/).

[18] Python Packaging Authority. *Packaging Python Projects*. [Official guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

[19] Google OR-Tools. *Traveling Salesperson Problem*. [Official guide](https://developers.google.com/optimization/routing/tsp).

[20] Nhóm dự án. `GUIDELINES.md`, `docs/architecture.md`, `docs/algorithm_ga.md`, `docs/algorithm_eho.md`, `docs/discrete_eho_analysis.md`, `docs/experiments.md` và `docs/source_attribution.md`. [Repository](https://github.com/datweb07/ga-eho-tsp).

---

## PHỤ LỤC

### A. Hướng dẫn cài đặt

#### Yêu cầu môi trường
- Python 3.11 trở lên
- Hệ điều hành: Windows 10/11, macOS, Linux
- RAM: Tối thiểu 4GB

#### Cài đặt môi trường

**Bước 1: Tạo virtual environment**
```bash
python --version  # Kiểm tra Python >= 3.11
python -m venv .venv
```

**Bước 2: Kích hoạt môi trường**

Windows (PowerShell):
```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
source .venv/bin/activate
```

**Bước 3: Cài đặt thư viện**
```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

#### Chạy chương trình

**Giao diện GUI:**
```bash
python -m ga_eho_tsp.gui
```

**Hoặc sử dụng script Demo:**
```bash
python Demo.py
```

**Kiểm tra dữ liệu:**
```bash
python -m ga_eho_tsp.cli validate
```

### B. Cấu trúc repository

```
ga-eho-tsp/
├── data/                    # Bộ dữ liệu TSP
├── src/ga_eho_tsp/         # Source code chính
│   ├── algorithms/         # GA và EHO implementation
│   │   ├── ga/            # Genetic Algorithm
│   │   └── eho/           # Elephant Herding Optimization
│   ├── domain/            # Models và objective functions
│   ├── experiments/       # Benchmark utilities
│   ├── gui/              # Tkinter GUI
│   └── cli.py            # Command-line interface
├── Experiment/            # Jupyter notebooks
├── docs/                 # Documentation
├── tests/                # Unit tests
└── Demo.py              # Demo script
```

### C. Phân công công việc nhóm

| Thành viên | Nhiệm vụ |
|------------|----------|
| Trương Thành Đạt | Triển khai GA core algorithms, GUI, tổng hợp báo cáo |
| Nguyễn Tấn Khiêm | Triển khai EHO algorithms, experiments |
| Nguyễn Phương Chinh | Data processing, validation, documentation |
| Lại Thành Đạt | Testing, benchmarking, visualization |
