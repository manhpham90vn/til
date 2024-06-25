# Auto Scaling Groups

- <https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html>
- Tự động điều chỉnh resource để đáp ứng nhu cầu workload
- Có 2 hình thức là
  - Scale Up/Down: tăng/giảm cấu hình của resource
  - Scale Out/In tăng/giảm số lượng thành phần trong 1 cụm chức năng

## Launch Template

- Cấu hình các thông số để thực hiện scaling

## Auto Scaling Method

- No Scaling: Duy trì số lượng instance cố định, nếu instance die thì tạo instance mới bổ sung ngoài ra không làm gì cả
- Manually Scaling: Điều chỉnh min/max/desire để quyết định số lượng instance
- Dynamic Scaling: Điều chỉnh tự động dựa trên việc moniotor các thông số

## Sticky sessions

- là tính năng sẽ để forward request vào đúng 1 server, dựa vào cookie để xử lý
- cần cấu hình tại ELB và AG
