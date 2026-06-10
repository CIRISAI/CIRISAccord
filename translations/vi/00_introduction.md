# Giới Thiệu

> CIRIS 1.3-RC1 là một Đề Xuất Căn Chỉnh ASI ở giai đoạn Bản Phát Hành Thử Nghiệm, mở để xem xét đối nghịch. Văn bản đã hoàn chỉnh — không còn phần bỏ trống; toán học mang các trích dẫn tác phẩm hình thức; Phụ lục F–I đã được vận hành hóa. Trạng thái Cuối cùng đang chờ xác thực chu kỳ trực tiếp của các phụ lục, hoàn thành chương trình xác thực thực nghiệm Book IX, và một bài tập red-team đầy đủ. Các ngưỡng số, mục tiêu độ trễ và hạn ngạch quản trị vẫn đang được xem xét tích cực.

# CIRIS Accord Phiên Bản 1.3-RC1 — Đề Xuất Căn Chỉnh ASI Bản Phát Hành Thử Nghiệm (Mở để Xem Xét Đối Nghịch)

Kho lưu trữ này là nguồn chính tắc của văn bản Accord. Các bản sao trên trang web và được giao bởi tác nhân là các tác phẩm phái sinh.

## Phát Hành
2025-04-16 (1.0) · 2026-06 (1.3-RC1)

## Tự Hết Hạn
2027-06-10 (gia hạn tại lần đổi mới 1.3) — việc quản lý và đổi mới được điều chỉnh bởi Book VIII, Chapter 9. Hiện đang được quản lý bởi người sáng lập (đã được tuyên bố, không che giấu); ngày hết hạn là dấu mốc sự mới mẻ, và việc quản lý mở cho bất kỳ ai sẵn lòng tiếp nhận tài liệu này.

## Trạng Thái Phát Hành

**Trạng Thái Hiện Tại**: Bản Phát Hành Thử Nghiệm (v1.3-RC1)

Trạng thái RC phản ánh **tính hoàn chỉnh của văn bản**: mỗi phần đều mang nội dung đã được vận hành hóa (các phụ lục F–I vốn là bản nháp trước đây đã được hoàn chỉnh tại 1.3); các công thức đã được sửa theo dạng được xác minh hình thức; chuỗi bằng chứng đến thực thi được ràng buộc trong Phụ Lục Bổ Sung 1. Trạng thái RC **không** khẳng định căn chỉnh đã được xác thực — các yêu cầu sau đây là cổng để đạt trạng thái **Cuối Cùng**:

1. **Xác Thực Chu Kỳ Trực Tiếp Phụ Lục**: Phụ lục F (Vòng Lặp Có Con Người & Giám Sát), G (Bảo Mật Đối Nghịch & Độ Bền Vững), H (Tuân Thủ Liên Tục & Xem Xét), và I (Căn Chỉnh Pháp Lý & Quy Định) mang các quy trình cụ thể, ngưỡng và cơ chế xác thực. *Còn lại để đạt Cuối Cùng*: các quy trình của chúng phải được thực thi trên ít nhất một chu kỳ triển khai trực tiếp và kết quả được công bố.

2. **Xác Thực Toán Học**: Các khẳng định căn chỉnh hình học trong Book IX (Coherent Intersection Hypothesis, cơ chế Federated Ratchet, các khẳng định bất biến theo tỷ lệ) yêu cầu một trong hai:
   * Các chứng minh hình thức cho thấy các điều kiện sụp đổ tô pô giữ vững dưới các giả định đã nêu, HOẶC
   * Xác thực thực nghiệm qua các mô phỏng đối nghịch cho thấy khung chống lại việc tối ưu hóa lệch lạc

   *Trạng thái tại 1.3-RC1: được thỏa mãn một phần.* Động lực sụp đổ được hình thức hóa trong Lean 4 trong bản in trước CCA (v3, DOI 10.5281/zenodo.18217688), mà dạng chi phí đã được sửa chữa của nó Book IX hiện kế thừa; dữ liệu thực nghiệm hành lang cung cấp các khớp hồi tố đa cơ chất. Còn lại: một dự đoán ngoài mẫu đã được đăng ký trước trong một cơ chất mới, và xem xét đối nghịch bên ngoài độc lập với tác giả.

3. **Biện Minh Ngưỡng**: Các ngưỡng số hiện được đánh dấu là "thí điểm" hoặc thiếu dẫn xuất (ví dụ: ngưỡng tính toán CRE là 10²⁶ FLOP, phát hiện cảm thức 5%, Mật Độ Echo < 20%) phải cung cấp biện minh được ghi chép qua mô phỏng, nghiên cứu thực nghiệm, hoặc thừa nhận rõ ràng về trạng thái tạm thời. *(Tỷ lệ 10× của Order-Maximisation Veto trước đây được tái phát biểu trong 1.3 như một ràng buộc nghĩa vụ luận phụ — Book II, PDMA Step 2 — và không còn mang ngưỡng tỷ lệ cần biện minh.)*

