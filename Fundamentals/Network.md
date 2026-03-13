# Network Protocols

> Tổng hợp kiến thức về các giao thức mạng - từ cơ bản đến nâng cao

---

## Mô hình OSI & TCP/IP

```
┌─────────────────────────────────────────────────────────────────────┐
│                        OSI Model                                    │
├───────────┬───────────┬───────────┬───────────┬─────────────────────┤
│  Layer 7 │  Layer 6  │  Layer 5  │  Layer 4  │    Application      │
│ Application│Presentation│  Session  │           │    (HTTP, DNS,     │
│           │           │           │           │   SMTP, WebSocket)  │
├───────────┴───────────┴───────────┴───────────┴─────────────────────┤
│                         Transport                                   │
│                      (TCP, UDP, QUIC)                               │
├─────────────────────────────────────────────────────────────────────┤
│                         Internet                                    │
│                       (IP, ICMP, ARP)                               │
├─────────────────────────────────────────────────────────────────────┤
│                      Network Interface                              │
│                  (Ethernet, WiFi, MAC)                             │
└─────────────────────────────────────────────────────────────────────┘
```

---

# Phần 1: Network Interface Layer (Layer 1-2)

## 1.1 Ethernet

### Giới thiệu
- **Layer**: Layer 1 (Physical) + Layer 2 (Data Link)
- **Standard**: IEEE 802.3
- **MAC Address**: 48-bit hardware address

### Frame structure
```
┌──────────┬──────────┬──────────┬────────────┬──────────┬──────────┐
│  Preamble│   SFD   │ Dest MAC │  Source MAC│  Type/  │  Data   │
│  (7 bytes)│ (1 byte)│ (6 bytes)│  (6 bytes) │  Length │(46-1500)│
└──────────┴──────────┴──────────┴────────────┴──────────┴──────────┘
       │                    │                   │
       ▼                    ▼                   ▼
   10101010...         AA:BB:CC:DD:EE:FF     0x0800 (IPv4)
```

### VLAN (Virtual LAN)
- Chia network thành các segment logic
- Tag: 802.1Q (4 bytes)
- VLAN ID: 0-4095

---

## 1.2 Wi-Fi (IEEE 802.11)

### Standards
| Standard | Frequency | Max Speed |
|----------|-----------|-----------|
| 802.11b | 2.4 GHz | 11 Mbps |
| 802.11g | 2.4 GHz | 54 Mbps |
| 802.11n | 2.4/5 GHz | 600 Mbps |
| 802.11ac | 5 GHz | 3.4 Gbps |
| 802.11ax (Wi-Fi 6) | 2.4/5/6 GHz | 9.6 Gbps |

### Security
| Protocol | Security | Notes |
|----------|----------|-------|
| WEP | Yếu | Không nên dùng |
| WPA | Tốt hơn WEP | Cũ |
| WPA2 | Tốt | Phổ biến nhất |
| WPA3 | Tốt nhất | Mới nhất |

---

## 1.3 ARP (Address Resolution Protocol)

### Giới thiệu
- **Purpose**: Map IP address → MAC address
- **Layer**: Layer 2 (Data Link)

### How it works
```
1. Host A muốn gửi đến IP B (cùng network)
2. A check ARP cache - không có
3. A broadcast ARP request: "Who has IP B?"
4. B respond: "I am, here's my MAC"
5. A cache kết quả, gửi data
```

### ARP Table
```bash
# Xem ARP table
arp -a

# Thêm entry tĩnh
arp -s 192.168.1.1 aa:bb:cc:dd:ee:ff
```

---

# Phần 2: Internet Layer (Layer 3)

## 2.1 IPv4

### Cấu trúc
- **Address**: 32-bit (4 octets)
- **Format**: xxx.xxx.xxx.xxx (0-255)
- **Examples**: 192.168.1.1, 10.0.0.1

### Private IP Ranges
| Class | Range | CIDR |
|-------|-------|------|
| A | 10.0.0.0 - 10.255.255.255 | 10.0.0.0/8 |
| B | 172.16.0.0 - 172.31.255.255 | 172.16.0.0/12 |
| C | 192.168.0.0 - 192.168.255.255 | 192.168.0.0/16 |

