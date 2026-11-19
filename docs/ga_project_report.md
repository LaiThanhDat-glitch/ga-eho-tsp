# Nội dung báo cáo đồ án - phần Genetic Algorithm cho TSP

> **Phạm vi tài liệu:** Đây là bản nội dung báo cáo cho phần Genetic Algorithm (GA), được viết theo cấu trúc chương trong file PDF mẫu `AI FINAL PROJECT.pdf`. PDF hiện có tiêu đề đúng với đề tài GA–EHO–TSP, nhưng mục lục và các tiêu đề nội dung bên trong vẫn ghi Tic Tac Toe, còn phần chương và tài liệu tham khảo để trống. Vì vậy, tài liệu này dùng cấu trúc chương làm khung trình bày, thay nội dung Tic Tac Toe bằng bài toán TSP theo đề tài của repository, và không coi nội dung mẫu sai chủ đề là yêu cầu thay đổi đề tài. Tài liệu chỉ trình bày GA; EHO được ghi nhận là chưa có solver.

## Đề tài

**Ứng dụng thuật toán Genetic Algorithm và Elephant Herding Optimization cho bài toán người du lịch (Traveling Salesman Problem - TSP)**

### Phạm vi phần GA

Phần này trình bày mô hình TSP, cách biểu diễn một hành trình, thuật toán GA được cài đặt trong repository, các kết quả thực nghiệm đã được ghi nhận và giới hạn hiện tại. Tên đề tài chung vẫn bao gồm cả GA và EHO theo phạm vi đồ án. Tuy nhiên, nội dung dưới đây chỉ mô tả GA để có thể hoàn thiện trước; không mô tả D-EHO như một thuật toán đã triển khai hoặc đã thử nghiệm.

GA chính thức nằm trong package `src/ga_eho_tsp/algorithms/ga/` và dùng chung mô hình bài toán ở `src/ga_eho_tsp/domain/`. Đầu mối sở hữu domain và GA là Trương Thành Đạt. Những thay đổi đối với hợp đồng dữ liệu chung cần được đề xuất và leader xem xét trước khi thực hiện.

# CHƯƠNG 1. TỔNG QUAN

## 1.1. Giới thiệu bài toán người du lịch

Bài toán người du lịch, thường được gọi là Traveling Salesman Problem (TSP), mô tả tình huống một người cần đi qua một tập thành phố. Mỗi thành phố phải được thăm đúng một lần, người đi bắt đầu từ một thành phố xác định, sau đó quay lại thành phố xuất phát. Mục tiêu là chọn thứ tự ghé thăm sao cho tổng chi phí của cả chuyến đi nhỏ nhất.

Trong đồ án này, chi phí giữa hai thành phố được lưu thành ma trận khoảng cách. Ma trận có một hàng và một cột cho mỗi thành phố. Phần tử ở hàng `i`, cột `j` biểu diễn chi phí đi từ thành phố `i` đến thành phố `j`. Phiên bản hiện tại tập trung vào symmetric TSP: chi phí đi từ `i` đến `j` bằng chi phí đi ngược từ `j` về `i`. Đây là một bài toán tổ hợp vì số thứ tự có thể ghé thăm tăng rất nhanh khi số thành phố tăng. Do đó, việc liệt kê tất cả hành trình để tìm đáp án tốt nhất chỉ phù hợp với các bài rất nhỏ.

## 1.2. Phát biểu bài toán

Gọi tập thành phố là `V = {0, 1, ..., n-1}` và ma trận khoảng cách là `D`. Một hành trình hợp lệ là hoán vị `π` của toàn bộ các thành phố, trong đó `π[0] = 0`. Chi phí của hành trình là tổng chi phí đi giữa hai thành phố liên tiếp, cộng thêm cạnh quay từ thành phố cuối về thành phố 0:

```text
L(π) = D[π[0], π[1]] + D[π[1], π[2]] + ...
       + D[π[n-2], π[n-1]] + D[π[n-1], π[0]]
```

Mục tiêu là tìm hành trình có `L(π)` nhỏ nhất. Trong chương trình, route được lưu dưới dạng tuple 0-based, ví dụ `(0, 3, 2, 1)`. Route lõi không lặp lại thành phố 0 ở cuối; hàm mục tiêu tự tính cạnh quay về đầu. Khi trình bày cho người dùng, CLI hoặc GUI có thể thêm thành phố 0 ở cuối để biểu diễn hành trình khép kín.

Một nghiệm phải thỏa mãn đồng thời ba điều kiện: có đúng `n` phần tử, bắt đầu bằng 0, và mỗi số từ 0 đến `n-1` xuất hiện đúng một lần. Việc kiểm tra các điều kiện này giúp loại các chuỗi không phải hành trình, chẳng hạn route bị thiếu thành phố, có thành phố lặp hoặc làm thay đổi điểm xuất phát.

