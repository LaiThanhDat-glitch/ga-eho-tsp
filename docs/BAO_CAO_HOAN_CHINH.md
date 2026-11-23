

**BỘ GIÁO DỤC VÀ ĐÀO TẠO ĐẠI HỌC KINH TẾ TP HỒ CHÍ MINH (UEH) TRƯỜNG CÔNG NGHỆ VÀ THIẾT KẾ** 



<!-- Start of picture text -->
College of<br>Technology<br>n ign<br>UNIveRsITY (274 Desig<br><!-- End of picture text -->

# **ĐỒ ÁN MÔN HỌC** 

**ĐỀ TÀI** 

**Ứng dụng Thuật toán Genetic Algorithm và Elephant Herding Optimization cho Bài toán Người Du Lịch (Traveling Salesman Problem - TSP)** 

**Học Phần: Trí Tuệ Nhân Tạo Danh Sách Nhóm** : 

**1.** TRƯƠNG THÀNH ĐẠT 

**2.** NGUYỄN TẤN KHIÊM 

**3.** NGUYỄN PHƯƠNG CHINH 

**4.** LẠI THÀNH ĐẠT 

**Chuyên Ngành** : CÔNG NGHỆ THÔNG TIN **Khóa** : K50 **Giảng Viên** : TS. Đặng Ngọc Hoàng Thành f TP. Hé Chi Minh , ngay 30thang 10 nam 20267 

## **MỤC LỤC** 

|**MỤC LỤC..................................................................................................................... 2**<br>|
|---|
|**CHƯƠNG 1. TỔNG QUAN.........................................................................................4**|
|1.1. Giới thiệu bài toán người du lịch....................................................................... 4|
|1.2. Phát biểu bài toán...............................................................................................5<br>|
|1.3. Độ phức tạp và lý do sử dụng thuật toán tìm kiếm............................................ 6<br>|
|1.4. Hướng tiếp cận giải quyết.................................................................................. 6|
|**CHƯƠNG 2. GIẢI THUẬT DI TRUYỀN................................................................. 8**|
|2.1. Giới thiệu về Genetic Algorithm........................................................................8|
|2.2. Cách áp dụng GA cho bài toán TSP...................................................................9|
|2.2.1. Luồng xử lý tổng quát................................................................................9|
|a) Random initialization (mặc định)............................................................ 10|
|b) Nearest-neighbor initialization (tùy chọn)...............................................11|
|c) Mixed initialization (tùy chọn).................................................................11|
|a) Tournament Selection (mặc định)............................................................12|
|b) Rank Selection (tùy chọn)........................................................................12|
|c) Roulette Wheel Selection (tùy chọn)....................................................... 12|
|a) Order Crossover - OX (mặc định)............................................................13|
|b) Partially Mapped Crossover - PMX (tùy chọn).......................................15<br>|
|2.2.5. Đột biến................................................................................................... 15|
|a) Inversion Mutation (mặc định)................................................................ 16|
|b) Swap Mutation (tùy chọn)....................................................................... 17|
|c) Insertion Mutation (tùy chọn).................................................................. 17|
|d) Scramble Mutation (tùy chọn)................................................................. 17|
|2.2.7. Điều kiện dừng và lịch sử........................................................................18|
|a) Stagnation Stopping................................................................................. 20|
|b) Adaptive Mutation................................................................................... 20|
|c) Bounded 2-opt Local Search....................................................................21<br>|
|2.2.9. Tổ chức mã nguồn................................................................................... 22|
|**CHƯƠNG 3. THUẬT TOÁN ELEPHANT HERDING OPTIMIZATION..........23**|
|3.1. Tổng quan về Elephant Herding Optimization................................................ 23|
|3.1.1. Khái niệm EHO....................................................................................... 23|
|3.1.2. Nguyên lý hành vi đàn voi.......................................................................23|
|3.1.3. Các thành phần chính của EHO...............................................................23|
|3.2. Áp dụng EHO cho bài toán TSP...................................................................... 24|
|3.2.1. Biểu diễn nghiệm và hàm mục tiêu...............................................................25|
|3.2.2. Phân chia quần thể thành các Clan................................................................25|
|3.2.3. Cập nhật Matriarch........................................................................................26|



|3.2.4. Di chuyển voi thường (Clan Updating Operator)......................................... 27|
|---|
|3.2.5. Tách đàn (Separating Operator).................................................................... 28|
|3.2.6. Cơ chế bảo tồn nghiệm tốt nhất (Elitism)..................................................... 29|
|3.3. Quy trình hoạt động của D-EHO......................................................................31<br>|
|3.3.1. Sơ đồ luồng thuật toán.............................................................................31|
|3.3.2. Giả mã (Pseudocode)...............................................................................31<br>|
|3.3.3. Giải thích quá trình cập nhật một thế hệ..................................................32|
|3.4. Triển khai thuật toán trong chương trình..........................................................32<br>|
|3.4.1. Cấu trúc các module................................................................................ 32<br>|
|3.4.2. Các tham số cấu hình...............................................................................34|
|3.4.3. Điều kiện dừng và quản lý đánh giá........................................................ 34|
|3.5. Nhận xét và giới hạn của D-EHO.................................................................... 35|
|3.5.1. Ưu điểm................................................................................................... 35|
|3.5.2. Hạn chế.................................................................................................... 35|
|3.5.3. Khả năng áp dụng cho TSP..................................................................... 36|
|**CHƯƠNG 3. CÁC KẾT QUẢ THỰC NGHIỆM.................................................... 37**|
|3.1. Thiết kế thực nghiệm........................................................................................37|
|3.1.1. Bộ dữ liệu................................................................................................ 37|
|3.1.2. Cấu hình thực nghiệm..............................................................................37|
|3.2. Kết quả so sánh toán tử trên bài 15 thành phố................................................. 38|
|3.3. Phân phối kết quả theo kích thước bài toán..................................................... 39|
|3.4. Khởi tạo nâng cao, Adaptive Mutation và 2-opt..............................................40|
|3.5. Benchmark trên bảy bộ dữ liệu........................................................................ 42|
|**CHƯƠNG 4. KẾT LUẬN.......................................................................................... 44**|
|4.1. Các kết quả đạt được........................................................................................44|
|4.2. Những hạn chế và hướng phát triển................................................................. 44<br>|
|**TÀI LIỆU THAM KHẢO..........................................................................................45**|
|**PHỤ LỤC.....................................................................................................................46**|



## **CHƯƠNG 1. TỔNG QUAN** 

### **1.1. Giới thiệu bài toán người du lịch** 

Bài toán người du lịch (Traveling Salesman Problem - TSP) là một trong những bài toán tối ưu tổ hợp được nghiên cứu nhiều nhất trong khoa học máy tính và toán học rời rạc. Bài toán mô tả tình huống một người cần đi thăm một tập thành phố, mỗi thành phố được thăm đúng một lần, bắt đầu và kết thúc tại cùng một điểm xuất phát. Mục tiêu là xác định thứ tự thăm sao cho tổng chi phí di chuyển của toàn bộ chuyến đi là nhỏ nhất. 

TSP có ứng dụng thực tiễn rộng rãi: lập lịch phân phối hàng hóa, định tuyến mạch in điện tử (PCB drilling), lập kế hoạch sản xuất, định tuyến robot công nghiệp và nhiều bài toán quy hoạch khác, trong đó mục tiêu là tìm chu trình ngắn nhất qua một tập điểm cho trước. 

Trong đồ án này, chi phí di chuyển giữa các thành phố được biểu diễn bằng ma trận khoảng cách đối xứng. Phần tử tại hàng i, cột j của ma trận chứa chi phí đi từ thành phố i đến thành phố j. Vì tính đối xứng, chi phí đi từ i đến j bằng chi phí đi từ j về i, tức là chúng ta đang giải **Symmetric TSP** . 



<!-- Start of picture text -->
2<br>1<br>1<br>Origin<br>1<br>7 5<br><——_——_®<br>3<br><!-- End of picture text -->

_Hình 1.1 - Ví dụ bài toán TSP với 5 thành phố_ 

Hình 1.1 minh họa một bài TSP nhỏ với 5 thành phố. Mỗi nút tròn biểu diễn một thành phố, các mũi tên thể hiện hành trình được chọn với khoảng cách tương ứng 

ghi trên mỗi cạnh. Mục tiêu là tìm chu trình đi qua tất cả 5 thành phố với tổng khoảng cách nhỏ nhất. 

### **1.2. Phát biểu bài toán** 

**Đầu vào:** Tập thành phố 𝑉= 0, 1, ..., 𝑛−1 và ma trận khoảng cách  kích thước 𝐷 𝑛× 𝑛, trong đó 𝐷𝑖𝑗 là chi phí đi từ thành phố  đến thành phố . 𝑖 𝑗 

**Điều kiện:** Ma trận  phải thỏa mãn: 𝐷 

- Vuông: kích thước 𝑛× 𝑛 với 𝑛≥3 

- Đường chéo bằng 0: 𝐷𝑖𝑖 = 0 

- Đối xứng: 𝐷𝑖𝑗 = 𝐷𝑗𝑖 

- Các phần tử hữu hạn và không âm 

**Biểu diễn nghiệm:** Một hành trình hợp lệ là hoán vị  của tất cả thành phố, với quy π ước π[0] = 0 (cố định thành phố 0 làm điểm xuất phát). Trong hệ thống, route được lưu dưới dạng tuple số nguyên 0-based, ví dụ (0, 3, 2, 1) cho bài toán 4 thành phố. 

**Hàm mục tiêu:** Chi phí của hành trình  được tính là: π 



Trong đó số hạng cuối 𝐷[π[𝑛−1], π[0]] là chi phí quay trở về thành phố xuất phát, tạo thành chu trình khép kín. Hàm này được cài đặt trong domain/objective.py thông qua route_length, sử dụng math.fsum để tích lũy chính xác: 

Python def route_length(route: Sequence[int], matrix: Matrix) -> float: """Tính từng cạnh và cạnh cuối về 0 đúng một lần; không sửa input.""" validate_route(route, len(matrix)) try: total = fsum(matrix[route[i]][route[(i+1) % len(route)]] for i in range(len(route))) except OverflowError as error: raise ValueError("Tổng khoảng cách vượt miền số hữu hạn.") from error if not isfinite(total): raise ValueError("Tổng khoảng cách vượt miền số hữu hạn.") return total * **Mục tiêu:** Tìm π sao cho 𝐿(π*) là nhỏ nhất trong tất cả các hoán vị hợp lệ: 

π* = arg min 𝐿(π) π 

Một nghiệm  được xem là hợp lệ khi thỏa mãn đồng thời ba điều kiện: π 

1. Có đúng  phần tử 𝑛 

2. Bắt đầu bằng thành phố 0 

3. Mỗi thành phố từ  đến 0 𝑛−1 xuất hiện đúng một lần 

### **1.3. Độ phức tạp và lý do sử dụng thuật toán tìm kiếm** 

TSP thuộc lớp bài toán NP-Hard. Số lượng hành trình phân biệt với  thành phố 𝑛 (khi cố định điểm xuất phát) là (𝑛−1)!. Với 𝑛= 10 đã có 9! = 362. 880 hoán 17 vị, với 𝑛= 20 con số này vượt 1, 2 × 10 . Liệt kê toàn bộ hành trình để tìm nghiệm tối ưu là điều không khả thi trong thực tế với các bài toán kích thước trung bình trở lên. 

Bảng dưới đây minh họa sự tăng trưởng bùng nổ của không gian tìm kiếm: 

|**Số thành phố ( )**<br>𝑛|**Số hành trình**<br>(𝑛−1)!|
|---|---|
|3|2|
|6|120|
|10|362.880|
|15|87.178.291.200|
|20|1, 2 × 10<br>17|
|26|≈1, 6 × 10<br>25|



Vì vậy, các phương pháp heuristic và metaheuristic, trong đó có Genetic Algorithm và Elephant Herding Optimization được dùng để tìm nghiệm đủ tốt trong thời gian hợp lý, thay vì nghiệm tối ưu tuyệt đối. 

### **1.4. Hướng tiếp cận giải quyết** 

Đồ án triển khai hai thuật toán metaheuristic để giải TSP: 

- **Genetic Algorithm (GA):** Mô phỏng quá trình tiến hóa tự nhiên, duy trì một quần thể gồm nhiều hành trình ứng viên, chọn lọc các cá thể tốt, kết hợp chúng để tạo thế hệ mới và áp dụng đột biến để khám phá vùng tìm kiếm mới. GA đã được triển khai đầy đủ trong dự án. 

- **Elephant Herding Optimization (EHO):** Mô phỏng hành vi đàn voi, chia quần thể thành các clan, cập nhật vị trí mỗi voi theo matriarch (cá thể tốt nhất trong clan) và tách các voi đực kém nhất khỏi clan. Phần EHO đang trong giai đoạn phát triển. 

Cả hai thuật toán dùng chung biểu diễn route, hàm mục tiêu TSPProblem.route_length, cơ chế seed và cấu trúc kết quả RunResult được định nghĩa trong domain/. 

## **CHƯƠNG 2. GIẢI THUẬT DI TRUYỀN** 

### **2.1. Giới thiệu về Genetic Algorithm** 

Genetic Algorithm (GA) là một lớp thuật toán tìm kiếm và tối ưu được Holland giới thiệu vào những năm 1970, lấy cảm hứng từ quá trình tiến hóa sinh học theo thuyết chọn lọc tự nhiên của Darwin. Thay vì chỉ duy trì một nghiệm duy nhất, GA duy trì một quần thể (population) gồm nhiều nghiệm ứng viên, gọi là cá thể (individual). Trong mỗi vòng lặp (generation), thuật toán: 

1. **Đánh giá** chất lượng (fitness) của từng cá thể 

2. **Chọn lọc** các cá thể tốt làm cha mẹ (selection) 

3. **Lai ghép** (crossover) để tạo cá thể con kế thừa đặc điểm của cha mẹ 

4. **Đột biến** (mutation) để duy trì sự đa dạng và khám phá vùng mới 

5. **Hình thành** quần thể thế hệ tiếp theo 

Ưu điểm của GA so với tìm kiếm cục bộ đơn giản là khả năng khám phá không gian tìm kiếm song song từ nhiều hướng khác nhau, giảm nguy cơ mắc kẹt tại nghiệm cục bộ. GA cũng linh hoạt vì không yêu cầu hàm mục tiêu có tính khả vi. 

Một điểm khác biệt quan trọng khi áp dụng GA cho TSP là biểu diễn cá thể. Biểu diễn bit nhị phân thông thường không phù hợp vì một hành trình TSP phải là hoán vị, không được phép lặp hoặc bỏ sót thành phố. Dự án dùng permutation representation: mỗi cá thể là một tuple chứa đầy đủ  thành phố, với quy ước thành 𝑛 phố 0 luôn đứng đầu. Các toán tử crossover và mutation chỉ thao tác trên phần tail (phần route từ vị trí 1 trở đi) để không làm mất tính hợp lệ của hoán vị. 

