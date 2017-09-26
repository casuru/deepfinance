import pandas as pd

def make_dataset(symbol):

    f = 'https://serveup-casuru.c9users.io/static/data/s&p/{0}.csv'.format(symbol)
    stock = pd.read_csv(f)
    stock = stock.sort_values(by = 'timestamp', ascending = True)
    stock = stock[["open", "high", "low", "close"]]
        
    inputs, targets = [], []
    for ii in range(5, len(feature_frame.iloc[:,:])):
        
        input_ = []
        
        for trailing in range(num_trailing):
            index = ii - (trailing + 1)
            input_.insert(0, np.array(feature_frame.iloc[index, :]))
            
        if input_[-1][-1] > np.array(feature_frame.iloc[ii,:])[-1]:
            
            targets.append(0)
        else:
            targets.append(1)
            
        inputs.append(input_)
        
    return np.array(inputs), np.array(targets)