Ma trận đầu vào được kiểm tra là ma trận vuông có ít nhất ba thành phố, các chi phí hữu hạn và không âm, đường chéo bằng 0, đồng thời đối xứng. Dữ liệu của repository là các ma trận văn bản, mỗi dòng chứa một hàng số cách nhau bằng khoảng trắng và không có dòng tiêu đề. Những số trong tên file dữ liệu chỉ được xem là gợi ý của nguồn ban đầu; chúng chưa được xác minh độc lập như optimum chính thức.

## 1.3. Hướng tiếp cận giải quyết

GA mô phỏng quá trình tiến hóa để tìm kiếm nghiệm tốt. Thay vì chỉ duy trì một hành trình, thuật toán giữ một quần thể gồm nhiều hành trình. Mỗi vòng lặp chọn các hành trình cha, kết hợp một phần thứ tự của chúng để tạo hành trình con, áp dụng đột biến để thay đổi một đoạn, sau đó hình thành quần thể kế tiếp.

Trong đồ án, một cá thể chính là một route hợp lệ của TSP. Chất lượng của cá thể được đo trực tiếp bằng tổng độ dài hành trình. Vì bài toán cần tối thiểu hóa, route có tổng chi phí nhỏ hơn được xem là tốt hơn. Cùng một hàm mục tiêu `TSPProblem.route_length` được dùng trong toàn bộ GA; route không có một công thức fitness riêng khác với công thức dùng để báo cáo kết quả.

GA là phương pháp tìm kiếm ngẫu nhiên có định hướng, nên một lần chạy không đảm bảo tìm được optimum toàn cục. Seed được truyền rõ ràng để có thể lặp lại cùng một cấu hình. Kết quả thí nghiệm vì vậy cần được đọc cùng số seed, số lần đánh giá hàm mục tiêu, thời gian chạy và cách chọn cấu hình, thay vì chỉ nhìn vào một route tốt nhất.

# CHƯƠNG 2. GIẢI THUẬT DI TRUYỀN

## 2.1. Giới thiệu về Genetic Algorithm

Genetic Algorithm là một thuật toán tối ưu lấy cảm hứng từ chọn lọc tự nhiên. Thuật toán bắt đầu với một tập nghiệm ứng viên, đánh giá chất lượng từng nghiệm, sau đó dùng các nghiệm tốt để tạo thế hệ tiếp theo. Qua nhiều vòng lặp, các nghiệm tốt có cơ hội được giữ lại hoặc truyền một phần cấu trúc sang các nghiệm mới.

Với bài toán TSP, việc biểu diễn bằng chuỗi bit thông thường không thuận tiện vì một hành trình cần là hoán vị, không được lặp hoặc bỏ thành phố. Do đó, repository dùng permutation representation: mỗi route chứa đầy đủ các thành phố đúng một lần và khóa thành phố 0 ở vị trí đầu. Các toán tử lai ghép và đột biến đều chỉ thao tác trên phần route sau thành phố 0 để giữ bất biến này.

Các tham số GA có ảnh hưởng đến sự cân bằng giữa khai thác nghiệm hiện có và tìm kiếm vùng mới. Quần thể lớn hơn thường giữ được nhiều phương án hơn nhưng cần nhiều lượt đánh giá. Mutation rate cao tạo thay đổi thường xuyên hơn nhưng có thể phá vỡ cấu trúc tốt. Crossover rate quyết định tần suất ghép cặp cha mẹ. Elitism giữ một số nghiệm tốt nhất để chúng không bị mất ở thế hệ sau. Các tham số này cần được so sánh dưới cùng điều kiện tính toán trước khi kết luận cấu hình nào tốt hơn.

## 2.2. Cách áp dụng GA cho TSP trong repository

### 2.2.1. Luồng xử lý tổng quát

Quy trình của một lần chạy GA gồm các bước sau:

1. Kiểm tra `TSPProblem` và `GAConfig`, bao gồm giới hạn tham số, ma trận và ngân sách tính toán.
2. Khởi tạo quần thể route. Mặc định, mỗi route được sinh ngẫu nhiên và chuẩn hóa để thành phố 0 luôn đứng đầu.
3. Tính độ dài cho từng route bằng shared objective, đếm số lần đánh giá và lưu best route toàn cục.
4. Ghi snapshot ban đầu vào lịch sử. Snapshot chứa best hiện tại, best toàn lịch sử, trung bình chi phí, số evaluations, thời gian và diversity.
5. Tạo quần thể kế tiếp bằng cách sao chép elites, chuẩn bị selection, chọn cha mẹ, lai ghép, đột biến và đánh giá con.
6. Chỉ commit một thế hệ khi quần thể mới đã đầy đủ. Nếu dừng giữa thế hệ do cancellation, time limit hoặc evaluation budget, các ứng viên đã được đánh giá vẫn được xét vào global best nhưng quần thể dở dang không được commit.
7. Kiểm tra điều kiện dừng, ghi snapshot cuối và trả `RunResult` chứa route tốt nhất của toàn bộ lần chạy, không chỉ route tốt nhất trong quần thể cuối.