### Special Addresses
- **127.0.0.1**: Localhost
- **0.0.0.0**: This network
- **255.255.255.255**: Broadcast
- **169.254.0.0/16**: Link-local (APIPA)

### IPv4 Header
```
┌────────┬────────┬───────────────┬──────────────┐
│Version │  IHL  │    TOS       │   Total Len  │
│  (4)   │  (4)  │    (8)        │    (16)      │
├────────┼────────┼───────────────┼──────────────┤
│      Identification     │Flags│  Fragment    │
│         (16)            │(3)  │   Offset(13) │
├────────┴────────┴───────┴──────────────────┤
│     TTL    │  Protocol    │  Header Checksum│
│     (8)    │    (8)       │     (16)       │
├────────────┴──────────────┴─────────────────┤
│              Source IP Address (32)          │
├──────────────────────────────────────────────┤
│           Destination IP Address (32)        │
├──────────────────────────────────────────────┤
│              Options (if IHL > 5)            │
└──────────────────────────────────────────────┘
```

---

## 2.2 IPv6

### Cấu trúc
- **Address**: 128-bit (8 groups × 16-bit)
- **Format**: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx
- **Example**: 2001:0db8:85a3:0000:0000:8a2e:0370:7334

### Rút gọn
```
# Full
2001:0db8:85a3:0000:0000:8a2e:0370:7334

# Rút gọn
2001:db8:85a3::8a2e:370:7334
::1                    # Localhost
fe80::                 # Link-local
```

### Ưu điểm so với IPv4
- Không gian địa chỉ lớn hơn
- Không cần NAT
- Built-in security (IPsec)
- Auto-configuration (SLAAC)
- No fragmentation by routers
- Simplified header

---

## 2.3 ICMP (Internet Control Message Protocol)

### Giới thiệu
- **Purpose**: Error reporting, diagnostics
- **Layer**: Layer 3 (Network)
- **Tools**: ping, traceroute

### Message Types
| Type | Name | Use |
|------|------|-----|
| 0 | Echo Reply | ping response |
| 3 | Destination Unreachable | Cannot reach |
| 8 | Echo Request | ping request |
| 11 | Time Exceeded | TTL expired |

### ping example
```bash
# Basic ping
ping google.com

# Continuous ping
ping -c 4 google.com

# With timestamp
ping -D google.com
```

### traceroute
```bash
# Linux
traceroute google.com

# Windows
tracert google.com

# With specific protocol
traceroute -I google.com  # ICMP
traceroute -T google.com   # TCP SYN
```

---

## 2.4 NAT (Network Address Translation)

### Giới thiệu
- **Purpose**: Map private IP → public IP
- **Problem**: IPv4 shortage

### NAT Types
| Type | Mô tả |
|------|-------|
| Static NAT | 1-1 mapping |
| Dynamic NAT | Pool of public IPs |
| PAT (NAT Overload) | Port-based (hầu hết router dùng) |

### How PAT works
```
┌──────────────┐              ┌──────────────┐
│  Private    │   NAT       │    Public    │
│  192.168.1.2:54321  ──► 203.0.113.1:54321 │
│  192.168.1.3:54321  ──► 203.0.113.1:54322 │
└──────────────┘              └──────────────┘
```

### NAT Table
```bash
# Xem NAT table (Linux)
conntrack -L -n

# Xem NAT rules
iptables -t nat -L -n -v
```

---

## 2.5 DHCP (Dynamic Host Configuration Protocol)

### Giới thiệu
- **Purpose**: Auto-assign IP addresses
- **Port**: Server 67, Client 68
- **Transport**: UDP

### Lease Process (DORA)
```
Client ──► [DISCOVER] ──► Server (broadcast)
Client ◄── [OFFER] ◄───── Server
Client ──► [REQUEST] ───► Server (broadcast)
Client ◄── [ACK] ◄─────── Server
```

### Configuration
```bash
# Linux DHCP client
dhclient -r           # Release
dhclient             # Renew

# DHCP lease file
/var/lib/dhcp/dhclient.leases
```

