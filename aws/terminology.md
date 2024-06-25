# Terminology

## Region

- là một khu vực vật lý trên thế giới chứa một hoặc nhiều trung tâm dữ liệu của AWS

## Availability Zone

- là một trong các khu vực tách biệt thuộc về  Region. Mỗi Region sẽ có nhiều Availability Zone
- khi thiết kế hệ thống thường nên kết hợp tối thiểu 2 Availability Zone để đảm bảo tính High Availability

## Local Zone

- là phần mở rộng của Region có khoảng cách địa lý gần với người dùng theo từng quốc gia để nhầm mục đích giảm độ trễ

## Edge Location

- là một mạng lưới các điểm phân phối trên thế giới nơi các dịch vụ AWS (Cloudfront, Route 53) cung cấp khả năng xử lý và phân phối nội dung (CDN) tới người dùng cuối
- Edge location thường hoạt động như một bộ đệm cho nội dung được phân phối bởi các dịch vụ AWS nhằm giảm độ trễ và tăng tối truy cập cho người dùng cuối

## High Availability

- là khả năng của hệ thống hoặc dịch vụ luôn trong tình trạng sẵn sàng phục vụ, giảm thiểu khả năng gián đoạn

## CDN

- là một mạng lưới máy chủ được liên kết giúp tăng tốc độ tải trang web
- dữ liệu được lưu trên CDN có sẽ vị trí gần với vị trí của người dùng để giảm độ trễ

## Pricing Model

- là một phương thức để định giá sản phẩm hoặc dịch vụ