Pseudocode dưới đây mô tả đường chạy mặc định. Các tùy chọn như PMX, khởi tạo nearest-neighbor, adaptive mutation và 2-opt chỉ được bật khi người dùng chọn rõ ràng.

```text
kiểm tra bài toán và cấu hình
tạo RNG riêng từ seed
tạo P route ngẫu nhiên
đánh giá P route; lưu global best và history ở iteration 0

cho mỗi iteration trong giới hạn cấu hình:
    kiểm tra stop request, time limit và evaluation budget
    giữ lại E cá thể tốt nhất cùng chi phí đã biết
    chuẩn bị phương pháp selection cho quần thể hiện tại
    khi quần thể kế tiếp chưa đủ P cá thể:
        chọn hai cha mẹ
        với xác suất crossover_rate, áp dụng OX (mặc định)
        với từng con cần thêm:
            áp dụng inversion mutation với xác suất mutation_rate
            đánh giá bằng TSPProblem.route_length
            cập nhật global best nếu tốt hơn
            thêm con vào quần thể kế tiếp
    nếu thế hệ đầy đủ thì commit, cập nhật stagnation và ghi history

trả global best và RunResult
```

### 2.2.2. Khởi tạo quần thể và seed

Mặc định, GA dùng random initialization. Các hoán vị được tạo bằng RNG của lần chạy, không sử dụng bộ sinh số ngẫu nhiên toàn cục. Do vậy, khi giữ nguyên dữ liệu, cấu hình và seed, route, distance, số evaluations và lịch sử số học có thể tái lập; thời gian thực tế có thể thay đổi giữa các lần chạy.

Repository cũng có hai phương án khởi tạo opt-in. `nearest_neighbor` tạo route tham lam từ nhiều điểm bắt đầu khác nhau: ở mỗi bước chọn thành phố chưa thăm có cạnh gần nhất, nếu bằng nhau thì chọn mã thành phố nhỏ hơn. `mixed` đặt một tỷ lệ route nearest-neighbor vào quần thể, phần còn lại là route ngẫu nhiên. Đây là biến thể khởi tạo của GA, không phải solver thứ ba, và kết quả không được gọi là nghiệm tối ưu chỉ vì bắt đầu bằng một heuristic.

### 2.2.3. Chọn cha mẹ

Selection quyết định cá thể nào có cơ hội làm cha mẹ. Bài toán dùng minimization, nên chi phí nhỏ hơn phải có lợi thế. Ba phương pháp hiện có là:

- **Tournament:** lấy ngẫu nhiên một nhóm `k` cá thể khác nhau và chọn cá thể có chi phí thấp nhất trong nhóm. Đây là lựa chọn mặc định.
- **Rank:** sắp thứ tự cá thể từ tốt đến kém và gán trọng số theo thứ hạng. Cách này làm selection ít nhạy với chênh lệch thô về độ dài route.
- **Roulette wheel:** biến chi phí thành trọng số chọn phù hợp với minimization. Trường hợp các chi phí bằng nhau hoặc trọng số bằng 0 được xử lý bằng lựa chọn đều thay vì chia cho 0 hoặc tạo phân phối không hợp lệ.

Trong mỗi thế hệ, phân phối rank/roulette được chuẩn bị một lần rồi dùng nhiều lần để lấy cha mẹ. Việc chuẩn bị không thay đổi population hoặc chi phí đã tính. Hai lượt chọn cha mẹ là độc lập, nên cùng một route có thể được chọn hai lần.

### 2.2.4. Lai ghép permutation

**Order Crossover (OX)** là phương pháp mặc định. OX chọn một đoạn liên tiếp trên phần đuôi của route cha thứ nhất và giữ nguyên đoạn đó ở cùng vị trí trong con. Sau đó, thuật toán duyệt route cha còn lại theo thứ tự vòng, bỏ các thành phố đã có trong đoạn giữ lại và điền vào các vị trí trống. Nhờ vậy, con vẫn là permutation hợp lệ và giữ được thông tin thứ tự từ cả hai cha mẹ.

**Partially Mapped Crossover (PMX)** là một lựa chọn khác. PMX giữ một đoạn của cha thứ nhất, rồi dùng ánh xạ giữa đoạn của hai cha mẹ để xử lý thành phố bị trùng ở ngoài đoạn. Cả OX và PMX chỉ thao tác trên tail, không đổi vị trí thành phố 0. Hai toán tử không sửa route cha tại chỗ và dùng RNG được truyền vào.

### 2.2.5. Đột biến

Mutation được áp dụng với một xác suất trên mỗi cá thể con. Điều này giúp tham số mutation rate có cùng ý nghĩa giữa các phương pháp. Bốn phương pháp hiện có là:

