import pandas as pd
import pandas as pd
from sklearn.preprocessing import LabelEncoder

columns = [  # 41 features + label
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
    'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins',
    'logged_in', 'num_compromised', 'root_shell', 'su_attempted',
    'num_root', 'num_file_creations', 'num_shells', 'num_access_files',
    'num_outbound_cmds', 'is_host_login', 'is_guest_login', 'count',
    'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate',
    'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate',
    'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
    'dst_host_same_srv_rate', 'dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate',
    'dst_host_serror_rate', 'dst_host_srv_serror_rate',
    'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'label'
]

import os

base_dir = os.path.dirname(os.path.abspath(__file__))
in_path = os.path.join(base_dir, "data", "KDDTrain_plus.txt")
if not os.path.exists(in_path):
    in_path = os.path.join(base_dir, "KDDTrain_plus.txt")

out_path = os.path.join(base_dir, "data", "nsl_kdd_cleaned.csv") if os.path.exists(os.path.join(base_dir, "data")) else os.path.join(base_dir, "nsl_kdd_cleaned.csv")

df = pd.read_csv(in_path, header=None, names=columns)
df.to_csv(out_path, index=False)
print(f"✅ Cleaned dataset saved to {out_path}")