---

## 2.6 Routing

### Routing Table
```bash
# Xem routing table
route -n              # Linux
netstat -rn           # Unix
route print           # Windows
```

### Default Gateway
- Router mặc định cho traffic đi ra ngoài network
- Cấu hình thủ công hoặc qua DHCP

### Static vs Dynamic Routing
| Type | Description |
|------|-------------|
| Static | Manual configuration |
| Dynamic | OSPF, RIP, BGP, EIGRP |

---

# Phần 3: Transport Layer (Layer 4)

## 3.1 TCP (Transmission Control Protocol)

### Giới thiệu
- **Connection-oriented**: Thiết lập kết nối trước
- **Reliable**: Đảm bảo dữ liệu đến đích
- **Ordered**: Thứ tự được bảo toàn

### 3-Way Handshake
```
Client                                          Server
  │                                               │
  ├─────────────── SYN (seq=x) ──────────────────►│
  │                                               │
  │◄─────────── SYN-ACK (seq=y, ack=x+1) ─────────┤
  │                                               │
  ├─────────────── ACK (ack=y+1) ───────────────►│
  │                                               │
  │              [Connection Established]          │
```

### Connection Termination (4-Way Handshake)
```
Client                                          Server
  │                                               │
  ├─────────────── FIN ──────────────────────────►│
  │◄────────────── ACK ───────────────────────────┤
  │                                               │
  │◄────────────── FIN ───────────────────────────┤
  ├─────────────── ACK ──────────────────────────►│
  │                                               │
  │              [Connection Closed]              │
```

### Features

#### Flow Control
- **Sliding Window**: Ngăn sender quá tải receiver
- **Window Size**: Số bytes chưa ACK

#### Congestion Control
| Phase | Algorithm |
|-------|-----------|
| Slow Start | Exponential increase |
| Congestion Avoidance | Linear increase |
| Fast Recovery | After packet loss |

#### TCP Flags
| Flag | Mô tả |
|------|-------|
| SYN | Synchronize (new connection) |
| ACK | Acknowledgment |
| FIN | Finish (close connection) |
| RST | Reset (abort connection) |
| PSH | Push (send immediately) |
| URG | Urgent |

### Header Structure
```
┌─────────┬─────────┬─────────────────────────────┐
│Source Pt│ Dest Pt│         Sequence Number     │
│ (16 bit)│(16 bit)│          (32 bits)          │
├─────────┴─────────┴─────────────────────────────┤
│         Acknowledgment Number     │  Data Off  │
│              (32 bits)           │  Res  Flags│
├───────────────────────────────────┴────────────┤
│           Window Size (16 bits)                │
├───────────────┬───────────────┴────────────────┤
│  Checksum     │        Urgent Pointer           │
│  (16 bits)   │           (16 bits)              │
├───────────────┴────────────────────────────────┤
│              Options (if any)                   │
└─────────────────────────────────────────────────┘
```

---

## 3.2 UDP (User Datagram Protocol)

### Giới thiệu
- **Connectionless**: Không cần thiết lập kết nối
- **Unreliable**: Không đảm bảo dữ liệu đến
- **No ordering**: Không có thứ tự

### Header Structure (8 bytes)
```
┌────────────────┬────────────────┐
│  Source Port   │  Dest Port     │
│    (16 bits)   │   (16 bits)    │
├────────────────┴────────────────┤
│    Length      │   Checksum     │
│   (16 bits)    │   (16 bits)    │
├────────────────┴────────────────┤
│         Data (optional)         │
└─────────────────────────────────┘
```

### So sánh TCP vs UDP

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Oriented | Connectionless |
| Reliability | ✅ Guaranteed | ❌ Best-effort |
| Order | ✅ Ordered | ❌ Unordered |
| Speed | Chậm hơn | Nhanh hơn |
| Header | 20-60 bytes | 8 bytes |
| Flow Control | ✅ | ❌ |
| Congestion Control | ✅ | ❌ |
| Use Cases | HTTP, Email, FTP | Video, VoIP, DNS, Gaming |