- **Inversion:** đảo ngược thứ tự một đoạn liên tiếp. Đây là mutation mặc định.
- **Swap:** đổi chỗ hai thành phố ở hai vị trí khác nhau.
- **Insertion:** lấy một thành phố ra và chèn vào vị trí khác.
- **Scramble:** xáo trộn thứ tự bên trong một đoạn.

Mọi thao tác đều giữ thành phố 0 đứng đầu và không làm thay đổi route cha. Nếu mutation rate bằng 0 thì route con được giữ nguyên; nếu bằng 1 thì toán tử được áp dụng cho từng route con, dù một số thao tác scramble có thể tình cờ tạo lại cùng thứ tự.

### 2.2.6. Elitism và global best

Elitism sao chép `elite_count` route tốt nhất sang quần thể kế tiếp và giữ lại fitness đã tính. Điểm số không bị gán về 0, vì cách đó sẽ làm sai thứ tự minimization và có thể chọn lặp sai cá thể. Kích thước quần thể được lấp theo số slot còn thiếu, vì vậy cấu hình có population size lẻ không làm giảm kích thước thế hệ.

Song song với population hiện tại, solver duy trì global best. Mỗi route được đánh giá đều có cơ hội cập nhật archive này. Kết quả cuối do đó vẫn giữ route tốt nhất đã gặp, ngay cả khi route ấy không còn nằm trong quần thể cuối hoặc thuật toán bị dừng giữa một thế hệ. Đây là điểm quan trọng để kết quả không xấu đi chỉ vì một thế hệ mới có các con kém hơn.

### 2.2.7. Điều kiện dừng và lịch sử

GA dừng khi đạt số generations hoặc `max_iterations` nhỏ hơn, hết `max_evaluations`, hết time limit, nhận yêu cầu cancellation, hoặc đạt `stagnation_patience` nếu cấu hình bật điều kiện trì trệ. Việc khởi tạo được đánh giá đầy đủ trước khi bắt đầu các thế hệ, nên `max_evaluations` phải đủ cho population ban đầu. Time limit và cancellation được kiểm tra tại các điểm an toàn giữa các lượt đánh giá; chúng là cơ chế dừng hợp tác, không phải bảo đảm hard real-time.

`RunResult` lưu thuật toán, tên bài toán, best route, best distance, số iteration hoàn tất, số evaluations, elapsed time, seed, history, cấu hình đã dùng, stopping reason, trạng thái hợp lệ và metadata. `IterationStat` lưu iteration, best trong population đã commit, best toàn cục, fitness trung bình, evaluations tích lũy, thời gian và population diversity. History có snapshot ban đầu và snapshot cuối; `record_history_every` điều khiển tần suất ghi các mốc trung gian.

Callback progress nhận một snapshot read-only. Callback stop được kiểm tra trong solver. Solver không phụ thuộc GUI, không thực hiện I/O trong vòng lặp và không dùng RNG toàn cục. CLI, benchmark và GUI gọi cùng API solver; vì vậy phần trình bày không thay đổi logic tối ưu.

### 2.2.8. Các phương án nâng cao đã chọn

GA có thêm một số lựa chọn ngoài đường mặc định:

- **Stagnation stopping:** dừng sau số thế hệ đầy đủ liên tiếp không cải thiện global best đã cấu hình.
- **Adaptive mutation:** điều chỉnh mutation rate theo mức trì trệ và diversity; tùy chọn này tắt mặc định để giữ hành vi baseline.
- **Bounded 2-opt:** thử các phép đảo đoạn theo first-improvement với giới hạn số move, số probe và evaluation budget. Mỗi probe tính lại toàn bộ objective và được tính vào evaluation count, do đó không bị xem như thao tác miễn phí.
- **PMX và nearest-neighbor/mixed initialization:** cho phép so sánh các lựa chọn GA mà không thay shared objective hoặc route representation.

2-opt được xem là thành phần local search hỗ trợ GA, không được giới thiệu thành thuật toán tối ưu chính thứ ba. Kết quả thí nghiệm hiện tại không cho thấy 2-opt luôn có lợi dưới cùng budget; vì vậy nó vẫn là tùy chọn và không được bật trong cấu hình mặc định.

### 2.2.9. Tổ chức mã nguồn

