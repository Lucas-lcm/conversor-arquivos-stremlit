import streamlit as st
import pandas as pd
from io import BytesIO
import json 
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Function to create a template for final fields in Excel format
def create_template():
    """Creates a DataFrame template for final fields."""
    template_data = {
        'Nome do campo': ['Field1', 'Field2', 'Field3'],  # Example fields
        'Tipo': ['text', 'numeric', 'text']  # Example types
    }
    return pd.DataFrame(template_data)

# Function to convert DataFrame to Excel and return as bytes
def to_excel(df):
    """Converts a DataFrame to an Excel file and returns it as bytes."""
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Transformed Data')
    output.seek(0)
    return output

# Function to save mappings to a JSON file
def save_mappings(mappings):
    """Saves the mappings to a JSON file."""
    return json.dumps(mappings)

# Function to load mappings from a JSON file
def load_mappings(json_data):
    """Loads mappings from a JSON file."""
    return json.loads(json_data)

# Streamlit app
st.set_page_config(page_title="1. Conversor MMB", page_icon=":material/source_notes:", layout="wide")

#Header
col_space0, col_main0, col_sapce0 = st.columns(
    (4,4,4)
)
with col_main0:
    st.title("Conversor MMB")

# Initialize state variables
if 'path' not in st.session_state:
    st.session_state.path = None  # Track the current path
if 'step' not in st.session_state:
    st.session_state.step = None  # Track the current step
if 'mappings' not in st.session_state:
    st.session_state.mappings = {} # Initialize mapping in session state
if 'df' not in st.session_state:
    st.session_state.df = None  # Initialize df in session state

#Columns config spacement
col_space1, col_main1, col_sapce1 = st.columns((1,6,1))
# Back and Next button config spacement
back, blank, next = st.columns((4,30,4))

#Button set steps
def set_step_path(step, path):
    st.session_state.path = path
    st.session_state.step = step

# Path selection
if st.session_state.path is None and st.session_state.step is None:
    
    with col_main1:
        st.subheader("Selecione uma das opções:")
        path_option = st.radio("Opções:", (
            "Novo mapeamento", 
            "Usar um mapeamento já configurado"
            )
        )
        st.button("Próximo", on_click=set_step_path, args=[1, path_option])
                
