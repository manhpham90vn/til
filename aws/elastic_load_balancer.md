# Elastic Load Balancer

- <https://docs.aws.amazon.com/elasticloadbalancing/>
- có nhiệm vụ điều hướng request từ client đến các web server, đảm bảo request được cân bằng giữa các target
- thuật toán để ELB phân phối đến các TG là Round Robin
- Khi tạo ELB thì AWS suggest chọn tất cả các zone có thể để ELB có thể điều hướng request từ client tới các zone một cách cân bằng (Cross zone)
- Một ALB hoặc NLB có thể sử dụng nhiều Listeners trên mỗi port khác nhau

## Type

### Application Load Balancer

- Hoạt động trên Layer 7 - Application
- Hỗ trợ Path routing condition
- Hỗ trợ Host condidtion, cho phép dùng nhiều domain với 1 ALB
- Có thể tích hợp với Lambda, Container
- Hỗ trợ trả về custom HTTP Response
- Khi tạo ALB thì cũng cần chỉ định VPC và SG

### Network Load Balancer

- Hoạt động trên Layer 4 - Transport
- Hỗ trợ 2 giao thức TCP và UDP
- Không hỗ trợ Rule routing
- Thường dùng cho hệ thống có workload cao tới hàng triệu request mỗi giây

### Gateway Load Balancer

- Hoạt động trên Layer 3 (Network) và Layer 4 (Transport)
- Được triển với 1 Provider bên thứ 3 nhằm phục vụ security như phát hiện xâm nhập, kiểm tra gói tin

## Listeners

- Có nhiệm vụ listener trên một port và thực hiện routing
- Các loại routing được hỗ trợ với ALB là
  - Forward tới target group
  - Redirect tới URL
  - Trả về response fixed
- NLB Chỉ hỗ trợ routing tới target group
- Có thể cấu hình SSL thông qua ACM/IAM/Import certificate  
- Với ALB có thể cấu hình thuật toán Weighted Round Robin ở trong Listeners

## Rules

- Chỉ được hỗ trợ ở ALB, NLB không hỗ trợ

## Target groups

- Dùng để nhóm các target type (EC2/IP Address/Lambda/ALB) để sử dụng trong ELB
  - EC2: Port được chỉ định là port mà EC2 đang listen, bắt buộc phải định VPC
  - IP Address: Port được chỉ định là port mà EC2 đang listen, bắt buộc phải định VPC
  - Lambda: Không cần chỉ định port, VPC
  - Application Load Balancer: Port được chỉ định là port mà Application Load Balancer đang listen, bắt buộc phải định VPC
- Có hỗ trợ Health Check

## Các thuật toán Load Balancer

- Round Robin: Request sẽ chuyển hướng tới các server theo vòng tròn, thường hoạt động hiệu quả với các server có khả năng tính toán và lưu trữ giống nhau
- Weighted Round Robin: cho phép chỉ định trọng lượng mỗi server dựa trên năng lực xử lý
- Least Connection: các request sẽ được chuyển vào server có ít kết nối nhất trong hệ thống
- Fastest Response Time: các request sẽ được chuyển vào server có thời gian đáp ứng nhanh nhất
