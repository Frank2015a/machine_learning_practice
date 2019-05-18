from contextlib import contextmanager
import time
import json
import requests
import socket
import sys


@contextmanager
def gc2():
    gc.enable()
    yield
    gc.collect()

@contextmanager
def timer(title='do'):
    t0 = time.time()
    yield
    print("{} - done in {:.4f}s".format(title, time.time() - t0))


# def bot(message, phones=phones, token=token):
def ding(message):
    token = "130fe712252513ab163f9453dbe9bdc9efca01eb3a7f1def85a5f6d89dc7c358"
    phones = [17621684529]
    url = 'https://oapi.dingtalk.com/robot/send'
    params = { 'access_token': token }
    headers = { 'Content-Type': 'application/json' }
    data = json.dumps({
        "msgtype": "text",
        "text": {
            "content": message + "\n" +
                       time.strftime('%Y/%m/%d %H:%M:%S') + "\n" +
                       socket.gethostname()},
        "at": {"atMobiles": phones},
    })
    return requests.post(url, headers=headers, params=params, data=data)



def convert_types(df, print_info = False):
    original_memory = df.memory_usage().sum()
    # Iterate through each column
    for c in df:        
        # Convert ids and booleans to integers
        if ('SK_ID' in c):
            df[c] = df[c].fillna(0).astype(np.int32)            
        # Convert objects to category
        elif (df[c].dtype == 'object') and (df[c].nunique() < df.shape[0]):
            df[c] = df[c].astype('category')        
        # Booleans mapped to integers
        elif list(df[c].unique()) == [1, 0]:
            df[c] = df[c].astype(bool)        
        # Float64 to float32
        elif df[c].dtype == float:
            df[c] = df[c].astype(np.float32)            
        # Int64 to int32
        elif df[c].dtype == int:
            df[c] = df[c].astype(np.int32)
        
    new_memory = df.memory_usage().sum()    
    if print_info:
        print(f'Original Memory Usage: {round(original_memory / 1e9, 2)} gb.')
        print(f'New Memory Usage: {round(new_memory / 1e9, 2)} gb.')
    return df


def df_null_stat(df, thres_null=0.5):
    """
    args:
        - thres_null, thres to filter cols to drop
    return:
        - df_null, df of null ratios 
    useage:
    df_null, col_drop = df_null_stat(df, 0.5)
    """ 
    df_null = pd.DataFrame(df.isnull().sum() / df.shape[0])
    df_null.rename(columns={0:'null_ratio'}, inplace=True);
    df_null = df_null.sort_values(by='null_ratio', ascending=False)
    
    num_null = df_null[df_null.null_ratio > thres_null].shape[0]
    print('num of col null ratio>{}: {}'.format(thres_null, num_null))
    cols_drop = list(df_null[df_null.null_ratio > thres_null].index)

    return df_null, cols_drop