| Module | Vai trò |
|---|---|
| `domain/models.py` | Schema `TSPProblem`, `GAConfig`, `RunResult`, `IterationStat` và kiểm tra cấu hình |
| `domain/objective.py` | Kiểm tra ma trận/route và tính chi phí chu trình |
| `data/matrix_loader.py` | Đọc ma trận khoảng trắng thành `TSPProblem` |
| `data/registry.py` | Khai báo tên các bộ dữ liệu và để `known_optimum=None` khi chưa xác minh |
| `algorithms/ga/initialization.py` | Random, nearest-neighbor và mixed initialization |
| `algorithms/ga/selection.py` | Tournament, rank và roulette selection |
| `algorithms/ga/crossover.py` | OX và PMX |
| `algorithms/ga/mutation.py` | Inversion, swap, insertion và scramble |
| `algorithms/ga/survivor.py` | Elitism và xây dựng phần quần thể sống sót |
| `algorithms/ga/monitoring.py` | Diversity và mutation rate thích nghi |
| `algorithms/ga/local_search.py` | Bounded 2-opt opt-in |
| `algorithms/ga/solver.py` | Vòng lặp GA, global best, history, stop và kết quả |
| `cli.py` | Lệnh validate, solve GA và benchmark nhiều seed |
| `experiments/benchmark.py` | Chạy lặp, kiểm tra kết quả và xuất summary/CSV/JSON |
| `gui/` | Form Tkinter, điều phối solver ở worker và biểu diễn kết quả GA |

Không tồn tại package `algorithms/eho/` có solver trong source hiện tại. `EHOConfig` trong domain và một mục EHO bị khóa ở registry GUI chỉ là schema/điểm handoff, không phải EHO đã cài đặt. CLI cũng từ chối `--algorithm eho` thay vì trả kết quả giả.

# CHƯƠNG 3. CÁC KẾT QUẢ THỰC NGHIỆM

## 3.1. Thiết kế thí nghiệm và các tình huống

Repository có bảy ma trận dữ liệu 3, 4, 6, 15, 26, 42 và 48 thành phố. Theo tài liệu nghiệm thu trong `docs/experiments.md`, benchmark mẫu sử dụng cấu hình population size 80, giới hạn 6.000 objective evaluations cho mỗi lần chạy và năm seed `[11, 23, 37, 53, 71]`. Tổng cộng có 35 lần chạy: bảy bộ dữ liệu nhân với năm seed. Tất cả lần chạy benchmark đó được báo cáo là hoàn tất hợp lệ trong bản ghi nghiệm thu.

Các thí nghiệm notebook được chia thành ba nhóm. Nhóm thứ nhất so sánh selection, crossover, mutation và một số thay đổi tham số trên bài 15 thành phố. Nhóm thứ hai khảo sát phân bố kết quả và độ ổn định trên các bài có kích thước khác nhau, đồng thời dùng exhaustive enumeration chỉ để kiểm tra các trường hợp nhỏ. Nhóm thứ ba so sánh random initialization với nearest-neighbor/mixed, PMX, adaptive mutation và GA kết hợp 2-opt trên các bài 15, 26, 42 và 48 thành phố.

Các phép so sánh cần dùng cùng dataset, seed set, cấu hình liên quan và số evaluation tương đương. Khi chỉ cố định số generation mà population thay đổi, số objective evaluations cũng thay đổi; vì vậy hai kiểu so sánh này không thể được đánh đồng. Runtime được ghi lại để mô tả chi phí thực tế nhưng có thể biến động theo máy và môi trường. Tên file dataset không được dùng làm optimum nếu chưa có nguồn kiểm chứng.

## 3.2. Kết quả so sánh operator trên bài 15 thành phố

Bảng dưới đây chép lại kết quả đã ghi trong tài liệu thí nghiệm của repository, với 40 cá thể, hai elites, ngân sách 2.000 evaluations và năm seed. Đơn vị distance là đơn vị chi phí của ma trận. Độ lệch chuẩn là sample standard deviation giữa các lần chạy.

| Biến thể | Distance trung bình | Trung vị | Độ lệch chuẩn mẫu |
|---|---:|---:|---:|
| GA mặc định (tournament + OX + inversion) | 1235.0 | 1225 | 43.86 |
| Rank selection | 1413.6 | 1402 | 81.79 |
| Roulette selection | 1400.8 | 1340 | 158.48 |
| PMX thay OX | 1275.4 | 1279 | 38.34 |
| Swap mutation | 1317.0 | 1289 | 113.40 |
| Insertion mutation | 1319.8 | 1287 | 68.16 |
| Scramble mutation | 1473.0 | 1391 | 152.78 |

Trong cấu hình cụ thể này, các biến thể được thử không tốt hơn trung bình của cấu hình mặc định. Điều đó không chứng minh chúng luôn kém: kết luận chỉ áp dụng cho ma trận, seed, budget và tham số đã chọn. Một thử nghiệm nhỏ với năm seed cũng chưa đủ để khẳng định thứ hạng ổn định trên mọi TSP.

## 3.3. Độ phân tán kết quả theo kích thước bài toán

Kết quả được lưu trong notebook phân bố sử dụng năm seed cho từng dataset. “Best observed” là route tốt nhất trong số lần chạy mẫu; nó không phải optimum đã chứng minh cho các bài lớn.

