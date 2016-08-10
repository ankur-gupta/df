import pandas as pd


def pdapply(groupby_obj, func):
    ''' Easy Apply '''
    func_output_list = [func(df) for i, df in groupby_obj]
    df = pd.concat(func_output_list)
    return df


# def func1(df):
#     df['mean'] = df['b']
#     return df

# df = pd.DataFrame({'a': range(10), 'b': range(10), 'c': range(10)})
# groupby_obj = df.groupby('a')
# dfnew = pdapply(groupby_obj, func1)
# print dfnew

