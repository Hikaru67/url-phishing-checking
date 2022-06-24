PATH_DATA_ALL = 'data/processed2604.csv'
PATH_SAVE_DATA = 'data_save'
PATH_SAVE_MODEL = 'model'
TRAINING_RATE = 0
PORT = 6001
HOST = '127.0.0.1'

MODEL_SUGGESTIONS = {
  1: 'CẢNH BÁO! URL có thể nguy hiểm',
  0: 'Khả năng URL là bình thường'
}
features = ['Domain_Length', 'Subdomain_Level', 'Have_At_Sign', 'Have_Tilde_Symbol', 'No_Https', 'Having_IP', 'Domain_In_Subdomains', 'Domain_In_Paths', 'Http_In_Hostname', 'Double_Slash_In_Path', 'Num_Dots', 'Num_Dashes_In_Hostname', 'Num_Underscore', 'Num_Percent', 'Num_Ampersand', 'Num_Hash', 'Num_Numeric_Chars', 'Num_Sensitive_Words', 'Ext_Favicon', 'Redirection', 'Tiny_URL', 'Prefix_Suffix', 'DNS', 'Domain_Age', 'Domain_End', 'Rank_Host', 'Rank_Country', 'Iframe', 'Mouse_Over', 'Right_Click', 'Forwarding']