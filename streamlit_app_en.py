import streamlit as st

from PIL import Image

st.set_page_config(layout="wide")

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #111C28;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
  image = Image.open('Img_app1.png')
  st.image(image)

  st.title('Genetic background')
  #st.markdown("***")
  
  st.header('Consanguinity')
  consanguinity_result = st.radio(
     "Consanguinity",
     ('No','Yes'))
  if consanguinity_result == 'Yes':
    st.write(':warning: This increases the probability of any recessive genetic syndrome!')
  sex_result = st.selectbox(
      'Sex',
      ('Unknown', 'Female', 'Male', 'Ambiguous'))


  st.header('Chromosome analysis')

  dpni_result = st.selectbox(
      'DPNI',
      ('Unknown', 'No', 'Yes and negatif', 'Yes and positif'))
  if dpni_result == 'Yes and positif':
    st.write(f'NIPT enter result :')
  
  karyotype_result = st.selectbox(
    'Karyotype',
    ('Unknown', 'No', 'Yes and negatif', 'Yes and positif'))
  if karyotype_result == 'Yes and positif':
    st.write(f'Karyotype enter result :')

  cgh_result = st.selectbox(
    'CMA/CGH array',
    ('Unknown', 'No', 'Yes and negatif', 'Yes and positif'))
  if cgh_result == 'Yes and positif':
    st.write(f'CMA/CGH array enter result :')


#col1, col2, col3 = st.columns(3)

colL1,colL2 = st.columns([25,10])
with colL2:
  image = Image.open('Img_app2.png')
  st.image(image)


#colT1,colT2 = st.columns([3,8])
#with colT2:
#st.title('Exome Analysis')

#st.text("")
st.header('Exome reader')

multi_css=f'''
<style>
.stMultiSelect div div div div div:nth-of-type(2) {{visibility: hidden;}}
.stMultiSelect div div div div div:nth-of-type(2)::before {{visibility: visible; content:"Select an anomaly"}}
</style>
'''
st.markdown(multi_css, unsafe_allow_html=True)

options = st.multiselect(
     'Ultrasound Warning Signs',
     ['Syndactyly of the toes', 'Proptosis', 'Hypertelorism', 'Brachyturricephaly', 'Other'])
st.text("")
if st.button('Summary'):
  st.write('Apert syndrome')
  col1, col2 = st.columns(2)
  with col1:
    st.write('Proximity score : 9/10') 
  with col2:
    st.write('1.25 births on 10 000')

st.markdown("***")
st.text("")

exome_result = st.selectbox(
  'Exome analysis',
  ('No', 'Yes'))
if exome_result == 'Yes':
  #st.write(f'Exome enter result :')
  st.header('Exome result file')
  uploaded_file = st.file_uploader("Select a vcf file")

  if uploaded_file is not None:
    if st.button('Run'):
      st.write('Mutated gene: FGFR2 with a probability of 99.6%')
      col1, col2 = st.columns(2)
      with col1:
        st.write('Diagnosed syndrome : ')
        st.code("""
          Apert syndrome
          Phenotypic similarity 91.9 %
          """)
        st.write('Autosomal dominant syndrome')
      with col2:
        st.write('Identified variant : ')
        st.code("""
          MISSENSE_VARIANT SNV 10-123256215-T-G [0/1]
          Score variant : 100 %
          """)
        url = "https://www.ncbi.nlm.nih.gov/snp/rs121918506"
        st.write("[rs121918506](%s)" % url)

      st.write('Genetic sex : XY')
      
      st.write('Other possible clinical signs to check : ')
      st.code("""
        Bicoronal synostosis
        Abnormally wide anterior fontanel
        Cutaneous syndactyly of the fingers
        Fusion of cervical vertebrae C5/C6
        Depressed nasal bridge
        Prominent frontal humps
        """)
    else:
      st.write('Run analysis')
    #df = pd.read_csv(uploaded_file)
    #st.subheader('DataFrame')
    #st.write(df)
    #st.subheader('Descriptive Statistics')
    #st.write(df.describe())
  else:
    st.info('Load a vcf file!')




st.markdown("***")

image = Image.open('logo_sonio_blanc.png')
st.image(image)