| Số thành phố | Min | Mean | Median | Max | Độ lệch chuẩn mẫu | Tỷ lệ đạt min quan sát |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 6 | 6 | 6 | 6 | 0 | 100% |
| 6 | 1248 | 1248 | 1248 | 1248 | 0 | 100% |
| 15 | 1194 | 1200.2 | 1194 | 1225 | 13.86 | 80% |
| 26 | 969 | 1046 | 1034 | 1186 | 82.85 | 20% |
| 42 | 1102 | 1151.6 | 1133 | 1211 | 49.75 | 20% |
| 48 | 51215 | 55404.6 | 55339 | 59638 | 3031.79 | 20% |

Ở hai bài nhỏ được ghi lại, kết quả mẫu giống nhau giữa các seed. Notebook còn kiểm tra độc lập route bằng cách liệt kê các hoán vị phần tail cho bài 3 và 6 thành phố; đây là kiểm chứng nhỏ cho công thức chi phí, không phải solver thứ ba dùng trong ứng dụng. Khi số thành phố tăng, khoảng cách giữa các lần chạy cũng tăng rõ ở một số dataset. Tỷ lệ đạt min quan sát chỉ cho biết số run chạm vào kết quả tốt nhất của chính mẫu hiện tại, không thể diễn giải là xác suất tìm optimum toàn cục.

## 3.4. Khởi tạo, adaptive mutation và 2-opt

Trong thí nghiệm đã ghi cho các bài 15, 26, 42 và 48 thành phố, cấu hình mixed initialization và nearest-neighbor cho kết quả trung bình thấp hơn control trên các mẫu đó. Chẳng hạn tại 48 thành phố, control đạt mean 55.404,6, trong khi mixed đạt 37.222,2 và nearest-neighbor đạt 36.559,0. Đây là bằng chứng thực nghiệm có phạm vi hẹp, không phải bảo đảm hai phương pháp khởi tạo này sẽ tốt hơn trên dữ liệu khác.

2-opt cho kết quả trung bình kém control ở cả bốn bài trong preset được ghi nhận. Trên bài 48 thành phố, 2-opt tiêu thụ trung bình 3.163,4 trên 4.000 lượt đánh giá cho các phép thử local search và chỉ commit khoảng 20,6 thế hệ, trong khi control commit khoảng 104 thế hệ. Điều này giải thích một đánh đổi quan trọng: các probe local search cũng dùng ngân sách objective, nên chúng làm giảm lượt tạo thế hệ mới. Không nên kết luận 2-opt tốt hơn chỉ vì từng move được chấp nhận là move cải thiện route hiện tại.

Adaptive mutation được triển khai như lựa chọn cấu hình, nhưng các kết quả trong notebook chỉ là quan sát theo seed, preset và evaluation budget đã chỉ định. Tùy chọn này không bật mặc định. GA vẫn giữ cấu hình mặc định random initialization, tournament selection, OX, inversion mutation và elitism hai cá thể để có baseline dễ so sánh.

## 3.5. Benchmark trên bảy ma trận

> Bảng dưới đây là số liệu thực nghiệm đã được ghi trong `docs/experiments.md` từ một batch benchmark 35 lần chạy. Nó không phải số đo vừa được chạy lại trong lần kiểm tra tài liệu này. Mỗi lần chạy dùng 6.000 evaluations và năm seed; thời gian là runtime trung bình mỗi lần chạy trên môi trường được ghi trong tài liệu nghiệm thu trước.

| Số thành phố | Distance trung bình | Độ lệch chuẩn mẫu | Runtime trung bình (giây) |
|---:|---:|---:|---:|
| 3 | 6 | 0 | 0.043994 |
| 4 | 189 | 0 | 0.047088 |
| 6 | 1248 | 0 | 0.050767 |
| 15 | 1200.2 | 13.86 | 0.064215 |
| 26 | 1056.4 | 72.84 | 0.081771 |
| 42 | 1166.2 | 26.28 | 0.101169 |
| 48 | 54194.4 | 3861.50 | 0.115391 |

Các ma trận có thang chi phí khác nhau, vì vậy không được so sánh trực tiếp mean distance của dataset này với dataset khác như thể chúng có cùng đơn vị hoặc cùng độ khó. Dữ liệu hiện chưa có known optimum được xác minh trong registry, nên relative gap để trống và không thể kết luận khoảng cách tới nghiệm tối ưu cho các bài lớn.

## 3.6. Kiểm tra source và smoke test ở lần rà soát hiện tại

Các kết quả dưới đây được chạy trực tiếp trên working tree hiện tại bằng interpreter `.venv` của repository. Trong terminal Windows của phiên kiểm tra, Python dùng encoding `cp1258`, khiến ký tự tiếng Việt và mũi tên trong output CLI không ghi được. Sau khi đặt `PYTHONIOENCODING=utf-8`, các lệnh chạy thành công. Đây là vấn đề encoding của console ở môi trường cụ thể; nó không làm thay đổi objective hay kết quả solver, nhưng người dùng Windows có thể cần đặt UTF-8 nếu gặp lỗi tương tự.

