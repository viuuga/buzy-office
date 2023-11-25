import streamlit as st

st.set_page_config(page_title="GuardianEye", page_icon="web_znach.png", layout="wide")


st.markdown("""
<style>
.st-emotion-cache-6q9sum.ef3psqc4
{
    visibility: hidden;
}
.st-emotion-cache-ch5dnh.ef3psqc5
{
    visibility: hidden;
}
.st-br.st-bq.st-as.st-at.st-b7.st-b6.st-bs.st-bt.st-bu.st-bv.st-av.st-aw.st-ax.st-ay.st-bj.st-bw.st-bx.st-by.st-bz.st-c0.st-c1.st-c2
{
    visibility: hidden;
}
.st-emotion-cache-cio0dv.ea3mdgi1
{
    visibility: hidden;
}
.st-emotion-cache-4z1n4l.en6cib65
{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)






st.sidebar.success("Вы на главной странице") 

col_head = st.columns(3)[1]
with col_head:
    st.title("GuardianEye")
col_subhead = st.columns(1)[0]
with col_subhead:
    st.subheader("Интеллектуальная безопасность и оптимизация бизнес-процессов в розничной торговле.")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.header("Этот проект охватывает области безопасности, эффективности персонала и управления розничными предприятиями с использованием передовых технологий, таких как умные камеры и нейронные сети. Путем интеграции этих технологий проект стремится создать инновационные решения для автоматизации процессов, улучшения безопасности и повышения эффективности работы персонала в магазинах и торговых сетях.")
    

with col2:
    st.image('smart_cam.png')

col1, col2 = st.columns(2)
