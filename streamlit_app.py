
import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="Data Cleaner Pro", layout="wide")

    # Branding Header
    st.markdown("<h1 style=\'text-align: center; color: #1E90FF;\'>Data Cleaner Pro</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style=\'text-align: center; color: #555555;\'>أداة احترافية لتنظيف البيانات</h3>", unsafe_allow_html=True)
    st.markdown("--- ")

    st.sidebar.header("إعدادات تنظيف البيانات")

    uploaded_file = st.sidebar.file_uploader("اسحب الملف أو اضغط للاختيار", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(".xlsx"):
                df = pd.read_excel(uploaded_file)
            
            st.success("تم تحميل الملف بنجاح!")
            st.write("نظرة عامة على البيانات الأصلية:")
            st.dataframe(df.head())

            st.sidebar.subheader("خيارات التنظيف")
            
            # Handle missing values
            if st.sidebar.checkbox("التعامل مع القيم المفقودة"):
                missing_option = st.sidebar.radio("كيف تريد التعامل مع القيم المفقودة؟", 
                                                  ("إزالة الصفوف", "ملء بالمتوسط", "ملء بالوسيط", "ملء بالوضع"))
                if missing_option == "إزالة الصفوف":
                    df.dropna(inplace=True)
                elif missing_option == "ملء بالمتوسط":
                    for col in df.select_dtypes(include=['number'\]).columns:
                        df[col].fillna(df[col].mean(), inplace=True)
                elif missing_option == "ملء بالوسيط":
                    for col in df.select_dtypes(include=\['number'\]).columns:
                        df[col].fillna(df[col].median(), inplace=True)
                elif missing_option == "ملء بالوضع":
                    for col in df.columns:
                        df[col].fillna(df[col].mode()[0], inplace=True)
                st.sidebar.success("تم التعامل مع القيم المفقودة.")

            # Remove duplicates
            if st.sidebar.checkbox("إزالة الصفوف المكررة"):
                df.drop_duplicates(inplace=True)
                st.sidebar.success("تم إزالة الصفوف المكررة.")

            # Convert data types (example for numeric)
            if st.sidebar.checkbox("تحويل أنواع البيانات (لتحويل الأعمدة الرقمية)"):
                numeric_cols = df.select_dtypes(include=\['object'\]).columns
                if len(numeric_cols) > 0:
                    selected_col = st.sidebar.selectbox("اختر عمودًا لتحويله إلى رقمي", numeric_cols)
                    if st.sidebar.button("تحويل"):
                        try:
                            df[selected_col] = pd.to_numeric(df[selected_col], errors=\'coerce\')
                            st.sidebar.success(f"تم تحويل العمود {selected_col} إلى رقمي.")
                        except ValueError:
                            st.sidebar.error("لا يمكن تحويل هذا العمود إلى رقمي.")
                else:
                    st.sidebar.info("لا توجد أعمدة نصية قابلة للتحويل إلى رقمية.")

            st.subheader("البيانات بعد التنظيف:")
            st.dataframe(df)

            # Download cleaned data
            csv_file = df.to_csv(index=False).encode(\'utf-8\')
            st.download_button(
                label="تنزيل البيانات المنظفة كملف CSV",
                data=csv_file,
                file_name="cleaned_data.csv",
                mime="text/csv",
            )

        except Exception as e:
            st.error(f"حدث خطأ أثناء معالجة الملف: {e}")
    else:
        st.info("يرجى رفع ملف CSV أو Excel للبدء.")

    # Branding Footer
    st.markdown("--- ")
    st.markdown("<p style='text-align: center; color: #888888; font-size: small;'>Developed by Ahmed Saeed Noaman | <a href='https://www.linkedin.com/in/ahmed-noaman-data' target='_blank' rel='noopener noreferrer'>LinkedIn</a> | Data Analytics Project</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