- `python -m compileall -q src`: pass.
- `python -m ga_eho_tsp.cli validate` cho cả bảy file: pass; các ma trận đều được xác nhận vuông, đối xứng, diagonal 0 và finite.
- Chạy `solve` trên `15Cities-1194.txt` với seed 42, population 20, 10 generations và 10 max iterations: distance 1687, 200 evaluations, 10 iterations, stopping reason `MAX_ITERATIONS`; elapsed được lệnh CLI ghi là 0.002457 giây trong lần chạy này.
- Gọi API solver hai lần cùng cấu hình trên: route, distance, evaluation count và dãy best-so-far bằng nhau; kiểm tra lại route length bằng shared objective cũng pass.
- Gọi CLI với `--algorithm eho`: bị từ chối với thông báo “EHO planned / not implemented”, exit code 2. Điều này xác nhận CLI không giả lập kết quả EHO.
- `python -m pytest -q`: không có test nào được tìm thấy trong repository hiện tại (`no tests ran`). Vì thế không thể báo cáo regression suite pytest pass trong working tree này.

Smoke test 15 thành phố dùng cấu hình nhỏ để xác minh luồng chạy, không phải benchmark chất lượng. Distance 1687 không được coi là optimum; đây là kết quả của seed và cấu hình nhỏ vừa chạy. Các bảng ở phần trước là số liệu từ báo cáo thực nghiệm đã có sẵn, được dẫn nguồn rõ ràng thay vì giả vờ chạy lại ở đây.

# CHƯƠNG 4. KẾT LUẬN

## 4.1. Kết quả đạt được

Source hiện tại có một GA solver thật cho symmetric TSP. GA dùng route permutation 0-based khóa city 0, shared objective, RNG riêng theo seed, global-best tracking, history, evaluation count và các điều kiện dừng có thể cấu hình. Pipeline mặc định gồm random initialization, tournament selection, OX crossover, inversion mutation và elitism. Các hàm operator được chia module để có thể đọc và thay đổi độc lập.

Ngoài cấu hình mặc định, source đã triển khai rank và roulette selection, PMX, swap/insertion/scramble mutation, nearest-neighbor/mixed initialization, stagnation stopping, adaptive mutation, cancellation/progress callback và bounded 2-opt. CLI có validate, solve GA và benchmark nhiều seed; GUI cũng đăng ký solver GA hiện có. Cả bảy ma trận bundled đã qua lệnh validate trong lần kiểm tra này.

Về phạm vi người dùng hỏi, có thể xác nhận **phần thuật toán GA cho TSP đã được triển khai ở source**, còn **EHO chưa được triển khai**. Tuy nhiên, không nên diễn đạt thành “toàn bộ repository đã qua nghiệm thu tự động”: working tree hiện không chứa regression test suite, và `pytest -q` không chạy được test nào. Tài liệu hiện có ghi lại các lần kiểm thử trước đó nhưng bằng chứng lịch sử không thay thế được việc có thể chạy lại bộ test trong repo.

## 4.2. Hạn chế và hướng phát triển

1. **Khôi phục regression suite thường trực.** Ưu tiên cao nhất là đưa lại tests vào repository để các thay đổi sau này có thể được kiểm tra bằng `pytest -q`. Không nên dựa riêng vào các số liệu test lịch sử đã lưu trong tài liệu.
2. **Kiểm tra encoding CLI trên Windows.** Trong môi trường terminal của lần rà soát này, CLI cần UTF-8 output encoding mới hiển thị thông điệp tiếng Việt và ký tự mũi tên. Cần quyết định có nên làm CLI tự cấu hình encoding hay chỉ chuẩn hóa hướng dẫn chạy.
3. **Mở rộng thực nghiệm có kiểm soát.** Tăng số seed, báo cáo phân bố, tách rõ fixed-generation với fixed-evaluation comparisons và chỉ dùng optimum/gap khi có nguồn xác minh.
4. **Xác minh nguồn dữ liệu và giấy phép.** Dataset hiện có nguồn gốc tham chiếu trong tài liệu attribution, nhưng giấy phép và optimum cho các ma trận vẫn chưa xác nhận đầy đủ.
5. **Chưa có TSPLIB loader, restart hoặc 2-opt delta engine.** Đây là các chức năng chưa nằm trong implementation hiện tại; không được mô tả như đã hoàn thành.
6. **EHO là phần việc kế tiếp của nhóm.** Solver EHO không có trong repository hiện tại. Việc triển khai cần tuân thủ shared contract, dùng cùng TSP objective và được kiểm tra độc lập; phần GA này không cung cấp kết quả EHO giả.

Do số lần chạy và số seed trong các thí nghiệm còn hạn chế, kết quả không chứng minh GA luôn tìm nghiệm tối ưu hoặc một operator luôn tốt hơn các operator còn lại. Kết luận phù hợp nhất là repository hiện có một GA solver triển khai được và tái lập được trong các smoke test đã chạy; mức tin cậy lâu dài còn phụ thuộc vào việc khôi phục bộ test tự động và mở rộng kiểm chứng.