### Khi nào dùng UDP?
- Video streaming (chấp nhận mất gói nhỏ)
- VoIP / Video call
- Online gaming
- DNS queries
- DHCP
- Real-time applications

---

## 3.3 QUIC (Quick UDP Internet Connections)

### Giới thiệu
- **Base**: UDP + Reliability + Security
- **Tác giả**: Google, sau đó IETF chuẩn hóa (RFC 9000)
- **HTTP/3**: HTTP over QUIC

### Vấn đề của TCP
1. **Head-of-line blocking**: 1 packet mất → tất cả đợi
2. **Connection chậm**: Cần nhiều round-trip
3. **TLS riêng biệt**: Handshake tách rời

### Đặc điểm nổi bật

| Feature | Mô tả |
|---------|-------|
| 0-RTT | Kết nối lại gần như ngay lập tức |
| Multiplexing | Nhiều stream độc lập |
| Connection ID | Đổi IP không mất kết nối |
| Built-in TLS 1.3 | Encryption tích hợp |
| No HOL blocking | Stream không chặn nhau |

### QUIC vs TCP+TLS Handshake
```
TCP + TLS 1.3:
Client ──► SYN ─────────────────────────────►
Client ◄─ SYN-ACK + ServerHello + Cert ◄─────
Client ──► ACK + ClientKeyExchange ─────────►
Client ◄─ Finished ◄─────────────────────────
[Application Data]

QUIC:
Client ──► Initial + CH + 0-RTT Data ───────►
Client ◄─ Initial + SH + Cert + Finished ◄───
[Application Data]
```

---

## 3.4 Port Numbers

### Well-Known Ports (0-1023)
| Port | Protocol | Service |
|------|----------|---------|
| 20 | TCP | FTP Data |
| 21 | TCP | FTP Control |
| 22 | TCP/UDP | SSH |
| 23 | TCP | Telnet |
| 25 | TCP | SMTP |
| 53 | TCP/UDP | DNS |
| 67/68 | UDP | DHCP Server/Client |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 143 | TCP | IMAP |
| 443 | TCP | HTTPS |
| 465 | TCP | SMTPS |
| 587 | TCP | SMTP Submission |
| 993 | TCP | IMAPS |
| 995 | TCP | POP3S |

### Registered Ports (1024-49151)
| Port | Protocol | Service |
|------|----------|---------|
| 1433 | TCP | MSSQL |
| 1521 | TCP | Oracle |
| 3000 | TCP | Dev servers |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 5672 | TCP/UDP | AMQP |
| 6379 | TCP | Redis |
| 8080 | TCP | HTTP Alt |
| 8443 | TCP | HTTPS Alt |
| 27017 | TCP | MongoDB |

### Dynamic/Private Ports (49152-65535)
- Ephemeral ports cho client connections
- Port range có thể cấu hình

---

# Phần 4: Application Layer (Layer 5-7)

## 4.1 DNS (Domain Name System)

### Giới thiệu
- **Port**: 53
- **Transport**: UDP (thường), TCP (large responses)
- **Purpose**: Map domain → IP address

### Resolution Process
```
Client → OS Cache → Local DNS → Root → TLD → Authoritative
```

### Record Types
| Type | Purpose | Example |
|------|---------|---------|
| A | IPv4 address | example.com → 93.184.216.34 |
| AAAA | IPv6 address | example.com → 2606:2800:... |
| CNAME | Alias | www.example.com → example.com |
| MX | Mail server | example.com → mail.example.com |
| TXT | Text record | Verification, SPF, DKIM |
| NS | Name server | example.com → ns1.example.com |
| SOA | Authority | Primary NS, admin email |
| PTR | Reverse DNS | IP → domain |

### DNS Query Types
```bash
# A record
dig google.com A

# AAAA record
dig google.com AAAA

# MX record
dig google.com MX

# CNAME
dig www.google.com CNAME

# Trace full resolution
dig google.com +trace

# Reverse DNS
dig -x 8.8.8.8
```

