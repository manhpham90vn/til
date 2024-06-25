# EC2

- [docs](https://docs.aws.amazon.com/ec2/?icmpid=docs_homepage_featuredsvcs)
- Action
  - Attach/Detach Volume
  - Attach/Detach IP
  - Attach/Detach Security Group
  - Attach/Detach IAM Role
  - Create snapshot from Volume
  - Create AMI from EC2 Instance
- Life Cycle of EC2
- Life Cycle of EC2 with instance-store volume: IOPS cao dùng để cache dữ liệu

## AMI: Amazon Machin Image

- là một bản sao của EC2 bao gồm một hệ điều hành, các ứng dụng dùng để triển khai EC2 instane mới
- có thể tạo 1 custom AMI từ EC2 instance, khi tạo 1 custom AMI thì sẽ tự động tạo 1 Snapshots
- có thể lauch ec2 instance từ 1 custom AMI vừa tạo ở trên

## EBS Volume

- Ổ cứng ảo được cấp phát bởi AWS, có thể đọc được dữ liệu khi gắn vào 1 instance
- Có thể gắn với một hoặc nhiều EC2
- Có thể tăng size volume kể cả khi server đang chạy và không làm mất data
- Không thể giảm size volume
- Volume chỉ có thể gắn vào EC2 instance có cùng Availability Zone
- Gồm 4 loại chính
  - General Purpose SSD: cung cấp dung lượng lưu trữ tiết kiệm chi phí
  - Provisioned IOPS SSD: được thiết kế để đáp ứng nhu cầu khối lượng công việc đòi hỏi nhiều I/O
  - Throughput Optimized HDD: cung cấp khả năng lưu trữ với chi phí thấp, phù hợp khối lượng công việc lớn và tuần tự
  - Cold HDD: chi phí thấp, yêu cầu truy cập không thường xuyên
  - Magnetic: phù hợp dữ liệu truy cập không thường xuyên

## Snapshot

- ảnh chụp của 1 EBS Volume tại 1 thời điểm, dùng để khôi phục dữ liệu khi có sự cố
- từ snapshot có thể tạo một volume rồi gắn vào ec2 hoặc tạo 1 AMI rồi launch ec2 instance mới

## Security Group

- hoạt động như một tường lửa ảo của instance để kiểm soát lưu lượng truy cập in, out
- là stateful, chỉ cần chỉ định inbound rules, không cần chỉ định outbound rules
- thường để outbound rules là allows all

## Subnets

- là một mạng con trong VPC, mỗi subnet có một dải địa chỉ IP riêng
- thường được phân chia theo Availability Zone

## Elastic IPs

- thuê 1 địa chỉ IP tĩnh để gắn vào instance

## Network Interfaces

- quản lý các card mạng ảo

## Get Meta data

```shell
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/local-ipv4
curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/public-ipv4
```

## Pricing Model

### On-Demand

- dùng bao nhiều trả bấy nhiêu, không cần trả trước

### Spot Requests

- đấu giá để sử dụng instance vào lúc thấp điểm

### Savings Plans

- cam kết sử dụng ở 1 ngưỡng nào đó để được hưởng giảm giá

### Reserved Instances

- mua trước 1,2,3 năm để được hưởng ưu đãi

### Dedicated Hosts

- thuê phần cứng của AWS
