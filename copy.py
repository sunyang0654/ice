import pandas as pd
import streamlit as st
import os
from datetime import datetime
import openpyxl


st.set_page_config(layout="wide")

st.title('hello')
uploaded_file = st.file_uploader('Upload an Excel file', type=['xlsx','xls'])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    # st.write(df)
else:
    st.write('Please upload an Excel file.')

today = datetime.today().strftime("%Y%m%d")

if uploaded_file is not None:

    # 提取第一列数据（索引0，若首行是标题需调整为iloc[1:, 0]）
    first_column = df.iloc[:, 0]  # 若第一行是标题，改为 iloc[1:, 0] 跳过标题

    # 对第一列数据进行去重
    unique_first_column = first_column.drop_duplicates()

    # 创建新DataFrame（仅包含去重后的第一列）
    new_df = pd.DataFrame({'第一列内容': unique_first_column})

    # 获取桌面路径（通用方法）
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # 生成新文件名（test_20250520.xlsx）
    output_path = os.path.join(desktop_path, f"test_{today}.xlsx")

    # 保存新表格
    try:
      new_df.to_excel(output_path, index=False, sheet_name='Sheet1')
      print(f"文件已成功保存至桌面：{output_path}")
    except Exception as e:
      print(f"保存文件失败，错误信息：{e}")

 #   st.dataframe(data=df.reset_index(drop=True),use_container_width=True,hide_index=True)

    st.dataframe(data=new_df.reset_index(drop=True),use_container_width=True,hide_index=True)