import warnings
import pandas as pd
warnings.filterwarnings('ignore')

base_path = r"E:\project\20210928_loan\data"
train_bank = pd.read_csv(base_path + r'\train_public.csv')
train_internet = pd.read_csv(base_path + r'\train_internet.csv')

test = pd.read_csv(base_path+ r'\test_public.csv')

train_bank.columns = ['loan_id', 'user_id', 'total_loan', 'year_of_loan', 'interest',
       'monthly_payment', 'class', 'employer_type', 'industry', 'work_year',
       'house_exist', 'censor_status', 'issue_date', 'use', 'post_code',
       'region', 'debt_loan_ratio', 'del_in_18month', 'scoring_low',
       'scoring_high', 'known_outstanding_loan', 'known_dero',
       'pub_dero_bankrup', 'recircle_b', 'recircle_u', 'initial_list_status',
       'app_type', 'earlies_credit_mon', 'title', 'policy_code', 'f0', 'f1',
       'f2', 'f3', 'f4', 'early_return', 'early_return_amount',
       'early_return_amount_3mon', 'is_default']
       
# ### 数据预处理

common_cols = []
for col in train_bank.columns:
    if col in train_internet.columns:
        common_cols.append(col)
    else: continue
len(common_cols)


print(len(train_bank.columns))
print(len(train_internet.columns))


train_bank_left = list(set(list(train_bank.columns)) - set(common_cols))
train_internet_left = list(set(list(train_internet.columns)) - set(common_cols))



train1_data = train_internet[common_cols]
train2_data = train_bank[common_cols]
test_data = test[common_cols[:-1]]