### DNS Cache
```bash
# Xem cache (Windows)
ipconfig /displaydns

# Flush cache (Windows)
ipconfig /flushdns

# Flush cache (Linux)
sudo systemd-resolve --flush-caches

# Flush cache (macOS)
sudo dscacheutil -flushcache
```

---

## 4.2 HTTP (HyperText Transfer Protocol)

### Evolution
```
HTTP/1.1 (1997) ──► HTTP/2 (2015) ──► HTTP/3 (2022)
      │                    │                 │
      ▼                    ▼                 ▼
  Persistent          Multiplexing         QUIC
  Connection         Header Compression
                   Server Push
```

### HTTP/1.1
- **Persistent connection**: Giữ kết nối mở
- **Pipelining**: Gửi nhiều request (bị HOL blocking)
- **Chunked transfer**: Streaming

### HTTP/2
- **Multiplexing**: Nhiều request/response trên 1 kết nối
- **HPACK**: Header compression
- **Server Push**: Server chủ động gửi resource
- **Binary framing**: Text → Binary

### HTTP/3
- **QUIC transport**: Thay TCP
- **0-RTT**: Fast reconnection
- **No HOL blocking**: Stream độc lập

### Request Methods
| Method | Safe | Idempotent | Purpose |
|--------|------|------------|---------|
| GET | ✅ | ✅ | Retrieve |
| POST | ❌ | ❌ | Create |
| PUT | ❌ | ✅ | Replace |
| PATCH | ❌ | ❌ | Partial update |
| DELETE | ❌ | ✅ | Delete |
| HEAD | ✅ | ✅ | Headers only |
| OPTIONS | ✅ | ✅ | Allowed methods |

### Status Codes
| Code | Meaning |
|------|---------|
| 1xx | Informational |
| 2xx | Success |
| 3xx | Redirection |
| 4xx | Client Error |
| 5xx | Server Error |

#### Chi tiết
| Code | Description |
|------|-------------|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 301 | Moved Permanently |
| 302 | Found (Temporary) |
| 304 | Not Modified |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 429 | Too Many Requests |
| 500 | Internal Server Error |
| 502 | Bad Gateway |
| 503 | Service Unavailable |
| 504 | Gateway Timeout |

### Headers
```
# Common Request Headers
Host: example.com
Content-Type: application/json
Authorization: Bearer <token>
Accept: application/json
User-Agent: Mozilla/5.0

# Common Response Headers
Content-Type: application/json
Content-Length: 123
Cache-Control: max-age=3600
Set-Cookie: session_id=abc123
ETag: "abc123"
```

---

## 4.3 WebSocket

### Giới thiệu
- **Full-duplex**: Client ↔ Server
- **Persistent**: Giữ kết nối mở
- **Transport**: TCP

### So sánh HTTP vs WebSocket
| Feature | HTTP Polling | WebSocket |
|---------|--------------|-----------|
| Connection | Mỗi request | Persistent |
| Server Push | ❌ | ✅ |
| Overhead | Cao | Thấp |
| Use Case | REST API | Real-time |

### Connection Handshake
```
# Request
GET /ws HTTP/1.1
Host: example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Sec-WebSocket-Version: 13

# Response
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
```

### Frame Structure
```
┌────────┬────────┬─────────┬──────────┐
│Opcode  │  Mask  │  Size   │  Data    │
│ (4 bit)│ (1 bit)│ (7/16b) │  (n bit) │
└────────┴────────┴─────────┴──────────┘
```

### Use Cases
- Chat applications
- Real-time dashboards
- Live notifications
- Collaborative editing
- Online gaming

---

## 4.4 gRPC

### Giới thiệu
- **Framework**: Google RPC
- **IDL**: Protocol Buffers
- **Transport**: HTTP/2

### Đặc điểm
- **Performance**: Nhỏ, nhanh (Protobuf)
- **Code generation**: Từ .proto file
- **Streaming**: 4 loại
- **Strongly typed**: Schema ràng buộc

### .proto Example
```protobuf
syntax = "proto3";

service UserService {
  rpc GetUser (GetUserRequest) returns (User);
  rpc CreateUser (CreateUserRequest) returns (User);
  rpc StreamUsers (StreamRequest) returns (stream User);
}

message User {
  string id = 1;
  string name = 2;
  string email = 3;
}
```

