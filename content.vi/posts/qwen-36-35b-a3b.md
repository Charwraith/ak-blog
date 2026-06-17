---
title: "qwen-36-35b-a3b"
displayTitle: "Qwen3.6-35B-A3B: Tại Sao MoE 3B-Hoạt-Động Của Alibaba Là Mối Đe Dọa Thực Sự Đầu Tiên Đối Với Các Mô Hình Mã Hóa Đóng"
date: 2026-06-18T09:00:00+08:00
draft: false
pillar: china-ai-outbound
clusters:
  - model-review
  - migration-guide
author: "AKRMIO"
description: "Qwen3.6-35B-A3B: Tại Sao MoE 3B-Hoạt-Động Của Alibaba Là Mối Đe Dọa Thực Sự Đầu Tiên Đối Với Các Mô Hình Mã Hóa Đóng"
---

Giữa tháng 6 năm 2026, Alibaba đã âm thầm phát hành phiên bản lượng tử hóa FP8 của Qwen3.6-35B-A3B trên Hugging Face — biến thể mã nguồn mở đầu tiên của dòng Qwen3.6. Kiến trúc MoE thưa 35B tổng / 3B hoạt động, ngữ cảnh gốc 262K (mở rộng lên 1M token), 73.4% trên SWE-bench, 51.5% trên Terminal-Bench.

## Tại sao MoE 3B-hoạt-động là mối đe dọa thực sự

Bế tắc của các mô hình mã nguồn mở là « mô hình nhỏ không xử lý được tác vụ phức tạp, mô hình lớn triển khai quá đắt ». Qwen3.6-35B-A3B đặt 35B « dung lượng kiến thức » vào 3B « chi phí suy luận ». Chỉ ~8.5% tham số được kích hoạt mỗi lần suy luận, nên chi phí mỗi token gần với mô hình dense 3B ; nhưng dung lượng tổng thể đạt 35B nhờ định tuyến thưa.

Đối với [Ralph Loop](https://akrmio.com/blog/posts/ralph-loop-coding/), chi phí kích hoạt 3B làm cho mỗi lần lặp rẻ hơn 70-80% so với Claude Sonnet 4.5, nhưng khoảng cách khả năng SWE-bench vẫn dưới 10%.

## Tác động đến mô hình chi phí API

Qwen3.6-35B-A3B lấp đầy điểm ngọt trên quang phổ « khả năng mã hóa - chi phí triển khai »:các mô hình 4B-8B rất rẻ nhưng SWE-bench < 50%;các mô hình 30B+ mạnh nhưng cần nhiều H100. Qwen3.6-35B-A3B chạy trên một H100 duy nhất với phiên bản lượng tử hóa FP8, chi phí triển khai gần với dense 7B, khả năng gần với 30B+.
