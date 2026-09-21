# Student Tools

Student Tools là một bộ tiện ích Python nhỏ phục vụ việc học tập và thực hành quy trình cộng tác mã nguồn mở trên GitHub.

## Tính năng

- Các phép tính cơ bản: cộng, trừ, nhân, chia.
- Đổi nhiệt độ giữa Celsius, Fahrenheit và Kelvin.
- Đổi khoảng cách giữa kilomet và mile, mét và kilomet.
- Kiểm tra dữ liệu số và chuỗi không rỗng.

## Converter

Student Tools hỗ trợ đổi nhiệt độ giữa Celsius, Fahrenheit và Kelvin, cùng với một số chuyển đổi khoảng cách thông dụng.

Xem ví dụ sử dụng trong [docs/usage.md](docs/usage.md).

## Bắt đầu nhanh

Yêu cầu Python 3.10 trở lên.

```bash
git clone <repository-url>
cd student-tools

PYTHONPATH=src python -m unittest discover -s tests -v
```

Ví dụ sử dụng:

```python
from student_tools import celsius_to_fahrenheit, divide

print(celsius_to_fahrenheit(25))
print(divide(10, 2))
```

Xem thêm API và ví dụ trong [docs/usage.md](docs/usage.md).

## Cấu trúc dự án

```text
student-tools/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml
├── src/
│   └── student_tools/
│       ├── calculator.py
│       ├── converter.py
│       └── validator.py
├── tests/
└── docs/
    └── usage.md
```

## Quy trình đóng góp

Mỗi thay đổi nên bắt đầu từ một Issue, được thực hiện trên feature branch, có test, rồi gửi Pull Request để một thành viên khác review. Xem chi tiết trong [CONTRIBUTING.md](CONTRIBUTING.md).
