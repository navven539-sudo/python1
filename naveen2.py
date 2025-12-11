import streamlit as st
st.title("welcome to streamlit")
num1=st.number_input ("Enter number 1",step=1)


num2=st.number_input("Enter number 2",step=2)
sum=num1+num2
if  st.button("Add"):
     st.write("sum is:",sum) 


sub=num1-num2
if st.button("Sub"):
    st.write("sub is:",sub)

multi=num1*num2
if st.button("Multi"):
    st.write("multi is:",multi)


divid=num1/num2
if st.button("Divid"):
    st.write("divid is:",divid)