# TÀI LIỆU THAM KHẢO

1. Holland, J. H. *Adaptation in Natural and Artificial Systems*. University of Michigan Press, 1975. Tài liệu nền tảng về cơ chế thích nghi và giải thuật di truyền.
2. Goldberg, D. E. *Genetic Algorithms in Search, Optimization, and Machine Learning*. Addison-Wesley, 1989. Tài liệu nhập môn về biểu diễn, selection, crossover và mutation trong GA.
3. Applegate, D. L., Bixby, R. E., Chvátal, V., và Cook, W. J. *The Traveling Salesman Problem: A Computational Study*. Princeton University Press, 2006. Tài liệu chuyên sâu về mô hình và phương pháp giải TSP.
4. Slowik, A. (Ed.). *Swarm Intelligence Algorithms: A Tutorial*. CRC Press, 2020. Tài liệu seminar được liệt kê trong README của repository; nội dung GA ở đây không dùng nó để khẳng định đã triển khai EHO.
5. Nhóm dự án, `docs/algorithm_ga.md`, `docs/experiments.md`, `docs/architecture.md`, `docs/source_attribution.md` và source trong `src/ga_eho_tsp/`. Các tài liệu này mô tả implementation, kết quả đã ghi nhận, hợp đồng dữ liệu và giới hạn hiện tại của repository.
6. File `AI FINAL PROJECT.pdf` do người dùng cung cấp. Tài liệu được dùng làm khung chương mục; mục lục/nội dung PDF còn ghi Tic Tac Toe và không phải mô tả implementation hiện tại của repository.

# PHỤ LỤC A. CÀI ĐẶT VÀ SỬ DỤNG GA

## A.1. Cài môi trường

Từ thư mục gốc repository, sử dụng Python 3.11 trở lên:

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Nếu PowerShell chặn activate script, có thể gọi trực tiếp `.\.venv\Scripts\python.exe` thay cho `python`. Trên terminal Windows gặp lỗi không in được tiếng Việt hoặc mũi tên, thử đặt encoding cho phiên terminal:

```powershell
$env:PYTHONIOENCODING = "utf-8"
```

## A.2. Kiểm tra dataset

```powershell
python -m ga_eho_tsp.cli validate --dataset data/06Cities-1248.txt
```

Thông báo thành công cho biết tên bài toán, dimension, tính đối xứng, đường chéo 0 và tính hữu hạn. Nếu file sai định dạng hoặc ma trận không hợp lệ, CLI trả lỗi thay vì tự sửa dữ liệu.

## A.3. Chạy GA

```powershell
python -m ga_eho_tsp.cli solve `
  --algorithm ga `
  --dataset data/15Cities-1194.txt `
  --seed 42
```

CLI in thuật toán, distance, tour đóng vòng, seed, số iteration, evaluations, runtime và stopping reason. Với cấu hình mặc định, population là 80, generations/max iterations là 250, tournament size là 3, crossover là OX với rate 0.9, mutation là inversion với rate 0.15 và elitism giữ 2 cá thể. Có thể cung cấp thêm flags để chọn selection/crossover/mutation khác, initialization, evaluation/time budget, stagnation, adaptive mutation hoặc 2-opt. Các giá trị được kiểm tra qua `GAConfig`.

Ví dụ chọn PMX và mixed initialization, giới hạn 6.000 evaluations:

```powershell
python -m ga_eho_tsp.cli solve `
  --algorithm ga `
  --dataset data/48Cities-33523.txt `
  --seed 42 `
  --crossover-method pmx `
  --initialization-method mixed `
  --max-evaluations 6000 `
  --json outputs/ga-pmx.json
```

JSON lưu route lõi 0-based chưa lặp city 0 ở cuối. Giá trị distance đã gồm cạnh quay từ thành phố cuối về thành phố xuất phát.

## A.4. Chạy benchmark và kiểm tra lại

```powershell
python -m ga_eho_tsp.cli benchmark --config examples/ga_benchmark.json
```

Config ví dụ chạy bảy ma trận với năm seed và tối đa 6.000 evaluations mỗi run. Summary, CSV và JSON được ghi vào `outputs/benchmarks/ga-example/`. Dữ liệu output có thể được thay thế khi chạy lại cùng cấu hình; cần đổi `output_dir` nếu muốn giữ các batch khác nhau.

Repository hiện không có regression suite `tests/`. Do đó, lệnh dưới đây trong working tree hiện tại sẽ báo không có test chạy được cho tới khi suite được khôi phục:

```powershell
python -m pytest -q
```

Các kiểm tra thực hiện trong lần rà soát hiện tại được nêu ở Mục 3.6, còn số liệu benchmark có sẵn được mô tả ở Mục 3.5. Hai nhóm bằng chứng này không được đánh đồng.