### 4 Loại RPC
| Type | Pattern |
|------|---------|
| Unary | Request → Response |
| Server Streaming | Request → stream Responses |
| Client Streaming | stream Requests → Response |
| Bidirectional | stream ↔ stream |

### So sánh REST vs gRPC
| Feature | REST | gRPC |
|---------|------|------|
| Format | JSON | Protobuf |
| Transport | HTTP/1.1 | HTTP/2 |
| Streaming | ❌ | ✅ |
| Code Gen | OpenAPI | .proto |
| Browser | ✅ | grpc-web |

---

## 4.5 GraphQL

### Giới thiệu
- **Query Language**: Cho APIs
- **Facebook**: 2012, public 2015
- **Transport**: HTTP (thường)

### Operations
```graphql
# Query (Read)
query GetUser {
  user(id: "123") {
    name
    email
    posts {
      title
    }
  }
}

# Mutation (Write)
mutation CreatePost {
  createPost(title: "Hello") {
    id
    title
  }
}

# Subscription (Real-time)
subscription OnNewComment {
  newComment(postId: "123") {
    body
    author { name }
  }
}
```

### So sánh REST vs gRPC vs GraphQL
| Feature | REST | gRPC | GraphQL |
|---------|------|------|---------|
| Fetching | Fixed | Fixed | Flexible |
| Over-fetch | ✅ | ✅ | ❌ |
| Under-fetch | ✅ | ✅ | ❌ |
| Streaming | ❌ | ✅ | Sub |
| Schema | OpenAPI | .proto | SDL |

### Khi nào dùng?
| Scenario | Recommendation |
|----------|----------------|
| Mobile apps | GraphQL |
| Microservices | gRPC |
| Public API | REST |
| Real-time | WebSocket/gRPC |
| Simple CRUD | REST |

---

## 4.6 Webhook

### Giới thiệu
- **Pattern**: HTTP POST callbacks
- **Alternative**: Polling

### How it works
```
1. Register callback URL
2. Event occurs
3. Server POST to callback
4. Client processes
5. Return 200 OK
```

### Polling vs Webhook
| Feature | Polling | Webhook |
|---------|---------|---------|
| Initiation | Client | Server |
| Resource | Tốn nhiều | Hiệu quả |
| Latency | Cao | Thấp |
| Setup | Dễ | Cần endpoint |

### Security Best Practices
- Verify signature (HMAC)
- Idempotency (xử lý retry)
- Short timeout
- Exponential backoff
- SSL/TLS bắt buộc

---

## 4.7 SSE (Server-Sent Events)

### Giới thiệu
- **Server → Client**: One-way
- **Transport**: HTTP
- **Native**: EventSource API

### Example
```javascript
// Client
const source = new EventSource('/stream');
source.onmessage = (event) => {
  console.log(event.data);
};

// Server (response)
Content-Type: text/event-stream

data: {"message": "hello"}

data: {"message": "world"}
```

### So sánh WebSocket vs SSE vs Webhook
| Feature | WebSocket | SSE | Webhook |
|---------|-----------|-----|---------|
| Direction | Bi | Server→Client | Server→Client |
| Connection | Persistent | Persistent | Per event |
| Browser | ✅ | EventSource | ✅ |
| Auto-reconnect | ✅ | ✅ | ❌ |

---

## 4.8 SMTP (Email)

### Giới thiệu
- **Port**: 25, 587 (submission), 465 (SMTPS)
- **Transport**: TCP

### Email Flow
```
MUA → MTA → [Internet] → MTA → MDA → MRA → MUA
       (Send)            (Receive)
```

### SMTP Commands
```
EHLO client.example.com
AUTH LOGIN
MAIL FROM:<sender@example.com>
RCPT TO:<receiver@example.com>
DATA
Subject: Hello

Email body here.
.
QUIT
```

