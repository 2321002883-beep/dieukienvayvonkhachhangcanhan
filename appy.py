import streamlit as st

# Tiêu đề
st.title("HỆ THỐNG ĐÁNH GIÁ ĐIỀU KIỆN VAY VỐN CÁ NHÂN")

st.write("### Nhập thông tin khách hàng")

# Nhập dữ liệu
STV = st.number_input("Số tiền muốn vay (triệu đồng)", min_value=0.0, step=1.0)
TGV = st.number_input("Thời gian vay (năm)", min_value=1.0, step=1.0)
LSV = st.number_input("Lãi suất vay (ví dụ: 0.12 = 12%)", min_value=0.0, step=0.01, format="%.2f")
TN = st.number_input("Thu nhập của hai vợ chồng (triệu đồng/tháng)", min_value=0.0, step=1.0)
SNTGD = st.number_input("Số người trong gia đình", min_value=0, step=1)
PTMC = st.number_input("Số tiền phải trả khoản vay cũ (triệu đồng/tháng)", min_value=0.0, step=1.0)
GTTSDB = st.number_input("Giá trị tài sản đảm bảo (triệu đồng)", min_value=1.0, step=1.0)
Tuoi = st.number_input("Tuổi khách hàng", min_value=18, max_value=100, step=1)

# Chi phí sinh hoạt
CPSH = 5

# Nút tính toán
if st.button("Đánh giá điều kiện vay"):

    # Tính toán
    PTMM = (STV / (TGV * 12)) + (STV * (LSV / 12))
    DTI = (PTMC + PTMM) / (TN - SNTGD * CPSH)
    LTV = STV / GTTSDB

    # Hiển thị kết quả
    st.subheader("Kết quả tính toán")
    st.write(f"**Số tiền phải trả hàng tháng cho khoản vay mới:** {PTMM:.2f} triệu đồng")
    st.write(f"**Chỉ số DTI:** {DTI:.2f}")
    st.write(f"**Chỉ số LTV:** {LTV:.2f}")

    # Đánh giá
    if DTI <= 0.7 and LTV <= 0.7 and 18 < Tuoi < 70:
        st.success("✅ Khách hàng ĐƯỢC VAY")
    else:
        st.error("❌ Khách hàng KHÔNG ĐƯỢC VAY")