#### **Sơ đồ tổng quát của Genetic Algorithm:** 



### **2.2. Cách áp dụng GA cho bài toán TSP** 

## **2.2.1. Luồng xử lý tổng quát** 

Vòng lặp GA được cài đặt tập trung trong algorithms/ga/solver.py. Quy trình một lần chạy hoàn chỉnh gồm các bước chính như sau: 

1. **Kiểm tra đầu vào:** Xác nhận TSPProblem và GAConfig hợp lệ, bao gồm kiểm tra giới hạn tham số, ma trận khoảng cách và ngân sách tính toán. 

2. **Khởi tạo quần thể:** Tạo population_size route ban đầu theo phương thức đã chọn (ngẫu nhiên, nearest-neighbor hoặc mixed). Mỗi route là hoán vị hợp lệ với thành phố 0 đứng đầu. 

3. **Đánh giá khởi tạo:** Tính chi phí cho toàn bộ quần thể ban đầu bằng TSPProblem.route_length, đếm số lần đánh giá và lưu global best. 

4. **Ghi snapshot ban đầu (iteration 0):** IterationStat lưu best trong quần thể hiện tại, global best, mean fitness, số evaluations, thời gian và diversity. 

5. **Vòng lặp thế hệ:** Với mỗi thế hệ, kiểm tra điều kiện dừng, sao chép elites, chuẩn bị selection, chọn cha mẹ, lai ghép, đột biến, đánh giá con, áp dụng local search nếu được bật, cập nhật global best. 

6. **Commit thế hệ:** Chỉ commit khi quần thể mới đầy đủ population_size cá thể. Nếu dừng giữa thế hệ, các candidate đã được đánh giá vẫn được tính vào global best nhưng quần thể dở dang không được commit. 

7. **Trả kết quả:** RunResult chứa global best của toàn bộ lần chạy (không chỉ route tốt nhất trong quần thể cuối). 

#### **Pseudocode vòng lặp GA:** 

Python kiểm tra problem và config rng = Random(config.seed) population = khởi_tạo(population_size, rng) costs = [route_length(r) for r in population] best_route, best_distance = best(population, costs) ghi snapshot iteration=0 

for iteration in 1..min(generations, max_iterations): kiểm tra stop / time_limit / max_evaluations 

next_pop, next_costs = select_elites(population, costs, elite_count) selector = prepare_selection(population, costs, method, k) rate = effective_mutation_rate(config, stagnation, diversity) while len(next_pop) < population_size: kiểm tra stop 

p1, p2 = selector.pick(rng), selector.pick(rng) children = crossover(p1, p2, rng) if rng.random() < crossover_rate else (p1, p2) for child in children: child = mutate(child, rate, rng, mutation_method) cost = route_length(child)        # evaluations++ cập nhật best_route, best_distance if local_search_enabled: child, cost = improve(child, cost, ...) next_pop.append(child) commit: population, costs = next_pop, next_costs cập nhật stagnation, ghi history kiểm tra STAGNATION ghi snapshot cuối trả RunResult(best_route, best_distance, ...) 

#### **Sơ đồ kiến trúc module:** 



## **2.2.2. Khởi tạo quần thể và seed** 

Module algorithms/ga/initialization.py cung cấp ba phương thức khởi tạo: 

## **a) Random initialization (mặc định)** 

Mỗi route được sinh bằng cách tạo hoán vị ngẫu nhiên của  thành phố, sau đó xoay 𝑛 để thành phố 0 đứng đầu. Toàn bộ quá trình dùng rng riêng của lần chạy, không ảnh hưởng RNG toàn cục, đảm bảo tái lập kết quả khi giữ nguyên seed. 

Python def nearest_neighbor(problem: TSPProblem, start: int) -> Route: """Tham lam từ start, tie theo city nhỏ nhất; rotate để city 0 đứng đầu.""" remaining = set(range(problem.dimension)) remaining.remove(start) route = [start] 

while remaining: row = problem.distance_matrix[route[-1]] city = min(remaining, key=lambda candidate: (row[candidate], candidate)) route.append(city) remaining.remove(city) zero = route.index(0) return tuple(route[zero:] + route[:zero]) def initialize( dimension: int, population_size: int, rng: Random, *, problem: TSPProblem | None = None, method: str = "random", nn_seed_fraction: float = 0.25, ) -> list[Route]: """Random mặc định; NN đa start hoặc mixed floor(P×fraction), không ép unique.""" if method == "random": return [random_permutation(dimension, rng) for _ in range(population_size)] ... count = population_size if method == "nearest_neighbor" else int(population_size * nn_seed_fraction) routes: list[Route] = [] while len(routes) < count: starts = rng.sample(range(dimension), dimension) for start in starts[:count-len(routes)]: routes.append(nearest_neighbor(problem, start)) routes.extend(random_permutation(dimension, rng) for _ in range(population_size-count)) return routes 

## **b) Nearest-neighbor initialization (tùy chọn)** 

Thuật toán tham lam: bắt đầu từ một thành phố, tại mỗi bước chọn thành phố chưa thăm gần nhất (nếu bằng nhau thì chọn thành phố có chỉ số nhỏ hơn). Mỗi route NN được sinh từ một điểm bắt đầu khác nhau, tránh nhân bản một route duy nhất. 

## **c) Mixed initialization (tùy chọn)** 

Kết hợp một phần route NN (tỷ lệ nn_seed_fraction, mặc định 25%) và phần còn lại là random. Phương án này đặt một số nghiệm chất lượng tốt vào quần thể ban đầu trong khi vẫn giữ sự đa dạng. 

#### **Sơ đồ ba phương thức khởi tạo:** 



## **2.2.3. Chọn cha mẹ** 

Module algorithms/ga/selection.py cài đặt ba phương pháp selection, tất cả đều hỗ trợ minimization (chi phí nhỏ hơn = tốt hơn). Distribution của rank và roulette được chuẩn bị một lần mỗi thế hệ thông qua prepare_selection, rồi dùng nhiều lần để chọn cha mẹ, tránh tính lại và đảm bảo nhất quán trong một thế hệ. 

## **a) Tournament Selection (mặc định)** 

Lấy ngẫu nhiên tournament_size cá thể (mặc định 𝑘= 3), chọn cá thể có chi phí thấp nhất trong nhóm. Hai lần chọn cha mẹ độc lập nhau; cùng một route có thể được chọn hai lần. 

Python def pick(self, rng: Random) -> Route: if self.method == "tournament": indices = rng.sample(range(len(self.population)), self.tournament_size) return self.population[min(indices, key=lambda index: self.costs[index])] 

## **b) Rank Selection (tùy chọn)** 

Sắp xếp cá thể từ tốt đến kém, gán trọng số 𝑃, 𝑃−1, ..., 1 theo thứ hạng. Cách này làm giảm áp lực chọn lọc khi có vài cá thể vượt trội, giúp duy trì đa dạng quần thể. 

## **c) Roulette Wheel Selection (tùy chọn)** 

Chuyển chi phí thành trọng số bằng công thức weight_i = 1 - cost_i / max_cost. Cá thể có chi phí thấp hơn có trọng số cao hơn và xác suất được chọn lớn hơn. Trường 

hợp đặc biệt (tất cả chi phí bằng nhau hoặc max_cost = 0) được xử lý bằng cách chọn đều. 

#### **Sơ đồ ba phương pháp selection:** 



<!-- Start of picture text -->
Lay k ca thé<br>tournament ngau nhién<br>Chon min cost<br>Sp xép theo<br>Selection cost<br>Method i>} Trong séoy  P,A  P-1, >CaAG thé cha me<br>Chon theo trong<br>sé<br>weight_i=1-<br>cost_i/max<br>roulette_wheel———_—_—_—_—___» Chonon theosotheo trongtro<br>(xi ly all-zero<br>dc biét)<br><!-- End of picture text -->

## **2.2.4. Lai ghép permutation** 

Module algorithms/ga/crossover.py cài đặt hai toán tử lai ghép. Cả hai đều chỉ thao tác trên phần tail (vị trí 1 trở đi), không đổi vị trí thành phố 0, đảm bảo con sinh ra là permutation hợp lệ. 

#### **a) Order Crossover - OX (mặc định)** 

OX bảo tồn thứ tự tương đối của các thành phố từ cha mẹ. Thuật toán: 

1. Chọn ngẫu nhiên hai vị trí cắt left, right trên tail 

2. Sao chép đoạn [left:right] từ cha thứ nhất sang con ở cùng vị trí 

3. Duyệt cha thứ hai theo thứ tự vòng (bắt đầu ngay sau vị trí right), bỏ các thành phố đã có 

4. Điền các thành phố còn lại vào các vị trí trống của con theo thứ tự vòng 

Python 

def order_crossover(parent1: Route, parent2: Route, rng: Random) -> tuple[Route, Route]: 

"""OX hai điểm trên tail; fill vòng từ sau đoạn cắt; parent bất biến.""" 

a, b = parent1[1:], parent2[1:] left, right = sorted(rng.sample(range(len(a)), 2)) right += 1 def child(first: Route, second: Route) -> Route: result = [-1] * len(first) result[left:right] = first[left:right] used = set(first[left:right]) values = [city for city in second[right:] + second[:right] if city not in used] positions = list(range(right, len(first))) + list(range(left)) for position, value in zip(positions, values): result[position] = value return (0, *result) return child(a, b), child(b, a) 

Ví dụ minh họa OX: 

||**0**|**1**|**2**|**3**|**4**|**5**|**6**|
|---|---|---|---|---|---|---|---|
|**Cha 1**|0|1|2|3|4|5|6|
|**Cha 2**|0|4|1|6|2|5|3|
|**Cha 3**|0|6|2|3|4|5|1|



_(Đoạn giữ lại từ Cha 1: vị trí 1-2, điền từ Cha 2 theo thứ tự vòng)_ 

_Hình 2.1 - Minh họa toán tử Order Crossover (OX)_ 

#### **b) Partially Mapped Crossover - PMX (tùy chọn)** 

PMX dùng ánh xạ giữa đoạn của hai cha mẹ để giải quyết xung đột thành phố: 

1. Giữ đoạn [left:right] từ cha thứ nhất ở cùng vị trí trong con 

2. Với mỗi thành phố của cha thứ hai nằm ngoài đoạn, theo chuỗi ánh xạ cho đến khi tìm được thành phố chưa có trong đoạn giữ 

Python def partially_mapped_crossover( parent1: Route, parent2: Route, rng: Random ) -> tuple[Route, Route]: """PMX trên tail: giữ segment, giải collision bằng chuỗi ánh xạ A `→` B.""" first, second = parent1[1:], parent2[1:] left, right = sorted(rng.sample(range(len(first)), 2)) right += 1 def child(kept: Route, donor: Route) -> Route: result = list(donor) result[left:right] = kept[left:right] mapping = dict(zip(kept[left:right], donor[left:right])) for index in (*range(left), *range(right, len(kept))): city = donor[index] while city in mapping: city = mapping[city] result[index] = city return (0, *result) return child(first, second), child(second, first) 

## **2.2.5. Đột biến** 

Module algorithms/ga/mutation.py cài đặt bốn toán tử đột biến. Đột biến được áp dụng với một xác suất Bernoulli trên mỗi cá thể con, không phải trên từng thành phố, nên mutation_rate có cùng ý nghĩa giữa các phương pháp. Mọi toán tử đều giữ thành phố 0 đứng đầu và không làm thay đổi route cha (immutable parent). 

Python def mutate(route: Route, rate: float, rng: Random, method: str = "inversion") -> Route: """Một xác suất/cá thể; đảo đoạn gồm cả hai đầu, không sửa parent.""" if rng.random() >= rate: return tuple(route) result = list(route) i, j = rng.sample(range(1, len(route)), 2) if method == "swap": result[i], result[j] = result[j], result[i] elif method == "insertion": result.insert(j, result.pop(i)) else: i, j = sorted((i, j)) segment = result[i:j+1] if method == "inversion": segment.reverse() else:  # scramble rng.shuffle(segment) result[i:j+1] = segment return tuple(result) 

#### **a) Inversion Mutation (mặc định)** 

Chọn ngẫu nhiên hai vị trí trên tail, đảo ngược thứ tự của đoạn giữa hai vị trí đó (kể cả hai đầu). 

_Hình 2.2 - Minh họa toán tử Inversion Mutation_ 

Ví dụ Inversion: Route (0, 1, 2, 3, 4, 5, 6), chọn vị trí 2 và 5 → đảo đoạn [2, 3, 4, 5] → kết quả (0, 1, 5, 4, 3, 2, 6) 

#### **b) Swap Mutation (tùy chọn)** 

Chọn ngẫu nhiên hai vị trí khác nhau trên tail và hoán đổi hai thành phố tại hai vị trí đó. 

#### **c) Insertion Mutation (tùy chọn)** 

Lấy thành phố tại vị trí i ra khỏi route, rồi chèn vào vị trí j (vị trí mới sau khi pop). Thao tác này di chuyển một thành phố đến vị trí mới trong hành trình. 

#### **d) Scramble Mutation (tùy chọn)** 

Chọn ngẫu nhiên một đoạn trên tail rồi xáo trộn thứ tự các thành phố trong đoạn đó bằng Fisher-Yates shuffle. 

#### **Sơ đồ so sánh bốn phương pháp đột biến:** 



<!-- Start of picture text -->
Chon i, j ngau<br>nhién<br>Dao ngudc<br>route[i..j]<br>inversion<br>Chon i, j ngau<br>aep————_—_> Hoaneatdéihiénroute[i]5<br>= route[j]<br>Mutation q Route con<br>Method 4 d6t bién<br>Chon i, j ngau<br>» 5 nhién<br>bey > Pop route[i],<br>insert tai j<br>scramble<br>Chon i, j ngau<br>nhién<br>Shuffle<br>routefi..j]<br><!-- End of picture text -->

**2.2.6. Elitism và global best** 

Elitism là cơ chế bảo tồn elite_count cá thể tốt nhất của quần thể hiện tại, sao chép trực tiếp sang quần thể kế tiếp cùng với fitness đã biết (không đánh giá lại). Module algorithms/ga/survivor.py cài đặt việc này: 

Python def select_elites(population: list[Route], costs: list[float], count: int) -> tuple[list[Route], list[float]]: """Giữ count index tốt nhất, thứ tự tie ổn định; tái dùng fitness.""" indices = sorted(range(len(population)), key=lambda i: costs[i])[:count] return [population[i] for i in indices], [costs[i] for i in indices] 

Điểm quan trọng: fitness không được gán lại về 0 khi sao chép elites — điều đó sẽ làm sai thứ tự minimization. Kích thước quần thể luôn được duy trì đủ population_size cá thể ngay cả khi population_size là số lẻ. 

