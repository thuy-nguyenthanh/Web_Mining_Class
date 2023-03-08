import re
text="Tại Đại hội Thể thao Đông Nam Á 2021, Đội tuyển nữ Việt Nam và Đội tuyển U-23 Việt Nam đã bảo vệ thành công tấm huy chương vàng tại SEA Games 30 sau chiến thắng lần lượt trước Đội tuyển nữ Thái Lan (1-0) và Đội tuyển U-23 Thái Lan (1-0)."

text_pre = re.sub("\d+", " ", text)
print(text_pre)