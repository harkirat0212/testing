#pip install streamlit
import streamlit as st

st.set_page_config(page_title="My first app", page_icon="☕", layout="centered")
# st.set_page_config(page_title="My first app", page_icon=":coffee:", layout="wide")
st.title("This is my first app")
# st.header("This is a header")
# st.subheader("This is a subheader")
# st.text("This is a text")
# st.markdown("This is a markdown")  #similar to to write but used for formating
# st.latex(r"a^2 + b^2 = c^2")
# st.code("import streamlit as st")
# st.write("This is a write")

name=st.text_input("Enter your name")
age=st.number_input("Enter your age",min_value=18,max_value=60)
password=st.text_input("Enter your password", type="password")
vol=st.slider("Select a volume",min_value=0,max_value=100)
color=st.color_picker("Select a color")
date=st.date_input("Select a date")
time=st.time_input("Select a time")
dept=st.selectbox("Select a department",["CSE","ECE","IT","ME","CE"])
subject=st.multiselect("Select a subject",["Maths","Physics","Chemistry","Biology"])

btn=st.button("Click me")

if btn:
    # st.write(name)
    # st.write(age)
    # st.write(password)
    # st.write(vol)
    # st.write(color)
    # st.write(date)
    # st.write(time)
    # st.write(dept)
    # st.write(subject)
    st.error("This is an error")
    st.warning("This is a warning")
    st.info("This is an info")
    st.success("This is a success")
    st.balloons()
    st.snow()