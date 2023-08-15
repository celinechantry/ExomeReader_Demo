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

  st.title('Antécédents génétiques')
  #st.markdown("***")
  
  st.header('Consanguinité')
  consanguinity_result = st.radio(
     "Consanguinité",
     ('Non','Oui'))
  if consanguinity_result == 'Oui':
    st.write(':warning: Cela augmente la probabilité de tout syndrome génétique récessif!')
  sex_result = st.selectbox(
      'Sexe',
      ('Inconnu', 'Feminin', 'Masculin', 'Ambigu'))


  st.header('Analyses chromosomiques')

  dpni_result = st.selectbox(
      'DPNI',
      ('Inconnu', 'Non', 'Oui et négatif', 'Oui et positif'))
  if dpni_result == 'Oui et positif':
    st.write(f'DPNI saisir le résultat :')
  
  caryotype_result = st.selectbox(
    'Caryotype',
    ('Inconnu', 'Non', 'Oui et négatif', 'Oui et positif'))
  if caryotype_result == 'Oui et positif':
    st.write(f'Caryotype saisir le résultat :')

  cgh_result = st.selectbox(
    'ACPA/CGH array',
    ('Inconnu', 'Non', 'Oui et négatif', 'Oui et positif'))
  if cgh_result == 'Oui et positif':
    st.write(f'ACPA/CGH array saisir le résultat :')


#col1, col2, col3 = st.columns(3)

colL1,colL2 = st.columns([25,10])
with colL2:
  image = Image.open('Img_app2.png')
  st.image(image)


#colT1,colT2 = st.columns([3,8])
#with colT2:
#st.title('Analyse Exome')

#st.text("")
st.header('Exome reader')

multi_css=f'''
<style>
.stMultiSelect div div div div div:nth-of-type(2) {{visibility: hidden;}}
.stMultiSelect div div div div div:nth-of-type(2)::before {{visibility: visible; content:"Choisir une anomalie"}}
</style>
'''
st.markdown(multi_css, unsafe_allow_html=True)

options = st.multiselect(
     'Signes d\'Appel Echographiques',
     ['Syndactylie des orteils','Proptose', 'Hypertélorisme', 'Brachyturricéphalie','Autre'])
st.text("")
if st.button('Synthèse'):
  st.write('Syndrome d\'Apert')
  col1, col2 = st.columns(2)
  with col1:
    st.write('Score de proximité : 9/10') 
  with col2:
    st.write('1.25 naissances sur 10 000')

st.markdown("***")
st.text("")

exome_result = st.selectbox(
  'Analyse d\'Exome',
  ('Non', 'Oui'))
if exome_result == 'Oui':
  #st.write(f'Exome saisir le résultat :')
  st.header('Fichier résultat Exome')
  uploaded_file = st.file_uploader("Selectionner un fichier vcf")

  if uploaded_file is not None:
    if st.button('Run'):
      st.write('Gène muté : FGFR2 avec une probabilité de 99,6 %')
      col1, col2 = st.columns(2)
      with col1:
        st.write('Syndrome diagnostiqué : ')
        st.code("""
          Syndrome d'Apert
          Similarité phenotypique 91,9 %
          """)
        st.write('Syndrome Autosomique dominant')
      with col2:
        st.write('Variant identifié : ')
        st.code("""
          MISSENSE_VARIANT SNV 10-123256215-T-G [0/1]
          Score variant : 100 %
          """)
        url = "https://www.ncbi.nlm.nih.gov/snp/rs121918506"
        st.write("[rs121918506](%s)" % url)

      st.write('Sexe génétique : XY')
      
      st.write('Autres signes cliniques possibles à vérifier : ')
      st.code("""
        Synostose bicoronale
        Fontanelle antérieure anormalement large
        Syndactylie cutanée des doigts
        Fusion des vertèbres cervicales C5/C6
        Pont nasal deprimé
        Bosses frontales proéminentes
        """)
    else:
      st.write('Lancer l\'analyse')
    #df = pd.read_csv(uploaded_file)
    #st.subheader('DataFrame')
    #st.write(df)
    #st.subheader('Descriptive Statistics')
    #st.write(df.describe())
  else:
    st.info('Chargez un fichier vcf!')




st.markdown("***")

image = Image.open('logo_sonio_blanc.png')
st.image(image)