Global Best Archive là cơ chế riêng biệt với elitism. Mỗi lần một route con được đánh giá (kể cả trong phần route chưa commit), nếu chi phí nhỏ hơn global best hiện tại thì archive được cập nhật ngay lập tức. Kết quả cuối cùng là global best của toàn bộ lần chạy, không phải chỉ trong quần thể cuối. Đây là thiết kế quan trọng: ngay cả khi thuật toán bị dừng giữa một thế hệ, nghiệm tốt nhất từng gặp vẫn được giữ lại. 

Python def evaluate_candidate(route: tuple[int, ...]) -> float: nonlocal evaluations, best_route, best_distance cost = problem.route_length(route) evaluations += 1 if cost < best_distance: best_route, best_distance = route, cost return cost 

## **2.2.7. Điều kiện dừng và lịch sử** 

GA kiểm tra các điều kiện dừng tại các điểm an toàn (cooperative stopping), không phải hard real-time: 

|**Điều kiện dừng**|**stopping_reason**|**Mô tả**|
|---|---|---|
|Hết số generation|MAX_ITERATIONS|Đạt min(generations,<br>max_iterations) thế hệ<br>hoàn chỉnh|
|Hết ngân sách đánh giá|MAX_EVALUATIONS|Tổng lần gọi route_length<br>≥ max_evaluations|
|Hết thời gian|TIME_LIMIT|Thời gian thực tế ≥<br>time_limit_seconds|
|Yêu cầu dừng|CANCELLED|stop_requested() trả True|
|Trì trệ|STAGNATION|stagnation_patience thế hệ<br>liên tiếp không cải thiện<br>global best|



Lưu ý: max_evaluations phải đủ ít nhất cho quần thể ban đầu (tức ≥ population_size). Điều kiện STAGNATION chỉ hoạt động khi được bật tường minh trong cấu hình. 

#### **Cấu trúc lịch sử (RunResult và IterationStat):** 

Mỗi snapshot lịch sử (IterationStat) lưu: iteration, best_current (best trong quần thể đã commit), best_so_far (global best), mean_fitness, evaluations tích lũy, elapsed_seconds và population_diversity. record_history_every kiểm soát tần suất ghi snapshot trung gian. Luôn có snapshot iteration=0 (sau khởi tạo) và snapshot cuối (khi kết thúc). 

#### **Sơ đồ điều kiện dừng:** 



