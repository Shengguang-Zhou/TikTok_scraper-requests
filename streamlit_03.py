from Scraper.extracting_03 import *
from Scraper.data_clean_03 import *
from Scraper.scraper_03 import *

# ToDO:
#  3. Add csv file uploadernand processer

########################################################################################################################################################################
########################################################################################################################################################################
###############################################################    Init     ############################################################################################
########################################################################################################################################################################
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

    user_panel['email'] = user_panel.apply(lambda row: 'User ID已改变' if row.get("user_subtitle") == "User ID已改变" else extract_email(row['user_bio']), axis=1)
    user_panel['Website'] = user_panel.apply(lambda row: 'User ID已改变' if row.get("user_subtitle") == "User ID已改变" else extract_websites(row['user_bio']), axis=1)
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

