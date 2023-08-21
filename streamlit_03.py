from extracting_03 import *
from data_clean_03 import *

# ToDO:
#  3. Add csv file uploadernand processer

########################################################################################################################################################################
###############################################################     Test input area     ################################################################################
########################################################################################################################################################################
# Initialization
# Upload username
# users_todo = ['davanlane', 'rosaless503', 'diylulu_5188', 'jacesanders590', 'yourm0msgirlfriend', 'sheisstillobsessed', 'huntersnipesxd', 'steevy502', 'kris_._22', 'iamfredyperez', 'weatherdaddy', 'thekeenecrew', 'jeremygiovinazzo', 'dalio14', 'ramirezanavil', 'laurenenslow', 'bbills', 'tatted_outdoorsy_vixen', 'lizzwhatley', 'kooneeg', 'tiago.pedace', 'jerseyboi83', '50thenew21', 'melany_laguera', 'magalylopez502', '_noyita_hernandez_', 'alisasmr1', 'addierich173', 'carlhoos2.0', 'lanatemireva', 'alicia.annn', 'estelaoro200', 'lac.bailey', 'suckafreesundays', 'lizzeth.1297_____', 'amurphyrn', 'geralynll', 'brerknoll', 'jjackrdgz', 'jaelanndavis', 'zaygee_', 'emitc_pr', 'shanleysings', 'alexanderinvicta', 'carlito_tenflow', 'shiemb7', 'big_luke_official', 'tesi.mae', 'shrk_cty_408', 'zacatecana05', 'saltybcreations', 'the_js2jimrose', 'itsjoenice', 'juanitosfam', 'miss_sabiko', 'uzair_official90', 'chaparrita_110387', 'unionganghq', 'gabry_wow', 'djyoungwheelz21', 'z.bunnies_', 'thomasroberts321', 'tarotbysoulless', 'michael_myers_florida', 'iamkorijoseph', 'bambamzee13', 'rainbow_tarot', 'darktinkerbell14', 'lovlysultan07', 'uncancellablemike', 'undeadangel0511', 'thunderdor', 'respempapoufakemoun', 'aidaargueta28', 'maddibabi1122', 'tinkerbellz777', 'steevecantara', 'karinabermudezlinares', 'thaboycurazy', 'efiwinnipeg', 'orlycastillo2.0', 'itzbelaroze', 'the_real_tkm93', '_kirriky', 'sol_200122', 'jasimmohamadalsha', 'codymcdonald2323', 'official_caragen', 'lover.alisha', 'kimberlyelayyne', 'unstoppable.sexxy', 'soundswithsasha', 'compaonce', 'cristinesworld', 'im_yake', 'bloodykronos', '0000yisus', 'team_journey_', 'johubae', 'therealbrandon2x', 'vickybrown_05', 'soyjuanguzman', 'bigfan12345865356', 'c14teen__', 'pray4leb', '___1mayalu', 'ihanabluhhhh', 'fwhatyaheard', 'crazy_jess77', 'superdem2022', 'habahtazeen2', 'claimitchristine', 'djchrisvybzz', 'sheisalpha1', 'sheisalpha1', 'coachrubenstein', 'carlito.oficial1', 'fonzy_jr760', 'david70lane', 'b0ymamax2', 'dblelevn', 'mirna_yo_soy_turista', 'got.joker', 'von_63rd', 'robot6753', 'kristjanaxg', '_lara19981', 'grldadof4', 'omimelli08', 'ainhoa_adeline_colins', 'lapatriciah22', '68pagan', 'rashak.25', 'peppa0511', 'that_blue_eyed_okie']
# users_todo = users_todo[55:80]

########################################################################################################################################################################
###############################################################    Init     ############################################################################################
########################################################################################################################################################################
def init():
    st.set_page_config(layout="wide",page_title='Tiktok达人信息')
    st.title('Tiktok Influencer Data  ')

init()

if 'uploaded' not in st.session_state:
    st.session_state.uploaded = None

if 'todo_list' not in st.session_state:
    st.session_state.todo_list = None

if 'user_panel' not in st.session_state:
    st.session_state.user_panel = None

if 'panel_show' not in st.session_state:
    st.session_state.panel_show = False
if st.session_state.todo_list == None:
    st.session_state.panel_show = False
else:
    True
######################################################################################################################################################################
######################################################################################################################################################################
######################################################################################################################################################################

# get user panel
def get_user_panel(usersnames):
    user_panel = getUsersInfoThru(usersnames)
    user_panel = pd.DataFrame(user_panel)
    user_panel['Email'] = user_panel.iloc[:,2].apply(extract_email)
    user_panel['Website'] = user_panel.iloc[:,2].apply(extract_websites)
    user_panel['是否已联系'] = ''
    return user_panel

# Download data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

########################################################################################################################################################################
########################################################################################################################################################################
###################################################################### Streamlit begin #################################################################################

if st.session_state.uploaded:
    if st.button('下载'):
        convert_df(st.session_state.user_panel)


# Show user panel
if st.session_state.uploaded:
    st.data_editor(st.session_state.user_panel,
                   column_config={
                       'Website':st.column_config.LinkColumn('相关网页',help = '该网页为用户个人/组织页面、网店、或其他合作方页面'),
                       '是否已联系':st.column_config.CheckboxColumn('是否已联系',help='联系该用户后请勾选')},
                   hide_index = True,
                   disabled=['0','1','2','3','4'],
                   use_container_width=True)

# uploading
with st.sidebar:
    file_uploader = st.file_uploader(label='**上传文件**',type = ['csv'],help = '拖拽或选择文件上传，片刻后达人数据将会加载')
    if st.button('Upload'):
        if file_uploader:
            st.session_state.todo_list = csv_to_list(file_uploader)
            st.session_state.user_panel = get_user_panel(st.session_state.todo_list)
            st.session_state.uploaded = True
        else:
            st.write('请上传文件')


# 显示所有email
# TODO：
#  2.Selector -> box for showing and sending email
#  3.Sending email

# # filtering
# column = st.selectbox('仅展示粉丝数在区间内的账户:',user_panel.columns)
# min_val, max_val = st.slider('选择粉丝区间数量', min(user_panel['粉丝数']), max(user_panel['粉丝数']),
#                              (user_panel(df['粉丝数']), user_panel(df['粉丝数'])))
# filtered_userPanel = user_panel[(user_panel['粉丝数'] >= min_val) & (user_panel['粉丝数'] <= max_val)]
# st.dataframe(filtered_userPanel)

