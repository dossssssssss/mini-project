import streamlit as st
import pandas as pd


def print_hi(name="World"):
    st.write(f"## Hello, {name}!")


print_hi()
df = pd.DataFrame(dict(x=[1, 2, 3, 4],
                       y=[13, 17, 14, 21]))
st.line_chart(df)


# if __name__ == '__main__':
#    print_hi('PyCharm')
