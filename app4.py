import streamlit as st
import pandas as pd

def main():
    df = pd.read_csv('./data/iris.csv')

    if st.button('데이터 프레임 보기'):
      st.dataframe( df )

      name = 'Mike'

     # 버튼 만드는 방법
    if st.button('대문자'):
      st.subheader( name.upper() )

    if st.button('소문자'):
      st.subheader( name.lower() )   

    #라디오버튼을 만드는 방법
    selected = st.radio('정렬을 선택하세요', ['오름차순 정렬','내림차순 정렬'])

    #df의 petal_length 컬럼을 정렬하도록 한다.

    if selected == '오름차순 정렬' :
      df.sort_values('petal_length')

    if selected == '내림차순 정렬' :
     st.dataframe(df.sort_values('petal_length', ascending=False))

     #체크박스를 나타내는 방법
    if st.checkbox('데이터프레임 보이기'):
       st.dataframe( df )
    else :
        st.write('')

    #셀렉트 박스 : 여러개중에 한개를 선택할때
    language = ['python','Java','C','PHP','GO']   

    my_choice = st.selectbox('좋아하는 언어를 선택하세요', language)

    st.text('저는 {} 언어를 좋아합니다.'.format(my_choice))

    if my_choice == language[0] or my_choice == language[3] or my_choice == language[-1]:
       st.text('배우기 쉽습니다.')
    elif my_choice == language[1] or my_choice == language[2]:
       st.text('배우기 어렵습니다.')   

     
     
     #멀티셀렉트 : 여러개를 동시에 선택 가능

    selected_list = st.multiselect('여러개 선택 가능', df.columns)

    print(selected_list)
    
# 여러 슬라이더의 초기값 설정
initial_age = 25
data_slider_value = 125

# 여러 슬라이더 생성
age = st.slider('나이를 선택하세요', 0, 100, value=initial_age)
data_slider = st.slider('데이터 선택', 50, 200, step=10, value=data_slider_value)

# 값을 리스트에 저장
values_list = [age, data_slider]

# 리스트의 값을 텍스트로 출력
st.text('제 나이는 ' + str(values_list[0]) + '입니다.')
st.text('선택된 데이터 값: ' + str(values_list[1]))

if __name__== '__main__' :
     main()