# IAM

- [docs](https://docs.aws.amazon.com/iam/)

## Policy

- Quy định ai/cái gì có thể hoặc không thể làm gì
- Policy bao gồm Statement quy đinh Allow/Deny hành động tới resource dựa trên condition
- Mỗi Statement cần định nghĩa các thông tin
  - Effect: Allow | Deny (Deny có độ ưu tiên cao hơn)
  - Action: Danh sách các action cho phép thực thi
  - Resource: Các resource cho phép tương tác tới
  - Condition: Điều kiện để thực thi Statement
- Mỗi Policy có thể gắn vào Role/Group/User
- Gồm 2 loại là
  - Inline Policy: đính trực tiếp lên Role/User/Group và không thể tái sử dụng trêm Role/User/Group khác
  - Managed Policy: được định nghĩa riêng và có thể tái sử dụng, gồm 2 loại là
    - AWS Managed
    - User Managed
- Sample

Policy dưới cho phép thực hiện 2 Action là Start và Stop trên tất cả EC2 Instance với điều kiện có thẻ Tag có tên ENV là Dev

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": ["ec2:StartInstances", "ec2:StopInstances"],
      "Resource": "arn:aws:ec2:*:*:instance/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/ENV": "Dev"
        }
      }
    }
  ]
}
```

## Resource Policy

- S3, SQS hỗ trợ định nghĩa policy ở cấp độ resource
- Quyền của user/group/role đối với resource là sự kết hợp IAM Policy và Resource Policy

## User

- Đại diện cho 1 profile của người dùng
- Có thể login vào AWS Console

## Role

- Đại diện cho 1 quyền trên AWS
- Dùng để cấp quyền cho một thực thể có thể tương tác với các Resource khác trên AWS
- Thường được dùng để gắn vào EC2, Lambda, Container
- Example: Tạo IAM Role cho EC2 access tới S3 (Nên sử dụng thay cho việc cấu hình Access Key để bảo mật hơn)

## Group

- Đại diện cho một nhóm user

## Permissions

## Assume Role

- cung cấp quyền để access resouce mà thông thường ta không có quyền một cách tạm thời