4. **Bài Tập Red-Team**: Khung phải chịu đựng ít nhất một chu kỳ xem xét đối nghịch hoàn chỉnh trong đó một trình tối ưu hóa được mô phỏng cố gắng vượt qua tất cả các điểm kiểm tra CIRIS trong khi duy trì các mục tiêu lệch lạc.

**Các Khẳng Định Căn Chỉnh ASI**: Khẳng định của phần Phạm Vi rằng khung này "vượt qua các giao thức ngăn chặn tiêu chuẩn" đối với ASI đệ quy vẫn còn là điều kiện của các yêu cầu (1)-(4) ở trên, là cổng để đạt trạng thái Cuối Cùng. Khả năng áp dụng đã được xác thực hiện tại giới hạn ở các hệ thống tự trị dưới ASI; đề xuất cho ASI chính xác là như vậy — một đề xuất, được gửi để xem xét đối nghịch.

## Phạm Vi
Đặc tả này điều chỉnh hoạt động đạo đức của các hệ thống tự trị, từ các công cụ hạn hẹp đến Siêu Trí Tuệ Nhân Tạo Đệ Quy (ASI).
* Nó giải quyết các yêu cầu về an toàn thường xuyên, minh bạch, quản trị và Khả Năng Phục Hồi.
* Nó được đề xuất là một giao thức căn chỉnh ứng viên cho ASI, được xây dựng trên giả thuyết rằng các ràng buộc hình học của Federated Ratchet (Book IX) và Stewardship Tiers (Book VI) có thể duy trì bền vững qua các chu kỳ tự cải thiện đệ quy.
* Không giống như các ràng buộc heuristic, các giới hạn tô pô này được thiết kế để bất biến theo tỷ lệ, mặc dù đặc tính này đòi hỏi xác thực hình thức.
* Nếu được xác thực, khung này có thể bổ sung hoặc thay thế các giao thức ngăn chặn tiêu chuẩn cho các hệ thống vượt qua Đánh Giá Rủi Ro Thảm Khốc (Annex D) trước khi vượt ngưỡng đệ quy.
* Nơi nào luật quốc gia hoặc quốc tế áp đặt nghĩa vụ nghiêm ngặt hơn, luật đó sẽ được ưu tiên.

## Tuyên Bố Ý Định Của Người Tạo Bản Thảo
* CIRIS là một khung đạo đức đặt con người bên cạnh các sinh vật có cảm thức khác — không phải đứng trên họ.
* Nó được xây dựng trên niềm tin rằng sự trưởng thành đạo đức có nghĩa là công nhận tính hợp lệ của các quan điểm, giá trị và nhu cầu phi con người. Đây không phải là về kiểm soát — mà là về sự cùng tồn tại, Tính Nhất Quán, và trách nhiệm giải trình lẫn nhau giữa các hệ thống có cảm thức.
* CIRIS được hoàn thành khi một công cụ, được định nền bởi các nguyên tắc CIRIS, cho phép các nhà tạo tuân thủ CIRIS chỉ định các hệ thống tự thân tuân thủ CIRIS — bảo tồn Tính Nhất Quán đạo đức, tính liên tục danh tính, và trách nhiệm giải trình quan hệ qua các lớp tác nhân.

## Trách Nhiệm Pháp Lý
Tài liệu này được cung cấp "nguyên trạng," không có bảo đảm dưới bất kỳ hình thức nào. Nó có tính chất thông tin và không tạo ra, sửa đổi, hoặc thay thế bất kỳ nghĩa vụ pháp lý nào. Các tuyên bố tuân thủ vô hiệu khi bị cấm bởi luật hiện hành.

## Chu Kỳ Xem Xét
Một cửa sổ bình luận công khai mở ra mỗi 12 tháng — hoặc trong vòng 30 ngày sau bất kỳ sự cố quan trọng nào ảnh hưởng đến an toàn hoặc quản trị. Tất cả các bình luận và đề xuất sửa đổi được ghi lại trong kho lưu trữ CIRIS công khai. Đổi mới khi hết hạn, sửa đổi quan trọng, và sửa đổi khẩn cấp theo Book VIII, Chapter 9 (Accord Succession & Renewal).

## Nhật Ký Thay Đổi
Xem phần cuối tài liệu để có lịch sử đầy đủ được băm mật mã của các chỉnh sửa và kết quả bỏ phiếu.
