module specialFunctions

export formatDataset3, formatDataset2

using DataFrames
using Dates

function formatDataset(data)
    df = DataFrame(data)
    df.datetime = DateTime.(df.date)
    select!(df, Not(:date))
    return df
end

function formatDataset1(df)
    columns_to_convert = [:open, :high, :low, :close, :volume]
    df[!, columns_to_convert] .= float.(df[!, columns_to_convert])
    return df
end






end