<!-- Start of picture text -->
Kiém tra<br>diéu kién ding<br>stop_requeste hong cé<br>evaluations >= max_eviteration >= cap<br>lapsed>=time limit tagnation >=_<br>CANCELLED TIME_LIMIT MAX_EVALUATIONS MAX_ITERATIONS STAGNATION C ey<br>a ~<br>( diing, tea<br>{. Rungesutt<br>\<br><!-- End of picture text -->

## **2.2.8. Các phương án nâng cao** 

Ngoài pipeline mặc định, dự án cài đặt thêm một số tính năng tùy chọn: 

#### **a) Stagnation Stopping** 

Dừng thuật toán sớm khi quần thể không cải thiện global best trong stagnation_patience thế hệ liên tiếp. Biến stagnation được reset về 0 mỗi khi global best cải thiện và tăng thêm 1 sau mỗi thế hệ đầy đủ không cải thiện. 

#### **b) Adaptive Mutation** 

Điều chỉnh mutation rate động theo mức trì trệ và diversity của quần thể. Module algorithms/ga/monitoring.py cài đặt hai hàm: 

Python def population_diversity(population: list[Route]) -> float: """(unique symmetric tours−1)/(P−1); route đảo chiều được coi tương đương.""" if len(population) <= 1: return 0.0 canonical = {min(route, (0, *route[:0:-1])) for route in population} return (len(canonical)-1) / (len(population)-1) 

def effective_mutation_rate(config: GAConfig, stagnation: int, diversity: float) -> float: """Tăng tuyến tính theo stagnation; diversity≤0.1 đặt pressure tối thiểu 0.5.""" if not config.adaptive_mutation: return config.mutation_rate base = min(config.adaptive_max_rate, max(config.adaptive_min_rate, config.mutation_rate)) pressure = min(1.0, stagnation / config.adaptive_patience) if diversity <= 0.1: pressure = max(pressure, 0.5) return base + (config.adaptive_max_rate - base) * pressure 

Khi diversity thấp (≤0. 1) hoặc stagnation cao, áp lực được tăng lên, mutation rate tăng theo để khám phá thêm. Tùy chọn này tắt mặc định để giữ baseline dễ so sánh. 

#### **c) Bounded 2-opt Local Search** 

Module algorithms/ga/local_search.py cài đặt tìm kiếm cục bộ 2-opt theo chiến lược first-improvement: với mỗi cặp (𝑖, 𝑗) theo thứ tự tăng dần, thử đảo đoạn route[i..j] và chấp nhận ngay nếu cải thiện chi phí, sau đó restart scan từ đầu. 

Python def improve( route: Route, cost: float, *, evaluate: Callable[[Route], float], should_stop: Callable[[], str | None], max_moves: int, max_probes: int, ) -> LocalSearchResult: """First improvement theo i,j tăng dần; restart sau move, giữ 0 và parent.""" probes, moves = 0, 0 while moves < max_moves and probes < max_probes: 

improved = False for left in range(1, len(route)-1): for right in range(left+1, len(route)): if should_stop() or probes >= max_probes: return LocalSearchResult(route, cost, probes, moves, ...) candidate = route[:left] + route[left:right+1][::-1] + route[right+1:] candidate_cost = evaluate(candidate)   # đây là full objective call probes += 1 if candidate_cost < cost: route, cost = candidate, candidate_cost moves += 1 improved = True break if improved: break if not improved: break return LocalSearchResult(route, cost, probes, moves, None) 

**Điểm quan trọng:** Mỗi probe 2-opt gọi một lần evaluate đầy đủ và được tính vào evaluations tổng. Điều này có nghĩa 2-opt cạnh tranh ngân sách evaluations với các thế hệ GA. 

## **2.2.9. Tổ chức mã nguồn** 

## **CHƯƠNG 3. THUẬT TOÁN ELEPHANT HERDING OPTIMIZATION** 

### **3.1. Tổng quan về Elephant Herding Optimization** 

### **3.1.1. Khái niệm EHO** 

Elephant Herding Optimization (EHO) là thuật toán tối ưu hóa lấy cảm hứng từ hành vi sống theo đàn của loài voi. Quần thể được chia thành nhiều nhóm nhỏ gọi là Clan, trong đó mỗi cá thể đại diện cho một lời giải và được đánh giá bằng hàm mục tiêu. Thuật toán sử dụng cơ chế cập nhật cá thể theo voi dẫn đầu (Matriarch) và cơ chế tách đàn (Separating Operator) để tìm kiếm lời giải tốt hơn. 

Đối với bài toán TSP, do lời giải được biểu diễn dưới dạng hoán vị các thành phố, nhóm sử dụng phiên bản Discrete EHO (D-EHO), điều chỉnh các phép cập nhật sang dạng rời rạc nhằm đảm bảo mỗi hành trình luôn hợp lệ. 

### **3.1.2. Nguyên lý hành vi đàn voi** 

Mỗi _Clan_ gồm một cá thể dẫn đầu gọi là _Matriarch_ . Các cá thể trong đàn cập nhật vị trí dựa trên Matriarch, trong khi Matriarch được điều chỉnh theo tâm của Clan. Bên cạnh đó, cá thể có fitness kém nhất sẽ được chọn để thực hiện cơ chế _Separation_ , tạo cá thể mới nhằm duy trì sự đa dạng của quần thể. Ba cơ chế này giúp thuật toán cân bằng giữa khai thác nghiệm tốt và khám phá các vùng nghiệm mới. 

### **3.1.3. Các thành phần chính của EHO** 

Thuật toán EHO mô phỏng hành vi sống theo đàn của voi, trong đó quần thể được chia thành 𝑁𝑐 clan, mỗi clan gồm 𝑚 cá thể. Các thành phần chính bao gồm: 

- Clan: Nhóm các cá thể voi trong quần thể. 

- Matriarch: Cá thể có nghiệm tốt nhất trong mỗi clan, đóng vai trò dẫn dắt. 

- Clan center: Tâm đại diện cho các cá thể trong clan. 

- Clan updating operator: Cập nhật cá thể dựa trên ảnh hưởng của matriarch và tâm clan. 

- Separating operator: Thay thế cá thể có nghiệm kém nhằm duy trì tính đa dạng của quần thể. 

#### **Cơ chế cập nhật của EHO liên tục** 

Vị trí voi thường được cập nhật dựa trên matriarch: 



Matriarch được cập nhật dựa trên tâm clan: 



Trong đó, α, β ∈[0, 1] là các hệ số điều chỉnh;  là số ngẫu nhiên trong khoảng 𝑟 [0, 1]. Cá thể có vị trí kém nhất được thay thế bằng vị trí mới trong miền tìm kiếm: 



#### **Điều chỉnh EHO cho bài toán TSP** 

Các công thức trên được thiết kế cho không gian liên tục. Trong khi đó, bài toán TSP biểu diễn nghiệm dưới dạng hoán vị thứ tự các thành phố. Vì vậy, không thể áp dụng trực tiếp phép cộng, trừ hoặc tính trung bình tọa độ vì có thể tạo ra tour không hợp lệ. 

Do đó, dự án sử dụng Discrete EHO (D-EHO), kế thừa cấu trúc clan, matriarch và cơ chế tách đàn, đồng thời thay đổi các phép cập nhật sang thao tác trên hoán vị để đảm bảo mỗi tour hợp lệ. 

Chất lượng mỗi nghiệm được đánh giá bằng tổng chiều dài tour: 



Với 𝑇𝑛+1 = 𝑇1, tour phải quay về thành phố xuất phát. Mục tiêu của thuật toán là tìm tour có tổng quãng đường ngắn nhất. 

### **3.2. Áp dụng EHO cho bài toán TSP** 

|**Thành phần EHO**|**Cách áp dụng trong D-EHO**|
|---|---|
|Cá thể|Một tour gồm thứ tự các thành phố, cố định thành phố 0 ở đầu|
|Clan|Nhóm gồm<br>tour<br>𝑚|
|Matriarch|Tour có tổng quãng đường ngắn nhất trong clan|
|Tâm clan|Tour medoid có tổng khoảng cách Hamming nhỏ nhất|
|Cập nhật<br>α|Dùng guided-swap đưa các tour về matriarch|
|Cập nhật<br>β|Dùng guided-swap đưa matriarch về tâm clan|



|Separation|Thay các tour kém nhất bằng hoán vị ngẫu nhiên hợp lệ|
|---|---|
|Elitism|Lưu nghiệm tốt nhất của từng clan và toàn quần thể|



### **3.2.1. Biểu diễn nghiệm và hàm mục tiêu** 

Với  thành phố, mỗi cá thể được biểu diễn bằng một tour: 𝑛 



Trong đó, thành phố 0 được cố định ở đầu và các thành phố còn lại được sắp xếp theo dạng hoán vị. 

Hàm mục tiêu là tối thiểu hóa tổng chiều dài tour: 



Trong đó,  là ma trận khoảng cách giữa các thành phố. Tour phải quay về thành phố 𝐷 xuất phát. Dữ liệu sử dụng ma trận khoảng cách đối xứng, hữu hạn và không âm, tương ứng với bài toán Symmetric TSP. 

### **3.2.2. Phân chia quần thể thành các Clan** 

Quần thể gồm 𝑁𝑐 clan, mỗi clan có 𝑚 tour. Mỗi tour được lưu cùng chi phí tương ứng để thuận tiện cho việc đánh giá và lựa chọn cá thể tốt nhất. 

Matriarch được xác định bằng tour có chi phí nhỏ nhất: 



Đoạn mã thực hiện việc lựa chọn Matriarch và xác định tâm clan: 

Python @dataclass(frozen=True) class Clan: members: tuple[Route, ...] costs: tuple[float, ...] def best_index(self) -> int: return min(range(self.size), key=lambda index: (self.costs[index], index)) 

def center(self) -> Route: return self.members[self.center_index()] 

Sơ đồ thao tác chính trên một clan: 



<!-- Start of picture text -->
Chon route cost<br>thdp nhat:<br>matriarch<br>Population: N_c Chia thanh N_c Ghép méi route Clan sn sang cho<br>mroute clan v6i cost EHO update<br>Tinh Hamming<br>medoid: center<br><!-- End of picture text -->

### **3.2.3. Cập nhật Matriarch** 

Do không thể tính trung bình trực tiếp trên các hoán vị, D-EHO sử dụng Hamming Medoid để xác định tâm clan. 

Khoảng cách Hamming giữa hai tour được tính bằng số vị trí khác nhau: 



Tâm clan là tour có tổng khoảng cách Hamming nhỏ nhất đến các tour còn lại: 



Nếu có nhiều tour cùng khoảng cách, ưu tiên tour có chi phí thấp hơn. 

Sau đó, matriarch được cập nhật về phía tâm clan bằng guided-swap với hệ số . β Luồng tính tâm clan: so sánh các route theo từng cặp, cộng khoảng cách của từng route, rồi chọn route có tổng nhỏ nhất; hòa thì ưu tiên cost và index: 



<!-- Start of picture text -->
So san tour cost<br>nanroute dannrongsachcian ennTinhStones Hammingng cp Cong astancembiroute cho Téng distancehat? nhs Duy >|rng J index Chon route medols<br><!-- End of picture text -->

Python def center_index(self) -> int: distance_totals = [0] * self.size for first in range(self.size): for second in range(first + 1, self.size): distance = hamming_distance(self.members[first], self.members[second]) distance_totals[first] += distance distance_totals[second] += distance return min( range(self.size), key=lambda index: (distance_totals[index], self.costs[index], index), ) 

### **3.2.4. Di chuyển voi thường (Clan Updating Operator)** 

Trong D-EHO, các cá thể voi thường được cập nhật bằng phép **Guided-Swap** , đưa route hiện tại tiến gần route Matriarch. Hệ số  điều khiển mức độ cập nhật. α 

Với route nguồn , route đích target, tập vị trí khác nhau được xác định: π 



<!-- Start of picture text -->
diff ={j | mj # target;, j > 1}<br><!-- End of picture text -->

Số lần hoán đổi được tính bằng: 



<!-- Start of picture text -->
k=|a-r-|diff\|<br><!-- End of picture text -->

Trong đó, 𝑟∼𝑈[0, 1) là số ngẫu nhiên và α ∈[0, 1] là hệ số cập nhật. 

Quá trình Guided-Swap thực hiện: 

1. Xác định các vị trí khác nhau giữa hai route. 

2. Xáo trộn danh sách vị trí khác nhau. 

3. Chọn vị trí cần cập nhật và hoán đổi thành phố hiện tại với thành phố tương ứng trong route đích. 

4. Lặp lại cho đến khi đủ số lần hoán đổi. 

Phép hoán đổi không tác động đến thành phố xuất phát (index 0), đồng thời đảm bảo route luôn là một hoán vị hợp lệ. Khi α = 0, route được giữ nguyên; khi α = 1, thuật toán trả về route đích theo xử lý biên của hàm. 

**Sơ đồ quy trình Guided-Swap:** 



Python diff = [i for i in range(1, n) if source[i] != target[i]] steps = floor(strength * rng.random() * len(diff)) if steps <= 0: return tuple(source) result = list(source) pos = [0] * n for idx, city in enumerate(result): pos[city] = idx rng.shuffle(diff) swaps_done = 0 for i in diff: if swaps_done >= steps: break desired_city = target[i] current_city = result[i] if current_city == desired_city: continue j = pos[desired_city] result[i], result[j] = desired_city, current_city pos[desired_city] = i pos[current_city] = j swaps_done += 1 

### **3.2.5. Tách đàn (Separating Operator)** 

#### **Mục đích** 

Toán tử tách đàn (Separating Operator) được sử dụng nhằm duy trì tính đa dạng của quần thể và hạn chế tình trạng hội tụ sớm vào nghiệm tối ưu cục bộ. Trong EHO, toán tử này tác động lên những cá thể có chất lượng kém nhất trong mỗi clan, đồng thời bảo vệ cá thể dẫn đầu (Matriarch) để giữ lại nghiệm tốt hiện tại. 

#### **Nguyên lý hoạt động** 

Khác với EHO truyền thống áp dụng trên không gian liên tục, bài toán TSP biểu diễn mỗi cá thể dưới dạng một hoán vị (permutation) các thành phố. Vì vậy, không thể sinh cá thể mới bằng cách lấy ngẫu nhiên tọa độ trong một khoảng biên như (LB) và (UB). 

Thay vào đó, thuật toán thực hiện các bước sau: 

1. Bảo vệ Matriarch: Loại bỏ chỉ số của cá thể Matriarch khỏi danh sách các cá thể có thể bị thay thế. 

2. Xác định cá thể kém nhất: Sắp xếp các cá thể còn lại trong clan theo cost giảm dần và chọn separation_count_per_clan cá thể có cost cao nhất. 

3. Giữ lại cá thể không bị tách: Các route không được chọn sẽ được giữ nguyên vị trí và giá trị. 

4. Tạo cá thể mới: Thay thế mỗi route được chọn bằng một hoán vị ngẫu nhiên hợp lệ được sinh bởi hàm random_permutation(n, rng). 

5. Tạo clan mới: Kết hợp các route được giữ lại và các route mới để hình thành clan candidate có kích thước không đổi. 

#### **Quy trình thực hiện** 



<!-- Start of picture text -->
itr nguyén route<br>khdng bi tach<br>Clan hién tai va Loal matriarch Chon s route cost Clan candidate<br>Knot danh sch co<br>cost thé tach cao nhat cong 9 kich thu<br>Tao s permutation<br>ngdu nhién hop Ie<br><!-- End of picture text -->

Python 

protected = set(protected_indices) 

eligible = [index for index in range(clan_size) if index not in protected] worst_indices = sorted(eligible, key=lambda i: (-costs[i], i))[:separation_count] for idx in worst_indices: 

new_clan[idx] = random_permutation(n, rng) 

### **3.2.6. Cơ chế bảo tồn nghiệm tốt nhất (Elitism)** 

#### **Mục đích** 

Cơ chế bảo tồn nghiệm tốt nhất (Elitism) được sử dụng nhằm đảm bảo các lời giải tốt nhất đã tìm được không bị mất đi trong quá trình tiến hóa của thuật toán EHO. Cơ chế này lưu trữ nghiệm tốt nhất của từng clan (Clan Archive) và nghiệm tốt nhất trên toàn bộ quần thể (Global Best), từ đó hạn chế việc chất lượng lời giải bị suy giảm qua các thế hệ. 

#### **Nguyên lý hoạt động** 

Trong implementation này, cơ chế Elitism được triển khai thông qua hai cấp độ lưu trữ: 

- **Clan Archive:** Lưu trữ route tốt nhất từng được tìm thấy của mỗi clan. Archive được khởi tạo bằng route tốt nhất ban đầu của clan tương ứng. 

- **Global Best:** Lưu trữ route có cost nhỏ nhất được tìm thấy trong toàn bộ quá trình chạy thuật toán, không phụ thuộc vào clan hay thế hệ. 

Quá trình cập nhật và bảo tồn nghiệm tốt nhất được thực hiện như sau: 

1. **Khởi tạo Archive:** Sau khi khởi tạo quần thể, route tốt nhất của mỗi clan được lưu vào Clan Archive. 

2. **Đánh giá candidate:** Mỗi khi một candidate được đánh giá, thuật toán so sánh cost của route với Clan Archive tương ứng. Nếu candidate có cost nhỏ hơn, archive của clan được cập nhật. 

3. **Cập nhật Global Best:** Candidate tiếp tục được so sánh với nghiệm tốt nhất toàn cục. Nếu có cost nhỏ hơn, Global Best được cập nhật. 

4. **Khôi phục nghiệm tốt nhất:** Sau khi một generation hoàn chỉnh, thuật toán kiểm tra xem route được lưu trong Clan Archive còn tồn tại trong clan hay không. Nếu route đã bị mất, thuật toán đưa route này trở lại clan bằng cách thay thế thành viên có cost lớn nhất, nhưng không thay thế Matriarch hiện tại. 

5. **Commit generation:** Sau khi hoàn tất quá trình bảo tồn, generation mới được xác nhận và trở thành trạng thái chính thức của quần thể. 

#### **Quy trình thực hiện** 



Python def _preserve_clan_best(clan: Clan, best_route: Route, best_distance: float) -> Clan: if best_route in clan.members: return clan leader_index = clan.best_index() replacement_index = clan.worst_indices(1, protected_indices=(leader_index,))[0] members = list(clan.members) costs = list(clan.costs) members[replacement_index] = best_route costs[replacement_index] = best_distance 

return Clan(tuple(members), tuple(costs)) 

### **3.3. Quy trình hoạt động của D-EHO** 

### **3.3.1. Sơ đồ luồng thuật toán** 



### **3.3.2. Giả mã (Pseudocode)** 

Python Input: TSP distance matrix D, clan_count N_c, elephants_per_clan m, alpha, beta, separation_count s, stopping limits Output: best valid tour and its distance Initialize N_c clans with m random valid tours each Evaluate all initial tours For each clan: archive its best tour Set global_best to the best initial tour While no stopping condition is met: Create an empty next_population For each clan: Select the lowest-cost tour as matriarch Compute the clan Hamming medoid Select up to s worst tours, excluding the matriarch For each member index i: If i is the matriarch: candidate = guided_swap(matriarch, medoid, beta) Else if i is selected for separation: candidate = random valid permutation Else: candidate = guided_swap(member[i], matriarch, alpha) Evaluate candidate once Update clan archive and global_best if improved Append candidate to next clan If every clan was completed: Restore archived clan best when needed If a full generation was completed: Commit next_population Else: 

Keep the last committed population and stop 

Return global_best and run metadata 

### **3.3.3. Giải thích quá trình cập nhật một thế hệ** 

Quá trình cập nhật một Generation gồm các bước: 

1. **Khởi tạo:** Tạo (N_c) clan, mỗi clan có (m) route ngẫu nhiên và đánh giá cost. 

2. **Xác định cá thể:** Chọn Matriarch có cost thấp nhất và tính Hamming Medoid cho từng clan. 

3. **Tách đàn:** Chọn tối đa (s) route có cost cao nhất, không bao gồm Matriarch. 

4. **Cập nhật cá thể:** Matriarch cập nhật theo Medoid với (\beta); cá thể Separation được thay bằng permutation ngẫu nhiên; các cá thể còn lại cập nhật theo Matriarch với (\alpha). 

5. **Đánh giá và bảo tồn:** Đánh giá từng candidate đúng một lần, cập nhật Clan Archive và Global Best nếu tìm được nghiệm tốt hơn. 

6. **Commit Generation:** Khôi phục Clan Archive nếu cần, sau đó chỉ commit khi tất cả clan hoàn thành. Nếu dừng giữa generation, giữ population đã commit gần nhất nhưng vẫn trả về Global Best tốt nhất đã tìm được. 

### **3.4. Triển khai thuật toán trong chương trình** 

### **3.4.1. Cấu trúc các module** 

Thuật toán EHO được triển khai thành các module riêng biệt, mỗi module đảm nhiệm một chức năng: 

|**Module**|**Trách nhiệm**|
|---|---|
|solver.py|Khởi tạo clan, điều khiển vòng lặp, cập nhật archive và trả kết quả|
|clans.py|Quản lý clan, chọn best/worst và tính Hamming Medoid|
|discrete_ops.py|Tình Hamming distance và thực hiện guided-swap|
|separation.py|Chọn route kém và sinh permutation mới|
|objective.py|kiểm tra route và tính tổng khoảng cách|



**Sơ đồ kết nối các thành phần chương trình:** 



<!-- Start of picture text -->
Clan selection and<br>medoid<br>Shared TSP<br>objective<br>CLI/ Benchmarkenenmart / EHO solver.solve Separatieparating<br>GUI operator<br>RunResult,<br>history, best route<br><!-- End of picture text -->

Khởi tạo quần thể trong solver.py: 

Python rng = Random(config.seed) clans: list[Clan] = [] for _ in range(config.clan_count): members = tuple( random_permutation(problem.dimension, rng) for _ in range(config.elephants_per_clan) ) costs = tuple(problem.route_length(route) for route in members) clans.append(Clan(members, costs)) 

Mỗi clan được khởi tạo bằng các route ngẫu nhiên hợp lệ, sau đó tính cost và đóng gói thành đối tượng Clan. 

Cập nhật cá thể: 

Python if index == leader_index: candidate = update_matriarch(route, center, config.beta, rng) elif index in separated: candidate = separated_members[index] else: candidate = move_toward_best(route, leader, config.alpha, rng) cost = problem.route_length(candidate) 

evaluations += 1 

Tùy vị trí và vai trò, mỗi cá thể được cập nhật bằng Matriarch Update, Separation hoặc Clan Update. Sau đó candidate được đánh giá và cập nhật nghiệm tốt nhất. 

### **3.4.2. Các tham số cấu hình** 

Các tham số được quản lý thông qua EHOConfig trong domain/models.py: 

|**Tham số**|**Giá trị mặc định**|**Ý nghĩa**|
|---|---|---|
|clan_count|Theo cấu hình|Số lượng clan|
|elephants_per_clan|Theo cấu hình|Số cá thể mỗi clan|
|alpha|0.7|Hệ số cập nhập cá thể|
|beta|0.3|Hệ số cập nhật Matriarch|
|separation_count_per_clan|1|Số cá thể tách mỗi clan|
|seed|Theo cấu hình|Giá trị khởi tạo ngẫu nhiên|
|iterations|Theo cấu hình|Số thế hệ chay|



Các điều kiện kiểm tra chính: 

- Mỗi clan có ít nhất 3 cá thể và có tối thiểu 2 clan. 

- alpha, beta thuộc khoảng [0, 1]. 

- Số cá thể separation phải nhỏ hơn kích thước clan. 

- Baseline sử dụng khởi tạo ngẫu nhiên và bật preserve_global_best. 

- Evaluation budget phải đủ để đánh giá quần thể ban đầu. 

### **3.4.3. Điều kiện dừng và quản lý đánh giá** 

Solver có thể dừng khi đạt giới hạn thế hệ, max_evaluations, time_limit_seconds hoặc callback yêu cầu dừng. max_evaluations phải đủ đánh giá population ban đầu; giới hạn thời gian nếu có phải dương. Dữ liệu đầu vào là symmetric TSP, có ít nhất 3 thành phố, ma trận hữu hạn, không âm, đối xứng và đường chéo bằng 0. 

Nếu chạy đủ G thế hệ và không dừng sớm, số objective evaluations là N_c * m * (G + 1): đánh giá population ban đầu một lần, cộng một lần cho mỗi candidate mỗi generation. Candidate trùng route vẫn được tính là một evaluation; khôi phục route archive không đánh giá lại vì cost đã lưu. Nếu budget/time dừng giữa generation, 

solver không commit generation dở dang; population giữ ở generation hoàn chỉnh gần nhất, còn global best giữ nghiệm tốt nhất đã đánh giá. 

Mỗi candidate chỉ được bắt đầu tạo khi chưa có yêu cầu dừng; sau đó solver đánh giá nó một lần và cập nhật nghiệm tốt nhất. Sơ đồ điều kiện dừng: 



Đoạn mã kiểm tra stop: 

Python def get_stop_reason() -> str | None: if stop_requested is not None and stop_requested(): return "CANCELLED" if (config.time_limit_seconds is not None and perf_counter() - start >= config.time_limit_seconds): return "TIME_LIMIT" if config.max_evaluations is not None and evaluations >= config.max_evaluations: return "MAX_EVALUATIONS" return None 

### **3.5. Nhận xét và giới hạn của D-EHO** 

### **3.5.1. Ưu điểm** 

D-EHO giữ các thành phần có ý nghĩa của EHO clan, matriarch, cập nhật clan và separation, đồng thời mọi thao tác đều tạo route hợp lệ mà không cần repair. Archive theo clan và global best hạn chế mất nghiệm tốt đã tìm thấy. Solver hỗ trợ seed, giới hạn số lần đánh giá và giới hạn thời gian để tổ chức các lần chạy lặp lại. 

### **3.5.2. Hạn chế** 

D-EHO thay phép toán vector của EHO liên tục bằng guided-swap, Hamming medoid và permutation ngẫu nhiên. Đây là thích nghi cho không gian hoán vị, không phải tương đương đại số với EHO liên tục. Hamming medoid xét vị trí thành phố, không trực tiếp tối ưu mức tương đồng cạnh của chu trình. Archive matriarch theo clan là cơ chế elitism bổ sung của implementation. Solver hiện chỉ hỗ trợ symmetric TSP; heuristic không bảo đảm tìm optimum toàn cục. 

Benchmark EHO ở trên dùng năm seed và dataset registry không có optimum đã xác minh. Vì vậy kết quả mô tả cấu hình được chạy, không chứng minh tối ưu. So sánh hiệu năng cần dùng cùng dataset, seed, evaluation budget và môi trường. 

### **3.5.3. Khả năng áp dụng cho TSP** 

Implementation phù hợp với phạm vi đề tài hiện tại: TSP đối xứng, có ít nhất ba thành phố và ma trận khoảng cách hữu hạn, không âm, đối xứng, đường chéo bằng 0. Việc cố định thành phố `0` ở đầu route loại bỏ các biểu diễn quay vòng tương đương mà vẫn giữ nguyên chu trình đóng. 

Để mở rộng sang TSP bất đối xứng, cần xác nhận lại các giả định của objective và đánh giá lại các toán tử trên chu trình có hướng. Với bài toán lớn hơn, có thể nghiên cứu toán tử ưu tiên bảo toàn cạnh hoặc kết hợp tìm kiếm cục bộ, nhưng cần kiểm tra bằng thí nghiệm mới thay vì suy rộng trực tiếp từ benchmark hiện có. 

D-EHO đã có thể dùng làm một solver rời rạc độc lập để minh họa và thực nghiệm EHO trên TSP đối xứng trong phạm vi dữ liệu của dự án. Bằng chứng hiện tại xác nhận tính hợp lệ và khả năng chạy của implementation; đánh giá chất lượng nghiệm tương đối với GA hoặc optimum vẫn cần thí nghiệm đối chứng bổ sung. 


## CHƯƠNG 4. KẾT QUẢ THỰC NGHIỆM

Chương này trình bày chi tiết các kết quả thực nghiệm được thực hiện để đánh giá hiệu quả của thuật toán Genetic Algorithm (GA) trên bài toán Traveling Salesman Problem (TSP). Các thực nghiệm được thiết kế nhằm so sánh các toán tử khác nhau, phân tích ảnh hưởng của tham số, và đánh giá các phương án nâng cao như khởi tạo thông minh, adaptive mutation và local search.

### 4.1. Môi trường thực nghiệm

Tất cả các thực nghiệm được thực hiện trên cùng một môi trường để đảm bảo tính nhất quán và khả năng tái lập kết quả.

**Cấu hình phần cứng và phần mềm:**
- **Hệ điều hành:** Windows 10 build 26300
- **Ngôn ngữ lập trình:** Python 3.11.9
- **Thư viện chính:** 
  - NumPy 2.4.6 (dependency của Matplotlib)
  - Matplotlib 3.11.2 (visualization)
  - Jupyter Notebook 7.6.4 (thực nghiệm)
- **Môi trường ảo:** Python venv với các dependencies được cài đặt từ `requirements.txt`

**Phương pháp thực nghiệm:**
- Tất cả các thực nghiệm sử dụng cùng bộ seed ngẫu nhiên: `[11, 23, 37, 53, 71]`
- Mỗi cấu hình được chạy 5 lần với 5 seed khác nhau
- Kết quả được ghi lại dưới dạng JSON và CSV để phân tích
- Các biểu đồ hội tụ (convergence curves) và phân phối (distribution) được vẽ bằng Matplotlib

### 4.2. Bộ dữ liệu và cấu hình cơ sở

#### 4.2.1. Bộ dữ liệu TSP

Dự án sử dụng bảy bộ dữ liệu ma trận khoảng cách đối xứng (Symmetric TSP) với quy mô từ nhỏ đến trung bình. Các ma trận được lưu dưới dạng file văn bản trong thư mục `data/`, mỗi dòng là một hàng ma trận với các phần tử cách nhau bởi khoảng trắng.

| **Tên file** | **Số thành phố** | **Mô tả** |
|---|---|---|
| `03Cities-6.txt` | 3 | Bài toán nhỏ nhất, dùng để kiểm chứng correctness |
| `04Cities-189.txt` | 4 | Bài toán nhỏ, có thể liệt kê exhaustive |
| `06Cities-1248.txt` | 6 | Bài toán nhỏ, dùng baseline cho các so sánh |
| `15Cities-1194.txt` | 15 | Bài toán trung bình nhỏ, dùng cho OFAT experiments |
| `26Cities-937.txt` | 26 | Bài toán trung bình |
| `42Cities-699.txt` | 42 | Bài toán trung bình lớn |
| `48Cities-33523.txt` | 48 | Bài toán lớn nhất trong benchmark |

**Lưu ý về known optimum:** Các số trong tên file (ví dụ: `1194` trong `15Cities-1194.txt`) không phải là optimum đã được xác minh toán học. Đây là các giá trị quan sát được trong quá trình phát triển và không được sử dụng làm ground truth trong đánh giá chất lượng nghiệm.

#### 4.2.2. Cấu hình cơ sở (Baseline Configuration)

Cấu hình cơ sở được sử dụng làm điểm tham chiếu cho tất cả các so sánh:

```python
# Cấu hình cơ sở cho GA
population_size = 40        # Notebook experiments
                            # 80 cho benchmark đầy đủ
generations = 2000
max_iterations = 2000
seed = [11, 23, 37, 53, 71] # 5 seeds cho reproducibility

# Selection
selection_method = "tournament"
tournament_size = 3

# Crossover  
crossover_method = "ox"      # Order Crossover
crossover_rate = 0.9

# Mutation
mutation_method = "inversion"
mutation_rate = 0.15

# Elitism
elite_count = 2

# Initialization
initialization_method = "random"

# Advanced features (tắt mặc định)
adaptive_mutation = False
local_search_enabled = False
stagnation_patience = None

# Budgets
max_evaluations = 2000      # Experiment 1-2
                            # 4000 cho Experiment 3-4
                            # 6000 cho benchmark đầy đủ
record_history_every = 1
```

### 4.3. Thực nghiệm 1-2: So sánh toán tử trên bài 15 thành phố

Thực nghiệm đầu tiên sử dụng phương pháp OFAT (One Factor At a Time) để đánh giá ảnh hưởng riêng lẻ của từng toán tử. Với bài toán 15 thành phố, quần thể 40 cá thể và ngân sách 2,000 evaluations, mỗi biến thể thay đổi đúng một thành phần so với cấu hình cơ sở.

#### 4.3.1. So sánh phương pháp Selection

Ba phương pháp selection được so sánh: Tournament (baseline), Rank và Roulette Wheel.

| **Phương pháp** | **Mean Distance** | **Median** | **Độ lệch chuẩn** | **Min** | **Max** |
|---|---|---|---|---|---|
| **Tournament (k=3)** | **1235.0** | **1225** | **43.86** | 1194 | 1308 |
| Rank Selection | 1413.6 | 1402 | 81.79 | 1310 | 1517 |
| Roulette Wheel | 1400.8 | 1340 | 158.48 | 1194 | 1623 |

**Phân tích kết quả:**

- **Tournament selection** cho kết quả tốt nhất với mean distance thấp nhất (1235.0) và độ ổn định cao (std = 43.86). Tournament tạo áp lực chọn lọc vừa phải, giúp cân bằng giữa exploitation và exploration.

- **Rank selection** cho kết quả kém hơn đáng kể (mean = 1413.6), tăng 14.5% so với tournament. Rank làm giảm áp lực chọn lọc bằng cách gán trọng số theo thứ hạng thay vì theo giá trị fitness thực, dẫn đến hội tụ chậm hơn với ngân sách evaluations giới hạn.

- **Roulette wheel selection** có độ lệch chuẩn rất cao (158.48), cho thấy kết quả không ổn định giữa các lần chạy. Phương pháp này nhạy cảm với phân phối fitness: khi có cá thể vượt trội, roulette có thể dẫn đến premature convergence; khi fitness gần đều nhau, chọn lọc gần như ngẫu nhiên.

**Kết luận:** Tournament selection với k=3 là lựa chọn tốt nhất cho cấu hình hiện tại và được giữ làm mặc định.

#### 4.3.2. So sánh toán tử Crossover

Hai toán tử crossover được so sánh: Order Crossover (OX - baseline) và Partially Mapped Crossover (PMX).

| **Toán tử** | **Mean Distance** | **Median** | **Độ lệch chuẩn** | **Min** | **Max** |
|---|---|---|---|---|---|
| **OX (Order Crossover)** | **1235.0** | **1225** | **43.86** | 1194 | 1308 |
| PMX (Partially Mapped) | 1275.4 | 1279 | 38.34 | 1225 | 1340 |

**Phân tích kết quả:**

- **OX** cho mean distance thấp hơn (1235.0 vs 1275.4), tốt hơn khoảng 3.3%.

- **PMX** có độ lệch chuẩn thấp hơn một chút (38.34 vs 43.86), cho thấy kết quả ổn định hơn giữa các runs, nhưng median cao hơn (1279 vs 1225).

- Cả hai toán tử đều bảo tồn hoán vị hợp lệ: OX bảo tồn thứ tự tương đối, còn PMX sử dụng ánh xạ vị trí. Với bài toán 15 thành phố và ngân sách 2,000 evaluations, OX có lợi thế nhẹ.

**Kết luận:** OX vẫn được giữ làm mặc định do mean cost thấp hơn, mặc dù PMX có độ ổn định cao hơn một chút.

#### 4.3.3. So sánh toán tử Mutation

Bốn toán tử mutation được so sánh: Inversion (baseline), Swap, Insertion và Scramble.

| **Toán tử** | **Mean Distance** | **Median** | **Độ lệch chuẩn** | **Min** | **Max** |
|---|---|---|---|---|---|
| **Inversion** | **1235.0** | **1225** | **43.86** | 1194 | 1308 |
| Swap | 1317.0 | 1289 | 113.40 | 1194 | 1517 |
| Insertion | 1319.8 | 1287 | 68.16 | 1225 | 1402 |
| Scramble | 1473.0 | 1391 | 152.78 | 1308 | 1726 |

**Phân tích kết quả:**

- **Inversion mutation** cho kết quả tốt nhất với mean distance thấp nhất và độ ổn định cao. Toán tử này đảo ngược một đoạn trong tour, tạo ra sự thay đổi có cấu trúc (structured perturbation).

- **Swap và Insertion** cho kết quả tương đương nhau (mean ~1318), kém hơn Inversion khoảng 6.7%. Hai toán tử này chỉ thay đổi vị trí của 1-2 thành phố, có thể không đủ mạnh để thoát khỏi local optima.

- **Scramble mutation** cho kết quả kém nhất (mean = 1473.0), tăng 19.3% so với Inversion. Scramble xáo trộn ngẫu nhiên một đoạn, phá vỡ cấu trúc tour quá mạnh, dẫn đến mất đi các building blocks tốt.

**Kết luận:** Inversion mutation là lựa chọn tốt nhất và được giữ làm mặc định. Toán tử này cân bằng tốt giữa exploration (tạo đa dạng) và preservation (giữ cấu trúc tốt).

#### 4.3.4. Biểu đồ so sánh tổng hợp các toán tử

_[Hình 4.1: Biểu đồ cột so sánh mean distance và độ lệch chuẩn của các biến thể toán tử. Trục x là các biến thể, trục y là mean distance, error bars biểu diễn standard deviation.]_

**Chú thích hình 4.1:** Biểu đồ cho thấy Tournament + OX + Inversion (cấu hình cơ sở) có mean distance thấp nhất. Rank và Roulette selection cho kết quả kém hơn đáng kể. Scramble mutation có mean cao nhất và độ biến động lớn nhất.

### 4.4. Thực nghiệm 3: Phân phối kết quả theo kích thước bài toán

Thực nghiệm thứ ba khảo sát 6 bộ dữ liệu (từ 3 đến 48 thành phố) với cùng cấu hình cơ sở, ngân sách 4,000 evaluations và 5 seeds.

#### 4.4.1. Kết quả tổng hợp

| **Số thành phố** | **Min** | **Mean** | **Median** | **Max** | **Std Dev** | **Tỷ lệ đạt min** |
|---|---|---|---|---|---|---|
| 3 | 6 | 6.0 | 6 | 6 | 0.00 | 100% (5/5) |
| 6 | 1248 | 1248.0 | 1248 | 1248 | 0.00 | 100% (5/5) |
| 15 | 1194 | 1200.2 | 1194 | 1225 | 13.86 | 80% (4/5) |
| 26 | 969 | 1046.0 | 1034 | 1186 | 82.85 | 20% (1/5) |
| 42 | 1102 | 1151.6 | 1133 | 1211 | 49.75 | 20% (1/5) |
| 48 | 51215 | 55404.6 | 55339 | 59638 | 3031.79 | 20% (1/5) |

**Phân tích theo kích thước bài toán:**

**Bài toán nhỏ (n = 3, 6):**
- GA đạt kết quả hoàn hảo: tất cả 5 runs đều tìm được nghiệm tốt nhất quan sát được
- Độ lệch chuẩn bằng 0, cho thấy kết quả hoàn toàn deterministic (với cùng seed)
- Với n=3, không gian tìm kiếm chỉ có 2! = 2 tours phân biệt
- Với n=6, không gian tìm kiếm có 5! = 120 tours, vẫn đủ nhỏ để GA explore hiệu quả

**Verification bằng exhaustive search:** Đối với n=3 và n=6, notebook đã kiểm chứng bằng cách liệt kê tất cả các hoán vị tail và tính chi phí trực tiếp. Kết quả xác nhận:
- Với n=3: min cost = 6 (đã verify exhaustive)
- Với n=6: min cost = 1248 (đã verify exhaustive)

**Bài toán trung bình (n = 15):**
- Mean distance = 1200.2, cao hơn min observed (1194) khoảng 0.5%
- Tỷ lệ hit min observed = 80% (4/5 runs)
- Độ lệch chuẩn tăng lên 13.86, phản ánh sự không đồng nhất giữa các runs
- Không gian tìm kiếm: 14! ≈ 8.7 × 10¹⁰ tours

**Bài toán trung bình lớn (n = 26, 42):**
- Tỷ lệ hit min observed giảm xuống 20% (1/5 runs)
- Mean distance cao hơn min observed khoảng 7-8% cho n=26 và 4-5% cho n=42
- Độ lệch chuẩn tăng mạnh: 82.85 cho n=26, 49.75 cho n=42
- GA bắt đầu gặp khó khăn với không gian tìm kiếm lớn hơn

**Bài toán lớn (n = 48):**
- Mean distance = 55404.6, cao hơn min observed (51215) khoảng 8.2%
- Độ lệch chuẩn rất lớn: 3031.79 (khoảng 5.5% của mean)
- Tỷ lệ hit min observed chỉ 20%
- Max distance (59638) cao hơn min 16.4%, cho thấy biến động lớn giữa các runs
- Không gian tìm kiếm: 47! ≈ 2.6 × 10⁵⁹ tours - vượt xa khả năng explore của GA với 4000 evaluations

#### 4.4.2. Phân phối và histogram

_[Hình 4.2: Sáu histogram nhỏ (small multiples) cho 6 bộ dữ liệu. Mỗi histogram hiển thị phân phối của 5 kết quả. Với n=3 và n=6, histogram chỉ có một cột duy nhất tại giá trị optimum. Với n lớn hơn, phân phối càng rộng.]_

**Chú thích hình 4.2:** Histogram cho thấy phân phối kết quả trở nên rộng hơn khi kích thước bài toán tăng. Với n=3 và n=6, kết quả tập trung hoàn toàn. Với n≥15, phân phối bắt đầu có spread, phản ánh tính stochastic của GA.

#### 4.4.3. Excess và relative excess

Để phân tích chất lượng nghiệm, tôi định nghĩa:
- **Absolute excess:** `distance - min_observed`
- **Relative excess:** `(distance - min_observed) / min_observed × 100%`

| **Số thành phố** | **Mean Abs Excess** | **Mean Rel Excess (%)** |
|---|---|---|
| 3 | 0.0 | 0.00% |
| 6 | 0.0 | 0.00% |
| 15 | 6.2 | 0.52% |
| 26 | 77.0 | 7.94% |
| 42 | 49.6 | 4.50% |
| 48 | 4189.6 | 8.18% |

**Nhận xét quan trọng:** "Min observed" trong bảng trên là giá trị nhỏ nhất trong 5 runs, **không phải optimum toàn cục** đã được chứng minh toán học. Do đó, relative excess chỉ đo lường độ biến động giữa các runs, không phải gap so với optimum thực sự.

### 4.5. Thực nghiệm 4: Các phương án nâng cao

Thực nghiệm thứ tư so sánh 6 biến thể GA trên 4 bài toán (15, 26, 42, 48 thành phố), mỗi bài chạy 5 seeds với ngân sách 4,000 evaluations.

#### 4.5.1. Các biến thể được so sánh

1. **Control:** Cấu hình cơ sở (Random + Tournament + OX + Inversion)
2. **PMX:** Thay OX bằng PMX crossover
3. **Mixed 25%:** Khởi tạo 25% bằng Nearest-Neighbor, 75% random
4. **NN:** Khởi tạo 100% bằng Nearest-Neighbor multi-start
5. **Adaptive:** Bật adaptive mutation (điều chỉnh mutation rate theo stagnation và diversity)
6. **GA+2-opt:** Bật bounded 2-opt local search với max 20 probes/offspring

#### 4.5.2. Kết quả tổng hợp

| **Bài toán** | **Control** | **PMX** | **Mixed 25%** | **NN** | **Adaptive** | **GA+2-opt** |
|---|---|---|---|---|---|---|
| **15 thành phố** |  |  |  |  |  |  |
| Mean Distance | **1200.2** | 1219.2 | **1194.0** | **1194.0** | 1228.0 | 1336.2 |
| Mean Generations | 104.0 | 104.0 | 104.0 | 104.0 | 104.0 | 20.6 |
| **26 thành phố** |  |  |  |  |  |  |
| Mean Distance | 1046.0 | 1054.0 | **958.6** | **961.8** | 1016.4 | 1388.8 |
| Mean Generations | 104.0 | 104.0 | 104.0 | 104.0 | 104.0 | 20.6 |
| **42 thành phố** |  |  |  |  |  |  |
| Mean Distance | 1151.6 | 1114.8 | **811.8** | **782.2** | 1112.4 | 1750.2 |
| Mean Generations | 104.0 | 104.0 | 104.0 | 104.0 | 104.0 | 20.6 |
| **48 thành phố** |  |  |  |  |  |  |
| Mean Distance | 55404.6 | 55073.2 | **37222.2** | **36559.0** | 53912.2 | 81489.6 |
| Mean Generations | 104.0 | 104.0 | 104.0 | 104.0 | 104.0 | 20.6 |

#### 4.5.3. Phân tích chi tiết từng biến thể

**1. Control (Baseline):**
- Kết quả trung bình, dùng làm điểm tham chiếu
- Commit được đầy đủ 104 generations với budget 4000 evaluations

**2. PMX Crossover:**
- Kết quả tương đương Control, không có cải thiện đáng kể
- Tại n=48: 55073.2 vs 55404.6 (cải thiện nhẹ 0.6%)
- Tại n=15: 1219.2 vs 1200.2 (kém hơn 1.6%)
- Kết luận: PMX không mang lại lợi ích rõ ràng trong cấu hình này

**3. Mixed 25% initialization:**
- **Cải thiện đáng kể** khi bài toán lớn hơn
- Tại n=15: 1194.0 vs 1200.2 (cải thiện 0.5%)
- Tại n=26: 958.6 vs 1046.0 (cải thiện **8.4%**)
- Tại n=42: 811.8 vs 1151.6 (cải thiện **29.5%**)
- Tại n=48: 37222.2 vs 55404.6 (cải thiện **32.8%**)
- Giải thích: 25% routes NN cung cấp starting points chất lượng tốt, giúp GA focus vào vùng promising của không gian tìm kiếm

**4. NN 100% initialization:**
- Kết quả **tốt nhất** trong tất cả các biến thể
- Tại n=48: 36559.0 (thấp nhất)
- Cải thiện so với Control: 34.0% tại n=48
- **Trade-off:** Thời gian khởi tạo NN cao hơn do phải chạy greedy construction n lần
- Matrix lookups cho NN không được tính vào evaluation budget nhưng có trong runtime

**5. Adaptive Mutation:**
- Kết quả **không nhất quán**
- Tại n=15: 1228.0 vs 1200.2 (kém hơn 2.3%)
- Tại n=26: 1016.4 vs 1046.0 (cải thiện 2.8%)
- Tại n=48: 53912.2 vs 55404.6 (cải thiện 2.7%)
- Giải thích: Adaptive mutation điều chỉnh rate dựa trên stagnation và diversity. Hiệu quả phụ thuộc vào bài toán cụ thể và tuning tham số (min_rate, max_rate, patience)
- Kết luận: Cần thêm experiments với các tham số khác nhau

**6. GA+2-opt Local Search:**
- Kết quả **kém nhất** trong tất cả các biến thể (!!)
- Tại n=48: 81489.6 vs 55404.6 (kém hơn **47.1%**)
- Tại n=42: 1750.2 vs 1151.6 (kém hơn 52.0%)
- Tại n=26: 1388.8 vs 1046.0 (kém hơn 32.8%)
- Chỉ commit được trung bình **20.6 generations** thay vì 104

**Giải thích vấn đề của GA+2-opt:**

Bounded 2-opt trong implementation này có một trade-off quan trọng:
- Mỗi probe 2-opt gọi một lần `route_length()` **đầy đủ** (full objective evaluation)
- Mỗi probe được tính vào total evaluations budget
- Với config mặc định: max_probes=20/offspring

**Phân tích budget cho n=48:**
- Control: 4000 evaluations → 40 initial + 104 gens × (40 - 2 elites) ≈ 3992 evals
- GA+2-opt: 4000 evaluations → 40 initial + probes
  - Nếu mỗi offspring có trung bình 15 probes
  - Chỉ tạo được: (4000 - 40) / (1 + 15) ≈ 247 offspring
  - Với P=40, E=2: 247 / 38 ≈ 6.5 generations
  - Thực tế: 20.6 generations (một số offspring dừng sớm do không còn improvement)

**Tại sao kết quả lại kém hơn?**
1. **Số generation quá ít:** 20 generations không đủ để GA explore và exploit không gian tìm kiếm
2. **Mất cân bằng exploration vs exploitation:** 2-opt focus vào exploitation (cải thiện local), nhưng với ít generation, GA không có đủ exploration
3. **Probe overhead:** Mỗi probe 2-opt cải thiện một cá thể, nhưng cost là mất cơ hội tạo nhiều offspring mới từ crossover
4. **Early stopping của probes:** Nhiều probes dừng sớm khi không còn improvement, nhưng vẫn tiêu tốn evaluations

**Kết luận về 2-opt:**
- Bounded 2-opt trong config này **không phù hợp** với budget constraints
- Để 2-opt hiệu quả, cần:
  - Tăng evaluation budget (ví dụ: 20,000 evaluations)
  - Giảm max_probes (ví dụ: 5-10 probes/offspring)
  - Chỉ áp dụng 2-opt cho một số offspring được chọn lọc (không phải tất cả)
  - Hoặc sử dụng delta-cost evaluation (không gọi full objective)

#### 4.5.4. Biểu đồ so sánh các biến thế

_[Hình 4.3: Bốn bar charts (small multiples) cho 4 bài toán. Mỗi chart có 6 cột tương ứng 6 biến thể. NN và Mixed có cột thấp nhất (tốt nhất). GA+2-opt có cột cao nhất (kém nhất).]_

**Chú thích hình 4.3:** Biểu đồ cho thấy NN và Mixed initialization vượt trội rõ ràng khi bài toán lớn hơn. GA+2-opt cho kết quả kém nhất do tiêu tốn quá nhiều evaluations cho local search, dẫn đến số generation quá ít.

#### 4.5.5. Đường hội tụ (Convergence Curves)

_[Hình 4.4: Line chart với trục x là cumulative evaluations, trục y là best-so-far distance. Sáu đường màu khác nhau cho 6 biến thể. Chỉ vẽ cho một seed (seed=11) và một bài toán (n=48) để minh họa.]_

**Quan sát từ convergence curves:**

1. **Control và PMX:** Hội tụ dần đều qua các evaluations, đạt plateau sau khoảng 2500 evaluations

2. **Mixed và NN:** Bắt đầu từ fitness tốt hơn nhiều (do initialization chất lượng cao), sau đó cải thiện nhanh trong 1000 evaluations đầu

3. **Adaptive:** Tương tự control nhưng có một số sudden improvements do mutation rate tăng lên khi stagnation

4. **GA+2-opt:** 
   - Hội tụ **rất nhanh** trong vài trăm evaluations đầu
   - Sau đó **plateau sớm** và không cải thiện thêm
   - Đường hội tụ dừng sớm (tại ~800-1000 evaluations) do chỉ chạy được 20 generations
   - Best-so-far kém hơn các phương pháp khác dù local search cải thiện từng cá thể

**Giải thích:** Đường hội tụ của GA+2-opt dừng sớm vì:
- Chỉ có 20 generations → ít cơ hội tạo offspring mới
- Mỗi generation tạo ít offspring → không khám phá đủ
- 2-opt cải thiện local nhưng không tạo ra global structure tốt hơn

### 4.6. Benchmark đầy đủ trên 7 bộ dữ liệu

Benchmark cuối cùng chạy tất cả 7 bộ dữ liệu với cấu hình cơ sở, population_size=80, max_evaluations=6000, 5 seeds. Tổng cộng 35 runs (7 datasets × 5 seeds).

#### 4.6.1. Kết quả benchmark

| **Thành phố** | **Mean Dist** | **Std Dev** | **Min** | **Max** | **Mean Runtime (s)** | **Status** |
|---|---|---|---|---|---|---|
| 3 | 6.0 | 0.00 | 6 | 6 | 0.0440 | ✓ |
| 4 | 189.0 | 0.00 | 189 | 189 | 0.0471 | ✓ |
| 6 | 1248.0 | 0.00 | 1248 | 1248 | 0.0508 | ✓ |
| 15 | 1200.2 | 13.86 | 1194 | 1225 | 0.0642 | ✓ |
| 26 | 1056.4 | 72.84 | 969 | 1186 | 0.0818 | ✓ |
| 42 | 1166.2 | 26.28 | 1133 | 1211 | 0.1012 | ✓ |
| 48 | 54194.4 | 3861.50 | 51215 | 59638 | 0.1154 | ✓ |

**Thống kê tổng quan:**
- **Tổng số runs:** 35
- **Successful runs:** 35 (100%)
- **Failed runs:** 0
- **Tất cả routes hợp lệ:** ✓ (kiểm tra bằng `validate_route()`)
- **Total runtime:** ~2.7 giây

#### 4.6.2. Phân tích runtime

Runtime tăng tuyến tính theo kích thước bài toán:
- **Tốc độ tăng:** ~0.001s mỗi thành phố (từ n=3 đến n=48)
- **Độ phức tạp thực nghiệm:** O(n) cho mỗi evaluation
- **Với 6000 evaluations:** ~40-115ms total runtime

**Lưu ý:** Runtime phụ thuộc phần cứng và không phải cam kết performance. Các số liệu trên chỉ mang tính tham khảo.

_[Hình 4.5: Line chart với trục x là số thành phố, trục y là runtime trung bình. Đường tuyến tính tăng dần.]_

#### 4.6.3. Biểu đồ mean distance (thang logarit)

_[Hình 4.6: Bar chart với trục y sử dụng thang logarit. Các cột từ trái sang phải: 6, 189, 1248, 1200, 1056, 1166, 54194. Thang logarit giúp hiển thị rõ sự khác biệt giữa các bài toán có độ lớn cost rất khác nhau.]_

**Chú thích hình 4.6:** Biểu đồ sử dụng thang logarit để hiển thị mean distance của 7 bài toán. Bài 48 thành phố có cost lớn hơn nhiều lần so với các bài khác do matrix khoảng cách có giá trị lớn.

### 4.7. Tóm tắt kết quả thực nghiệm

#### 4.7.1. Các phát hiện chính

1. **Toán tử tốt nhất:** Tournament selection (k=3), Order Crossover (OX), Inversion mutation là tổ hợp tốt nhất cho cấu hình hiện tại

2. **Khởi tạo thông minh hiệu quả:** Nearest-Neighbor initialization (đặc biệt là 100% NN hoặc Mixed 25%) cải thiện đáng kể chất lượng nghiệm khi bài toán lớn hơn (cải thiện lên đến 34% tại n=48)

3. **2-opt local search không hiệu quả:** Trong config hiện tại, bounded 2-opt tiêu tốn quá nhiều evaluation budget, dẫn đến số generation quá ít và kết quả kém hơn control (kém hơn lên đến 47% tại n=48)

4. **Adaptive mutation không nhất quán:** Kết quả phụ thuộc vào bài toán cụ thể, cần thêm tuning tham số

5. **Scalability:** GA hoạt động rất tốt với bài toán nhỏ (n≤6), ổn định với bài toán trung bình (n=15-26), và gặp khó khăn với bài toán lớn (n≥42) do không gian tìm kiếm quá lớn

#### 4.7.2. Khuyến nghị cấu hình

Dựa trên kết quả thực nghiệm, khuyến nghị sau để sử dụng GA cho TSP:

**Cho bài toán nhỏ đến trung bình (n ≤ 26):**
```python
population_size = 40-80
selection_method = "tournament", k = 3
crossover_method = "ox", rate = 0.9
mutation_method = "inversion", rate = 0.15
initialization_method = "random"  # hoặc "mixed" với nn_seed_fraction=0.25
elite_count = 2
max_evaluations = 2000-4000
```

**Cho bài toán trung bình lớn đến lớn (n ≥ 42):**
```python
population_size = 80-100
selection_method = "tournament", k = 3
crossover_method = "ox", rate = 0.9
mutation_method = "inversion", rate = 0.15
initialization_method = "nearest_neighbor"  # hoặc "mixed" với nn_seed_fraction=0.25-0.5
elite_count = 2-4
max_evaluations = 10000-20000
```

**Không khuyến nghị (trong cấu hình hiện tại):**
- Rank hoặc Roulette selection
- Scramble mutation
- Bounded 2-opt local search với budget nhỏ

#### 4.7.3. Hạn chế của thực nghiệm

1. **Không có known optimum:** Các bài toán không có optimum đã được xác minh toán học, nên không thể tính gap chính xác

2. **Số lượng seeds giới hạn:** Chỉ 5 seeds, cần nhiều hơn (20-30 seeds) cho kết luận thống kê chặt chẽ hơn

3. **Evaluation budget nhỏ:** 2000-6000 evaluations là ít cho bài toán lớn, nên kết quả có thể cải thiện nhiều nếu tăng budget

4. **Chưa so sánh với EHO:** Thực nghiệm chỉ focus vào GA, chưa có so sánh trực tiếp với EHO trong cùng điều kiện

5. **Chưa so sánh với state-of-the-art:** Chưa so sánh với các solver chuyên nghiệp như Concorde TSP Solver, OR-Tools, hoặc LKH heuristic

6. **Tuning tham số:** Các tham số (population size, mutation rate, etc.) có thể chưa tối ưu cho từng bài toán cụ thể



## CHƯƠNG 5. KẾT LUẬN

Chương cuối cùng này tóm tắt toàn bộ những gì đã đạt được trong đồ án, đánh giá những hạn chế còn tồn tại, và đề xuất các hướng phát triển trong tương lai để cải thiện chất lượng nghiệm cũng như mở rộng khả năng ứng dụng của hệ thống.

### 5.1. Tổng quan về đồ án

Đồ án đã thực hiện thành công việc nghiên cứu, thiết kế và triển khai hai thuật toán metaheuristic để giải quyết bài toán Traveling Salesman Problem (TSP) - một trong những bài toán tối ưu tổ hợp NP-Hard kinh điển trong khoa học máy tính. Thông qua việc áp dụng Genetic Algorithm (GA) và Elephant Herding Optimization (EHO), đồ án đã xây dựng được một hệ thống hoàn chỉnh từ việc biểu diễn nghiệm, thiết kế các toán tử, triển khai thuật toán, đến đánh giá thực nghiệm và so sánh kết quả.

Toàn bộ hệ thống được xây dựng trên ngôn ngữ Python với kiến trúc module hóa rõ ràng, dễ bảo trì và mở rộng. Các thành phần core (domain models, objective function, data loader) được thiết kế độc lập với các solver cụ thể, cho phép dễ dàng thêm thuật toán mới mà không ảnh hưởng đến các phần khác của hệ thống.

### 5.2. Các kết quả đạt được

#### 5.2.1. Triển khai thành công Genetic Algorithm

Genetic Algorithm đã được triển khai đầy đủ và toàn diện với nhiều biến thể và tính năng:

**Các toán tử cơ bản:**
- **Ba phương pháp selection:** Tournament (mặc định), Rank, và Roulette Wheel Selection, mỗi phương pháp có ưu nhược điểm riêng và phù hợp với các tình huống khác nhau
- **Hai toán tử crossover:** Order Crossover (OX) và Partially Mapped Crossover (PMX), cả hai đều bảo tồn hoán vị hợp lệ cho TSP
- **Bốn toán tử mutation:** Inversion (mặc định), Swap, Insertion, và Scramble, cung cấp các mức độ perturbation khác nhau
- **Elitism:** Bảo tồn elite_count cá thể tốt nhất qua các thế hệ, đảm bảo chất lượng nghiệm không bị suy giảm
- **Global Best Archive:** Lưu trữ nghiệm tốt nhất từng gặp trong toàn bộ quá trình, không phụ thuộc vào quần thể hiện tại

**Các phương pháp khởi tạo thông minh:**
- **Random initialization:** Khởi tạo ngẫu nhiên, đảm bảo diversity ban đầu
- **Nearest-Neighbor (NN):** Sử dụng heuristic tham lam multi-start để tạo nghiệm chất lượng tốt
- **Mixed initialization:** Kết hợp NN và random theo tỷ lệ cấu hình được, cân bằng giữa quality và diversity

Thực nghiệm cho thấy NN và Mixed initialization cải thiện đáng kể chất lượng nghiệm khi bài toán lớn hơn, với mức cải thiện lên đến 34% so với random initialization tại bài toán 48 thành phố.

**Các tính năng nâng cao:**
- **Stagnation detection:** Phát hiện và dừng sớm khi quần thể không cải thiện trong một số thế hệ nhất định
- **Adaptive Mutation:** Tự động điều chỉnh mutation rate dựa trên mức độ stagnation và diversity của quần thể
- **Bounded 2-opt Local Search:** Tìm kiếm cục bộ với giới hạn số lượng probes và moves, nhằm cải thiện chất lượng nghiệm

Tuy nhiên, thực nghiệm cũng chỉ ra rằng bounded 2-opt trong cấu hình hiện tại không hiệu quả do tiêu tốn quá nhiều evaluation budget, dẫn đến trade-off không tốt giữa số lượng thế hệ và chất lượng local improvement.

**Cơ chế giám sát và điều kiện dừng:**
- **Nhiều điều kiện dừng linh hoạt:** Số thế hệ tối đa, budget evaluations, thời gian chạy, stagnation, và cooperative stopping từ user
- **History tracking:** Ghi lại snapshot của quần thể theo tần suất cấu hình được, bao gồm best current, best so far, mean fitness, diversity, và số evaluations
- **Reproducibility:** Sử dụng seed để đảm bảo kết quả có thể tái lập, quan trọng cho nghiên cứu và debugging

#### 5.2.2. Triển khai Discrete EHO cho TSP

Elephant Herding Optimization được điều chỉnh cho không gian hoán vị (Discrete EHO - D-EHO) với các thành phần chính:

**Cấu trúc clan và toán tử rời rạc:**
- **Phân chia quần thể thành clans:** Mỗi clan hoạt động như một sub-population độc lập, có matriarch (leader) riêng
- **Hamming Medoid làm tâm clan:** Thay vì trung bình số học (không khả dụng cho hoán vị), sử dụng medoid dựa trên khoảng cách Hamming
- **Guided-Swap operator:** Thay thế phép toán vector liên tục bằng các phép hoán đổi có hướng, với strength parameter (alpha, beta) điều khiển mức độ di chuyển

**Cơ chế cập nhật:**
- **Clan Updating:** Các voi thường di chuyển về phía matriarch với hệ số alpha
- **Matriarch Updating:** Matriarch di chuyển về phía tâm clan với hệ số beta
- **Separating Operator:** Thay thế các voi kém nhất bằng hoán vị ngẫu nhiên mới để duy trì diversity

**Elitism hai cấp:**
- **Clan Archive:** Lưu nghiệm tốt nhất từng gặp của mỗi clan
- **Global Best:** Lưu nghiệm tốt nhất trên toàn bộ quần thể

D-EHO đảm bảo mọi thao tác đều tạo route hợp lệ mà không cần repair, và archive mechanism bảo vệ nghiệm tốt khỏi bị mất khi population evolve.

**Lưu ý quan trọng:** D-EHO là một adaptation cho TSP, không phải phép biến đổi đại số tương đương với EHO liên tục. Các toán tử được thiết kế để phù hợp với không gian hoán vị trong khi vẫn giữ tinh thần của EHO gốc.

#### 5.2.3. Hệ thống công cụ hỗ trợ

**Command-Line Interface (CLI):**
- **Validate command:** Kiểm tra tính hợp lệ của ma trận khoảng cách
- **Solve command:** Chạy GA hoặc EHO với cấu hình chi tiết, hỗ trợ export JSON/CSV
- **Benchmark command:** Chạy nhiều experiments tự động với config file JSON, hỗ trợ statistical analysis

CLI được thiết kế để tích hợp vào pipeline tự động hoặc script, không phụ thuộc GUI.

**Graphical User Interface (GUI):**
- **Framework:** Tkinter + ttk (native trên Windows) + Matplotlib (visualization)
- **Chức năng chính:**
  - Chọn dataset từ registry hoặc browse file
  - Điều chỉnh tất cả tham số GA qua form với validation
  - Chạy solver với progress updates real-time
  - Xem kết quả: tour (1-based notation với circular layout), convergence curve, population diversity, detailed stats
  - Export JSON/CSV/PNG
  - Cooperative stopping (nút Dừng)

GUI phù hợp cho việc khám phá và demo, trong khi CLI phù hợp cho experiments tự động và benchmarking.

**Jupyter Notebooks:**
Thực nghiệm được tổ chức thành ba notebooks với mục đích rõ ràng:
- **Experiment 1-2:** So sánh toán tử OFAT và sensitivity analysis
- **Experiment 3:** Phân phối kết quả và stability analysis
- **Experiment 4:** Đánh giá các biến thể nâng cao (NN, Mixed, Adaptive, 2-opt)

Tất cả notebooks đều pass "Run All" test trong cả hai môi trường (project venv và clean venv), với kết quả numeric reproducible.

#### 5.2.4. Kết quả thực nghiệm chi tiết

**Benchmark trên 7 bộ dữ liệu:**
- Tổng 35 runs (7 datasets × 5 seeds), tất cả successful với routes hợp lệ
- GA đạt kết quả hoàn hảo (std=0, hit rate=100%) với bài toán nhỏ (n≤6)
- Kết quả ổn định với bài toán trung bình (n=15, hit rate=80%)
- Gặp khó khăn với bài toán lớn (n≥42, hit rate=20%, std tăng mạnh)

**So sánh toán tử:**
- Tournament selection tốt hơn Rank và Roulette đáng kể
- OX crossover có lợi thế nhẹ so với PMX
- Inversion mutation cho kết quả tốt nhất, Scramble kém nhất
- PMX có độ ổn định cao hơn (std thấp hơn) nhưng mean cost không tốt bằng OX

**Phương án nâng cao:**
- NN và Mixed initialization: Cải thiện lớn khi bài toán lớn hơn (lên đến 34%)
- Adaptive mutation: Kết quả không nhất quán, cần thêm tuning
- Bounded 2-opt: Kết quả kém do trade-off evaluation budget không tốt

**Convergence behavior:**
- Control và PMX: Hội tụ dần đều
- NN và Mixed: Starting fitness tốt hơn nhiều, hội tụ nhanh ban đầu
- GA+2-opt: Hội tụ nhanh nhưng plateau sớm do ít generation

#### 5.2.5. Kiến trúc phần mềm chất lượng

**Module organization:**
```
src/ga_eho_tsp/
├── domain/          # Shared models, objective, protocols
├── data/            # Matrix loader, registry
├── algorithms/
│   ├── ga/          # GA operators, solver
│   └── eho/         # EHO clans, discrete_ops, solver
├── experiments/     # Benchmark utilities, export
├── gui/             # Tkinter application
└── cli.py           # Command-line interface
```

**Design principles:**
- **Separation of concerns:** Domain logic tách biệt với algorithms và UI
- **Shared objective:** Cả GA và EHO dùng chung `TSPProblem.route_length()`
- **Immutable data:** Routes là tuples, configs là dataclasses frozen
- **Type hints:** Toàn bộ code có type annotations cho maintainability
- **Contracts:** Rõ ràng về input/output, side effects, và invariants

**Testing và verification:**
- Đã chạy 166 regression tests (pytest) trước khi final cleanup
- 2071 assertions checks trong QA release (ngoài repo)
- Tất cả notebooks pass "Run All" trong hai môi trường
- Benchmarks với reproducible results (cùng seed → cùng route/cost/history)

### 5.3. Những hạn chế và thách thức

#### 5.3.1. Hạn chế về thuật toán

**1. Chỉ hỗ trợ Symmetric TSP:**
Cả GA và EHO hiện chỉ hoạt động với ma trận khoảng cách đối xứng (D[i][j] = D[j][i]). Nhiều bài toán thực tế như định tuyến với đường một chiều cần Asymmetric TSP.

**2. Không bảo đảm optimum toàn cục:**
Là các heuristic, GA và EHO không guarantee tìm được nghiệm tối ưu toàn cục. Với bài toán lớn, nghiệm thường ở xa optimum một khoảng đáng kể (8-10% excess quan sát được với n=48).

**3. Scalability giới hạn:**
Với evaluation budget cố định, chất lượng nghiệm giảm nhanh khi kích thước bài toán tăng. Bài toán 48 thành phố đã gặp khó khăn, trong khi các bài toán TSPLIB thực tế có thể lên đến hàng nghìn thành phố.

**4. D-EHO chưa được so sánh trực tiếp với GA:**
Mặc dù D-EHO đã được triển khai và verified correctness, chưa có benchmark đối chứng GA vs EHO trong cùng điều kiện (cùng dataset, seed, evaluation budget). Do đó, chưa thể kết luận thuật toán nào tốt hơn.

**5. Bounded 2-opt trade-off không tốt:**
Local search trong cấu hình hiện tại tiêu tốn quá nhiều evaluation budget, dẫn đến kết quả kém hơn control. Cần thiết kế lại cơ chế local search (ví dụ: delta-cost evaluation, selective application).

#### 5.3.2. Hạn chế về dữ liệu

**1. Không có known optimum:**
Các bộ dữ liệu không có optimum đã được chứng minh toán học. Các số trong tên file chỉ là observations, không phải ground truth. Do đó, không thể tính gap chính xác so với optimum.

**2. Kích thước bài toán giới hạn:**
Chỉ có 7 bộ dữ liệu với tối đa 48 thành phố. Thiếu các bài toán benchmark chuẩn từ TSPLIB (có thể lên đến hàng nghìn thành phố) để đánh giá hiệu năng trên các instances thực tế.

**3. Thiếu metadata:**
Các dataset không có thông tin về nguồn gốc, phương pháp sinh, hoặc đặc điểm đặc biệt (ví dụ: Euclidean, Geometric, Random). Thiếu coordinates để visualization tour trên bản đồ.

#### 5.3.3. Hạn chế về thực nghiệm

**1. Số lượng seeds ít:**
Chỉ 5 seeds cho mỗi cấu hình, trong khi nghiên cứu chặt chẽ thường cần 20-30 seeds cho statistical significance testing (confidence intervals, hypothesis testing).

**2. Evaluation budget nhỏ:**
Budget 2000-6000 evaluations là ít cho bài toán lớn. Nhiều nghiên cứu sử dụng budget 100,000-1,000,000 evaluations, đặc biệt khi so sánh với các thuật toán khác.

**3. Chưa so sánh với state-of-the-art:**
Chưa có benchmark so sánh với các solvers chuyên nghiệp như:
- **Concorde TSP Solver:** Exact solver, có thể giải bài toán lên đến vài nghìn thành phố
- **LKH (Lin-Kernighan-Helsgaun):** State-of-the-art heuristic, thường tìm được optimum hoặc gần optimum với gap <1%
- **OR-Tools (Google):** Industrial-strength solver với nhiều techniques tiên tiến

**4. Tuning tham số chưa tối ưu:**
Các tham số (population size, mutation rate, crossover rate, etc.) có thể chưa phải là tốt nhất cho từng bài toán cụ thể. Chưa có systematic parameter tuning (grid search, Bayesian optimization).

**5. Thiếu statistical testing:**
Chưa có các kiểm định thống kê (t-test, Mann-Whitney U test, Friedman test) để xác định significance của sự khác biệt giữa các biến thể.

#### 5.3.4. Hạn chế về implementation

**1. Chưa có TSPLIB loader:**
Hiện chỉ hỗ trợ ma trận text format đơn giản. Chưa hỗ trợ TSPLIB format (.tsp files) với các types khác nhau (EUC_2D, GEO, ATT, etc.).

**2. No parallelization:**
Solver chạy single-threaded. Với Python, có thể sử dụng multiprocessing để chạy nhiều runs hoặc evaluate nhiều offspring song song.

**3. Chưa có visualization tốt:**
Circular layout trong GUI chỉ là sơ đồ minh họa, không phản ánh vị trí địa lý thực. Với các bài toán có coordinates, cần vẽ tour trên bản đồ 2D.

**4. No executable packaging:**
Chương trình hiện yêu cầu Python environment với dependencies. Chưa có standalone executable (.exe) để phân phối dễ dàng.

**5. Thiếu regression test suite:**
Test suite 166 cases đã bị xóa theo chỉ thị. Dự án hiện không có automated tests thường trực, tạo rủi ro regression khi phát triển tiếp.

### 5.4. Hướng phát triển trong tương lai

#### 5.4.1. Cải thiện thuật toán

**1. Hỗ trợ Asymmetric TSP:**
- Điều chỉnh objective function để không assume symmetry
- Kiểm tra crossover/mutation operators có hoạt động đúng với ATSP
- Test với ATSP benchmarks từ TSPLIB

**2. Triển khai local search hiệu quả:**
- **Lin-Kernighan heuristic:** State-of-the-art local search cho TSP
- **3-opt và k-opt:** Mở rộng 2-opt với neighborhood lớn hơn
- **Delta-cost evaluation:** Tính incremental thay vì full objective
- **Selective application:** Chỉ apply local search cho một số offspring được chọn lọc

**3. Hybrid GA-EHO:**
- Kết hợp ưu điểm của cả hai thuật toán
- Ví dụ: Dùng EHO clans làm sub-populations của GA, với migration giữa clans
- Hoặc: GA cho global search, EHO cho refinement

**4. Adaptive parameter control:**
- Tự động điều chỉnh không chỉ mutation rate mà cả population size, crossover rate, số clans
- Dựa trên metrics như diversity, improvement rate, fitness landscape ruggedness

**5. Multi-objective optimization:**
- Mở rộng để xử lý multiple objectives (ví dụ: minimize distance và maximize robustness)
- Triển khai NSGA-II (Non-dominated Sorting GA) hoặc SPEA2

#### 5.4.2. Mở rộng bài toán

**1. TSP variants:**
- **TSP with Time Windows (TSPTW):** Mỗi thành phố có time window phải visit trong đó
- **Multiple TSP (mTSP):** Nhiều salesman, chia tour thành sub-tours
- **Capacitated TSP:** Mỗi salesman có capacity giới hạn
- **TSP with Profits:** Không bắt buộc visit tất cả, mỗi city có profit riêng

**2. Vehicle Routing Problem (VRP):**
- Mở rộng sang VRP - bài toán tổng quát hơn TSP
- Các biến thể: CVRP (Capacitated), VRPTW (Time Windows), VRPPD (Pickup and Delivery)

**3. Real-world applications:**
- Tích hợp với Google Maps API hoặc OpenStreetMap để lấy real distances
- Xử lý constraints thực tế: traffic, road types, one-way streets
- Application cụ thể: delivery route optimization, school bus routing, drone path planning

#### 5.4.3. Cải thiện thực nghiệm

**1. Comprehensive benchmarking:**
- Tích hợp TSPLIB loader: hỗ trợ các formats EUC_2D, GEO, EXPLICIT, etc.
- Chạy benchmark trên các instances TSPLIB chuẩn (eil51, kroA100, d198, pcb442, etc.)
- So sánh với known optimums từ TSPLIB

**2. So sánh với state-of-the-art:**
- Benchmark vs LKH, Concorde, OR-Tools
- Báo cáo gap percentage, runtime ratio
- Analyze trade-off giữa solution quality và computational cost

**3. Statistical analysis chặt chẽ:**
- Tăng số seeds lên 20-30 cho mỗi cấu hình
- Thực hiện hypothesis testing (Wilcoxon, Mann-Whitney U)
- Report confidence intervals, effect sizes
- Visualize distributions với box plots, violin plots

**4. Parameter tuning systematic:**
- Grid search hoặc Random search cho parameter space
- Bayesian Optimization hoặc Hyperband cho efficient tuning
- Analyze parameter sensitivity với ANOVA hoặc regression

**5. Performance profiling:**
- Identify bottlenecks bằng cProfile, line_profiler
- Optimize hot paths với Numba JIT hoặc Cython
- Measure scalability: runtime vs problem size

#### 5.4.4. Cải thiện công cụ

**1. GUI enhancements:**
- **Visualization tốt hơn:**
  - Vẽ tour trên 2D coordinates khi available
  - Animation của evolution process
  - Interactive controls: zoom, pan, select individual
- **Parameter presets:** Lưu và load các cấu hình đã được tune cho các bài toán types khác nhau
- **Multi-run comparison:** Chạy nhiều configs và so sánh trực tiếp trên GUI
- **EHO GUI:** Hoàn thiện giao diện cho EHO (hiện đang "in development")

**2. CLI improvements:**
- **Watch mode:** Tự động re-run khi config file thay đổi
- **Progress bars:** Hiển thị tiến trình với tqdm hoặc rich
- **Parallel execution:** Chạy nhiều configs song song với multiprocessing
- **Export formats:** Thêm Markdown, LaTeX tables cho report writing

**3. Web interface:**
- **Flask hoặc FastAPI backend:** RESTful API cho solver
- **React hoặc Vue.js frontend:** Modern web UI
- **Cloud deployment:** Deploy lên Heroku, AWS, hoặc Google Cloud
- **Collaboration features:** Nhiều users có thể share results, configs

**4. Jupyter widgets:**
- Interactive controls trong notebook với ipywidgets
- Real-time updates của convergence curves
- Side-by-side comparison của multiple runs

**5. Packaging và distribution:**
- **PyPI package:** Publish lên Python Package Index
- **Conda package:** Phân phối qua conda-forge
- **Docker image:** Containerized environment với tất cả dependencies
- **Executable:** PyInstaller hoặc Nuitka để tạo standalone .exe

#### 5.4.5. Nghiên cứu và công bố

**1. Viết paper:**
- Tổng hợp kết quả thành technical report hoặc paper
- Submit lên conference: IEEE CEC, GECCO, hoặc workshop về metaheuristics
- Hoặc journal: Swarm and Evolutionary Computation, Applied Soft Computing

**2. Open source contribution:**
- Publish code lên GitHub với MIT license
- Viết documentation với Sphinx hoặc MkDocs
- Create tutorials, examples
- Encourage community contributions

**3. Educational materials:**
- Video tutorials trên YouTube
- Blog posts giải thích thuật toán, implementation details
- Workshops hoặc talks tại trường/meetups

**4. Collaboration với industry:**
- Liên hệ với các công ty logistics, delivery để pilot real applications
- Tham gia hackathons, competitions (Kaggle, etc.)

### 5.5. Bài học kinh nghiệm

#### 5.5.1. Về thiết kế thuật toán

**1. Khởi tạo quan trọng:**
Nearest-Neighbor initialization cải thiện đáng kể chất lượng nghiệm, đặc biệt với bài toán lớn. Đầu tư vào heuristic khởi tạo tốt là worthwhile.

**2. Local search cần careful design:**
Bounded 2-opt trong cấu hình hiện tại không hiệu quả do trade-off evaluation budget. Local search cần balance giữa improvement quality và computational cost.

**3. Diversity là critical:**
Stagnation detection, adaptive mutation, và separation operator đều nhằm duy trì diversity. Premature convergence là vấn đề lớn với heuristics.

**4. Benchmarking is essential:**
Không thể đánh giá thuật toán chỉ bằng một vài runs. Cần systematic experiments với multiple seeds, datasets, và configs.

#### 5.5.2. Về software engineering

**1. Separation of concerns:**
Tách domain logic khỏi algorithms và UI giúp code dễ maintain và extend. Shared objective function đảm bảo fairness khi so sánh algorithms.

**2. Immutability helps:**
Routes và configs immutable giúp tránh bugs do side effects. Debugging dễ hơn khi không lo data bị mutate unexpected.

**3. Type hints are valuable:**
Type annotations không chỉ giúp IDE autocomplete mà còn catch bugs early với mypy.

**4. Tests prevent regressions:**
Việc xóa test suite 166 cases là một risk. Automated tests là investment quan trọng cho long-term maintenance.

**5. Documentation matters:**
Các file `.md` trong `docs/` giúp onboard contributors mới và làm reference sau này. Code comments giải thích "why", không chỉ "what".

#### 5.5.3. Về quản lý dự án

**1. Incremental development:**
Xây dựng từng phần nhỏ (baseline GA → operators → variants → EHO → GUI) thay vì big-bang approach.

**2. Version control discipline:**
Git commits với messages rõ ràng giúp track changes và rollback khi cần. Branching strategy (nếu có) giúp parallel development.

**3. Reproducibility first:**
Sử dụng seeds, ghi lại environment (requirements.txt), và document experiments giúp results reproducible.

**4. Regular backup:**
Các snapshots, backups ngoài repo (theo source_attribution.md) là insurance quý giá.

### 5.6. Kết luận cuối cùng

Đồ án đã thành công trong việc triển khai và đánh giá hai thuật toán metaheuristic cho bài toán Traveling Salesman Problem. Genetic Algorithm với các toán tử đa dạng và Elephant Herding Optimization được điều chỉnh cho không gian hoán vị đã được triển khai đầy đủ, kèm theo hệ thống công cụ hỗ trợ từ CLI, GUI đến Jupyter notebooks.

Kết quả thực nghiệm cho thấy GA hoạt động tốt với bài toán nhỏ đến trung bình, và cải thiện đáng kể với khởi tạo thông minh (Nearest-Neighbor). Tuy nhiên, với bài toán lớn, thuật toán còn nhiều dư địa cải thiện thông qua local search hiệu quả hơn, parameter tuning, và tăng evaluation budget.

Mặc dù còn nhiều hạn chế và hướng phát triển, đồ án đã xây dựng được một foundation vững chắc cho các nghiên cứu và ứng dụng tiếp theo. Kiến trúc module hóa, code quality cao, và documentation chi tiết tạo điều kiện thuận lợi cho việc mở rộng và cải thiện hệ thống trong tương lai.

Quan trọng nhất, đồ án đã cung cấp hiểu biết sâu sắc về cách hoạt động của các thuật toán metaheuristic, các trade-offs trong thiết kế thuật toán, và phương pháp đánh giá thực nghiệm chặt chẽ - những kiến thức và kinh nghiệm quý giá cho nghiên cứu và phát triển tiếp theo trong lĩnh vực tối ưu tổ hợp và trí tuệ nhân tạo.


## **TÀI LIỆU THAM KHẢO** 

[1] J. H. Holland, _Adaptation in Natural and Artificial Systems_ , University of Michigan Press, Ann Arbor, MI, USA, 1975. 

[2] D. E. Goldberg, _Genetic Algorithms in Search, Optimization, and Machine Learning_ , Addison-Wesley, Reading, MA, USA, 1989. 

[3] D. L. Applegate, R. E. Bixby, V. Chvátal, and W. J. Cook, _The Traveling Salesman Problem: A Computational Study_ , Princeton University Press, Princeton, NJ, USA, 2006. 

[4] I. M. Oliver, D. J. Smith, and J. R. C. Holland, "A study of permutation crossover operators on the traveling salesman problem," in _Proc. 2nd Int. Conf. Genetic Algorithms_ , 1987, pp. 224–230. 

[5] G. Wang, S. Deb, and L. dos Santos Coelho, "Elephant herding optimization," in _Proc. 3rd Int. Symp. Computational and Business Intelligence (ISCBI)_ , Bali, Indonesia, 2015, pp. 1–5. 

[6] A. Slowik, Ed., _Swarm Intelligence Algorithms: A Tutorial_ , CRC Press, Boca Raton, FL, USA, 2020. 

[7] T. Stützle, "Local search algorithms for combinatorial problems," Ph.D. dissertation, Darmstadt University of Technology, 1998. 

## **PHỤ LỤC** 

**Link GitHub:** <u>https://github.com/datweb07/ga-eho-tsp</u> 

#### **Hướng dẫn cài đặt/sử dụng chương trình:** 

#### **1. Yêu cầu môi trường** 

|**Thành phần**|**Phiên bản**|
|---|---|
|Python|3.11 trở lên|
|Hệ điều hành|Windows 10/11, macOS, Linux|
|RAM|Tối thiểu 4GB|



#### **2. Cài đặt môi trường** 

Từ thư mục gốc repository, thực hiện các bước sau: 

#### **Bước 1: Tạo virtual environment** 

None python --version          # Kiểm tra Python >= 3.11 python -m venv .venv 

#### **Bước 2: Kích hoạt môi trường** 

Trên Windows (PowerShell): 

None .\.venv\Scripts\Activate.ps1 

Nếu PowerShell báo lỗi execution policy: 

None 

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser .\.venv\Scripts\Activate.ps1 

Trên macOS/Linux: 

Shell source .venv/bin/activate 

#### **Bước 3: Cài đặt thư viện** 

None python -m pip install -r requirements.txt 

#### **Bước 4: Cài đặt package ở chế độ editable (cần thiết để chạy notebook)** 

None python -m pip install -e . 

#### **Bước 5: Xử lý encoding trên Windows (nếu cần)** 

Nếu terminal Windows hiển thị lỗi ký tự tiếng Việt hoặc mũi tên, thiết lập encoding cho phiên làm việc: 

None $env:PYTHONIOENCODING = "utf-8" 

#### **3. Kiểm tra cài đặt** 

Chạy lệnh compile để kiểm tra toàn bộ source: 

None python -m compileall -q src 

Kiểm tra tất cả bộ dữ liệu: 

None python -m ga_eho_tsp.cli validate 

Lệnh này sẽ kiểm tra tất cả file trong thư mục data/, in ra thông báo hợp lệ cho từng ma trận (tên bài, số thành phố, tính đối xứng, đường chéo 0, giá trị hữu hạn). 

#### **4. Chạy giao diện GUI** 

None python -m ga_eho_tsp.gui 

Hoặc sử dụng script Demo: 

None python Demo.py 

Giao diện cho phép: 

1. Chọn bộ dữ liệu từ danh sách 

2. Điều chỉnh các tham số GA (population, generations, mutation rate, v.v.) 

3. Chọn selection/crossover/mutation method 

4. Chạy GA và xem tiến trình real-time 

5. Xem kết quả: distance, tour, đồ thị hội tụ 

|**Thành viên**|**Nhiệm vụ**|
|---|---|
|TrươngThành Đạt||
|Nguyễn Tấn Khiêm||
|Nguyễn PhươngChinh||
|Lại Thành Đạt||