# First Path:
if st.session_state.path == "Novo mapeamento":
    # Step 1 - Upload Final Fields File
    if st.session_state.step == 1:

        with col_main1:
            st.subheader("Etapa 1: Carga do arquivo com os campos finais")
            final_fields_file = st.file_uploader("Carregue o arquivo (Excel):", type=["xlsx"])
            # Download button for template
            template_df = create_template()
            excel_file = to_excel(template_df)
            st.download_button(
                label="Baixar o modelo (Excel)",
                data=excel_file,
                file_name='final_fields_template.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                key="download-template"
            )
            
            if final_fields_file is not None:
                try:
                    st.session_state.final_fields_df = pd.read_excel(final_fields_file) #Return if file uploaded correctly
                    st.success("Arquivo de campos finais carregado com sucesso!")
                    with next:
                        st.button("Próximo", on_click=set_step_path, args=[2, "Novo mapeamento"])
                except Exception as e:
                    st.error(f"Erro ao ler o arquivo de campos finais: {e}")

            with back:
                # Back button
                if st.button("Recomeçar", on_click=set_step_path, args=[None, None]):
                    st.session_state.mappings = {}  # Clear mappings
                    st.session_state.df = None  # Clear DataFrame


    # Step 2 - Upload Data File and Define Header Row
    elif st.session_state.step == 2:

        with col_main1:
            st.subheader("Etapa 2: Carregar arquivo de dados que será transformado")
            uploaded_file = st.file_uploader("Carregue o arquivo (CSV ou Excel):", type=["csv", "xlsx"])
            header_row = st.number_input("Insira o número da linha onde o cabeçalho começa:", min_value=1, value=1)

            if uploaded_file is not None:
                with st.spinner("Carregando dados..."):
                    try:
                        if uploaded_file.name.endswith('.csv'):
                            df = pd.read_csv(uploaded_file, header=header_row - 1)  # Convert to 0-based index
                            st.session_state.df = df
                            st.session_state.uploaded_columns = df.columns.tolist()
                            st.write("Colunas do arquivo carregado:", st.session_state.uploaded_columns) #Return if files columns are loaded 
                        elif uploaded_file.name.endswith('.xlsx'):
                            df = pd.read_excel(uploaded_file, header=header_row - 1)  # Convert to 0-based index
                            st.session_state.df = df
                            st.session_state.uploaded_columns = df.columns.tolist()
                            st.write("Colunas do arquivo carregado:", st.session_state.uploaded_columns) #Return if files columns are loaded 
                        else:
                            st.error("Tipo de arquivo não suportado. Carregue um arquivo CSV ou Excel.") #Return if file is not suported
                            st.stop()
                    except Exception as e:
                        st.error(f"Erro ao ler o arquivo: {e}") #Return if error to read the file
                        st.stop()
                        
                # Create dropdowns for mapping based on final fields
                st.subheader("Mapear colunas:")
                for field_name in st.session_state.final_fields_df['Nome do campo']:
                    selected_column = st.selectbox(f"Selecione a coluna que irá para {field_name}:", options=[''] + st.session_state.uploaded_columns, key=f"selecione_{field_name}")
                    st.session_state.mappings[field_name] = selected_column

                # Show the current mappings
                st.subheader("Mapeamento realizado:")
                for field, column in st.session_state.mappings.items():
                    st.write(f"{field} -> {column}")

                #Save mappings as Json
                json_mappings = save_mappings(st.session_state.mappings)
                st.download_button(
                    label="Baixar mapeamento (JSON)",
                    data=json_mappings,
                    file_name='mapeamento.json',
                    mime='application/json'
                )

                # Check if all fields are mapped
                with next:
                    st.button("Próximo", on_click=set_step_path, args=[3, "Novo mapeamento"])

        # Back button
        with back:
            st.button("Voltar", on_click=set_step_path, args=[1, "Novo mapeamento"])

    # Step 3 - Download Transformed File
    elif st.session_state.step == 3:

        with col_main1:
            st.subheader("Etapa 3: Baixe o arquivo transformado")

            # Create a new DataFrame based on the mappings using original field names
            transformed_data = {field: st.session_state.df[st.session_state.mappings[field]] for field in st.session_state.mappings.keys()}
            transformed_df = pd.DataFrame(transformed_data)
            st.write("Tabela transformada:")
            st.dataframe(transformed_df)

            # Allow user to download the transformed DataFrame as Excel
            excel_output = to_excel(transformed_df)
            st.download_button(
                label="Baixar tabela transformada (Excel)",
                data=excel_output,
                file_name='dados_transformados.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )

        with back:
            st.button("Voltar", on_click=set_step_path, args=[2, "Novo mapeamento"])

        with next:
            if st.button("Recomeçar", on_click=set_step_path, args=[None, None]):
                    st.session_state.mappings = {}  # Clear mappings
                    st.session_state.df = None  # Clear DataFrame

# Second Path:
elif st.session_state.path == "Usar um mapeamento já configurado":
    # Step 1 - Upload JSON mapping and data file to be transformed
    if st.session_state.step == 1:

        with col_main1:
            st.subheader("Etapa 1: Carga do arquivo de mapeamento e o arquivo que será transformado:")
            uploaded_mapping_file = st.file_uploader("Carregue o arquivo de configuração do mapeamento (JSON)", type=["json"]) # Upload JSON mapping file
        
            if uploaded_mapping_file is not None:
                try:
                    json_data = uploaded_mapping_file.read().decode("utf-8")
                    st.session_state.mappings = load_mappings(json_data)
                    st.success("Mapeamento carregado com sucesso!")
                except Exception as e:
                    st.error(f"Erro ao carregar o mapeamento: {e}")
                
                # Upload data file
                uploaded_file = st.file_uploader("Carregue o arquivo (CSV ou Excel):", type=["csv", "xlsx"])
                header_row = st.number_input("Insira o número da linha onde o cabeçalho começa:", min_value=1, value=1)

                if uploaded_file is not None:
                    with st.spinner("Carregando dados... "):
                        try:
                            if uploaded_file.name.endswith('.csv'):
                                df = pd.read_csv(uploaded_file, header=header_row - 1)  # Convert to 0-based index
                            elif uploaded_file.name.endswith('.xlsx'):
                                df = pd.read_excel(uploaded_file, header=header_row - 1)  # Convert to 0-based index
                            else:
                                st.error("Tipo de arquivo não suportado. Carregue um arquivo CSV ou Excel.")
                                st.stop()
                        except Exception as e:
                            st.error(f"Erro ao ler o arquivo: {e}")
                            st.stop()

                    st.session_state.df = df
                    st.session_state.uploaded_columns = df.columns.tolist()
                    st.write("Colunas do arquivo carregado:", st.session_state.uploaded_columns)

                    # Display the mappings
                    st.subheader("Mapeamento realizado:")
                    for field, column in st.session_state.mappings.items():
                        st.write(f"{field} -> {column}")

                with next:
                    st.button("Próximo", on_click=set_step_path, args=[2, "Usar um mapeamento já configurado"])

            with back:
                if st.button("Recomeçar", on_click=set_step_path, args=[None, None]):
                    st.session_state.mappings = {}  # Clear mappings
                    st.session_state.df = None  # Clear DataFrame

    # Step 2 - Download Transformed File
    elif st.session_state.path == "Usar um mapeamento já configurado" and st.session_state.step == 2:

        with col_main1:
            st.subheader("Etapa 2: Baixe o arquivo transformado")

            # Check if the DataFrame and mappings are available
            if st.session_state.df is not None and st.session_state.mappings:
                # Create a new DataFrame based on the mappings using original field names
                transformed_data = {field: st.session_state.df[st.session_state.mappings[field]] for field in st.session_state.mappings.keys()}
                transformed_df = pd.DataFrame(transformed_data)
                st.write("Tabela transformada:")
                st.dataframe(transformed_df)

                # Allow user to download the transformed DataFrame as Excel
                excel_output = to_excel(transformed_df)
                st.download_button(
                    label="Baixar tabela transformada (Excel)",
                    data=excel_output,
                    file_name='dados_transformados.xlsx',
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
        
        with back:
            st.button("Voltar", on_click=set_step_path, args=[1, "Usar um mapeamento já configurado"])

        with next:
            if st.button("Recomeçar", on_click=set_step_path, args=[None, None]):
                    st.session_state.mappings = {}  # Clear mappings
                    st.session_state.df = None  # Clear DataFrame