### Related Protocols
| Protocol | Port | Purpose |
|----------|------|---------|
| SMTP | 25/587 | Send email |
| IMAP | 143/993 | Access email |
| POP3 | 110/995 | Download email |
| DKIM | - | Email signing |
| SPF | - | Sender policy |
| DMARC | - | Email authentication |

---

## 4.9 FTP / SFTP

### FTP (File Transfer Protocol)
- **Port**: 21 (control), 20 (data)
- **Modes**: Active / Passive
- **Plain text** → Dùng FTPS

### SFTP (SSH File Transfer)
- **Thực tế**: SSH protocol
- **Port**: 22
- **Encrypted**: SSH-based

### So sánh
| Protocol | Encryption | Port | Firewall |
|----------|------------|------|----------|
| FTP | None | 21/20 | Khó |
| FTPS | TLS | 990/21 | Khó |
| SFTP | SSH | 22 | Dễ |

---

## 4.10 SSH (Secure Shell)

### Giới thiệu
- **Port**: 22
- **Purpose**: Remote access, file transfer

### Authentication
1. **Password**: Traditional
2. **SSH Key**: Public/Private
   - RSA, ECDSA, Ed25519
3. **Certificate**: Enterprise

### Commands
```bash
# Login
ssh user@host

# Copy file (SCP)
scp file.txt user@host:/path/

# Copy file (SFTP)
sftp user@host

# Tunneling
ssh -L 8080:localhost:80 user@host    # Local
ssh -R 9090:localhost:3000 user@host   # Remote
ssh -D 1080 user@host                  # SOCKS
```

---

# Phần 5: Real-time & Messaging Protocols

## 5.1 WebRTC

### Giới thiệu
- **Purpose**: P2P real-time communication
- **Transport**: UDP + SRTP
- **Use**: Video call, voice, gaming

### Components
| Component | Purpose |
|-----------|---------|
| ICE | Connection establishment |
| STUN | NAT traversal |
| TURN | Relay server |
| SDP | Session description |
| DTLS | Encryption |
| SRTP | Media encryption |

### Connection Flow
```
1. Create RTCPeerConnection
2. Create SDP offer
3. Exchange ICE candidates
4. P2P connection established
```

---

## 5.2 MQTT

### Giới thiệu
- **Pattern**: Publish/Subscribe
- **Port**: 1883 (plain), 8883 (TLS)
- **Use**: IoT, telemetry

### Architecture
```
        ┌──────┐
        │Broker│
        │(Mosq)│
        └──┬───┘
    ┌─────┼─────┐
    ▼     ▼     ▼
┌─────┐ ┌─────┐ ┌─────┐
│Sensor│ │Sensor│ │ App │
│ (Pub)│ │ (Pub)│ │(Sub)│
└─────┘ └─────┘ └─────┘
```

### QoS Levels
| Level | Guarantee | Use Case |
|-------|-----------|----------|
| 0 | At most once | Telemetry |
| 1 | At least once | Acknowledgment |
| 2 | Exactly once | Billing |

---

## 5.3 AMQP

### Giới thiệu
- **Pattern**: Message queue
- **Port**: 5672, 5671 (TLS)
- **Use**: Enterprise messaging

### Architecture
```
Producer → Exchange → Queue → Consumer
```

### Exchange Types
| Type | Routing |
|------|---------|
| Direct | Exact match |
| Topic | Wildcard |
| Fanout | All queues |
| Headers | Attribute match |

### So sánh MQTT vs AMQP
| Feature | MQTT | AMQP |
|---------|------|------|
| Simplicity | Đơn giản | Phức tạp |
| Use Case | IoT | Enterprise |
| Message Size | Nhỏ | Lớn |

---

# Phần 6: Security Protocols

## 6.1 TLS/SSL

### Giới thiệu
- **Purpose**: Encryption, authentication
- **Port**: 443 (HTTPS)
- **Version**: TLS 1.2, 1.3

### TLS Handshake (1.2)
```
Client ─► ClientHello ──────────────────────►
Client ◄─ ServerHello + Cert + KeyEx ◄──────
Client ─► KeyExchange + ChangeCipherSpec ──►
Client ◄─ ChangeCipherSpec + Finished ◄────
[Encrypted Data]
```

### TLS 1.3 Improvements
- **1-RTT**: Thay 2-RTT
- **0-RTT**: Fast resumption
- **Removed**: MD5, SHA-1, 3DES, AES-CBC
- **Added**: ChaCha20-Poly1305, AES-GCM

---

## 6.2 OAuth 2.0

### Flows
| Grant | Use Case |
|-------|----------|
| Authorization Code | Web apps |
| PKCE | Mobile/SPA |
| Client Credentials | M2M |
| Refresh Token | Get new token |

### Tokens
- **Access Token**: API access
- **Refresh Token**: Get new access token
- **ID Token**: User identity (OIDC)

---

## 6.3 JWT (JSON Web Token)

### Structure
```
xxxxx.yyyyy.zzzzz
  │      │    │
  │      │    └─ Signature
  │      └────── Payload
  └───────────── Header
```

### Example
```json
// Header
{"alg": "HS256", "typ": "JWT"}

// Payload
{
  "sub": "1234567890",
  "name": "John",
  "iat": 1516239022,
  "exp": 1516242622
}

// Signature
HMACSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload), secret)
```

---

# Phần 7: Infrastructure

## 7.1 CDN (Content Delivery Network)

### How it works
```
User ──► CDN Edge ──► Origin (if not cached)
    ◄────── Response ──────────────
```

### Features
- Static asset caching
- SSL/TLS
- DDoS protection
- Image optimization
- Geo-routing

### Providers
- Cloudflare
- AWS CloudFront
- Akamai
- Fastly

---

## 7.2 Proxy & Reverse Proxy

### Forward Proxy
```
Client ──► Proxy ──► Internet ──► Server
```

### Reverse Proxy
```
Client ──► Reverse Proxy ──► Backend Servers
          (Nginx/HAProxy)
```

### Use Cases
| Type | Purpose |
|------|---------|
| Forward Proxy | Bypass firewall, cache |
| Reverse Proxy | LB, SSL termination, caching |

### Nginx vs HAProxy
| Feature | Nginx | HAProxy |
|---------|-------|---------|
| Layer | L7 | L4/L7 |
| Performance | Cao | Rất cao |
| SSL | ✅ | ✅ |

---

## 7.3 Load Balancer

### Algorithms
| Algorithm | Description |
|-----------|-------------|
| Round Robin | Sequential |
| Least Connections | Fewest active |
| IP Hash | Same client → same server |
| Weighted | Based on capacity |

### Health Check
- TCP check
- HTTP check
- HTTPS check
- Custom script

---

# Phụ lục: Công cụ Network

## Công cụ thường dùng

| Tool | Purpose |
|------|---------|
| `ping` | Check connectivity |
| `traceroute` | Path tracing |
| `nslookup` | DNS lookup |
| `dig` | DNS queries |
| `netstat` | Network stats |
| `ss` | Socket stats |
| `tcpdump` | Packet capture |
| `wireshark` | Packet analysis |
| `curl` | HTTP client |
| `httpie` | HTTP CLI |

## Command Examples
```bash
# Check connectivity
ping -c 4 google.com

# Trace route
traceroute google.com

# DNS lookup
dig google.com A +short
nslookup google.com

# Port scan
nmap -p 80,443 google.com

# Listen port
nc -l 8080
ss -tuln

# HTTP request
curl -X GET https://api.example.com
curl -X POST -H "Content-Type: application/json" \
  -d '{"key":"value"}' https://api.example.com

# Packet capture
tcpdump -i eth0 port 80
```

---

## Tài liệu tham khảo

### RFC Documents
- RFC 793 - TCP
- RFC 768 - UDP
- RFC 9000 - QUIC
- RFC 7540 - HTTP/2
- RFC 9113 - HTTP/3
- RFC 8446 - TLS 1.3
- RFC 6749 - OAuth 2.0
- RFC 7519 - JWT
- RFC 1035 - DNS

### Tài nguyên khác
- "Computer Networking: A Top-Down Approach"
- "High Performance Browser Networking" - Ilya Grigorik
- MDN Web Docs
- Cloudflare Blog
